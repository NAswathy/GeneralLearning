from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from typing import List, Dict, Optional
import shutil
import os
from pathlib import Path
from datetime import datetime

from config import settings
from pdf_processor import PDFProcessor
from summarizer import PDFSummarizer

# Initialize FastAPI app
app = FastAPI(
    title=settings.api_title,
    version=settings.api_version,
    description="PDF Summarization Agent - Summarizes PDF documents page by page"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create temp directory for uploads
UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


# Models
class PageSummary(BaseModel):
    page_number: int
    text: str
    summary: str
    word_count: int
    method: str


class SummaryResponse(BaseModel):
    file_name: str
    total_pages: int
    upload_time: str
    page_summaries: List[Dict]
    document_summary: str
    status: str


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str
    openai_available: bool


# Global storage for processed PDFs
processed_pdfs = {}


# Routes
@app.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return HealthResponse(
        status="healthy",
        service=settings.api_title,
        version=settings.api_version,
        openai_available=bool(settings.openai_api_key)
    )


@app.post("/api/summarize", response_model=SummaryResponse)
async def summarize_pdf(file: UploadFile = File(...)):
    """
    Upload and summarize a PDF file
    
    Args:
        file: PDF file to summarize
        
    Returns:
        Summary of the PDF with page-by-page analysis
    """
    if not file.filename:
        raise HTTPException(status_code=400, detail="No file provided")
    
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    # Check file size
    file_size = len(await file.read())
    await file.seek(0)  # Reset file pointer
    
    if file_size > settings.max_file_size:
        raise HTTPException(
            status_code=413,
            detail=f"File size exceeds maximum allowed size ({settings.max_file_size / 1024 / 1024}MB)"
        )
    
    try:
        # Save uploaded file
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Extract text from PDF
        processor = PDFProcessor()
        pages_data = processor.extract_text_from_pdf(str(file_path))
        
        # Summarize pages
        summarizer = PDFSummarizer()
        page_summaries = summarizer.summarize_all_pages(pages_data)
        
        # Generate overall document summary
        document_summary = summarizer.generate_document_summary(page_summaries)
        
        # Prepare response
        response_data = {
            "file_name": file.filename,
            "total_pages": processor.get_total_pages(),
            "upload_time": datetime.now().isoformat(),
            "page_summaries": page_summaries,
            "document_summary": document_summary,
            "status": "completed"
        }
        
        # Store for later retrieval
        processed_pdfs[file.filename] = response_data
        
        return response_data
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    
    finally:
        # Clean up uploaded file
        try:
            if file_path.exists():
                file_path.unlink()
        except:
            pass


@app.get("/api/summary/{filename}")
async def get_summary(filename: str):
    """Retrieve previously processed PDF summary"""
    if filename not in processed_pdfs:
        raise HTTPException(status_code=404, detail="PDF summary not found")
    
    return processed_pdfs[filename]


@app.get("/api/summaries")
async def list_summaries():
    """List all processed PDF summaries"""
    return {
        "total": len(processed_pdfs),
        "summaries": list(processed_pdfs.keys())
    }


@app.delete("/api/summary/{filename}")
async def delete_summary(filename: str):
    """Delete a stored PDF summary"""
    if filename not in processed_pdfs:
        raise HTTPException(status_code=404, detail="PDF summary not found")
    
    del processed_pdfs[filename]
    return {"status": "deleted", "filename": filename}


@app.get("/")
async def root():
    """Root endpoint with API documentation"""
    return {
        "service": settings.api_title,
        "version": settings.api_version,
        "description": "Upload a PDF and get page-by-page summaries",
        "endpoints": {
            "health": "/health",
            "summarize": "POST /api/summarize",
            "get_summary": "GET /api/summary/{filename}",
            "list_summaries": "GET /api/summaries",
            "delete_summary": "DELETE /api/summary/{filename}"
        },
        "docs": "/docs",
        "openapi_schema": "/openapi.json"
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )
