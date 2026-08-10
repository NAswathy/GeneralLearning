from typing import List, Dict
import PyPDF2
import os
from pathlib import Path


class PDFProcessor:
    """Handles PDF extraction and text processing"""
    
    def __init__(self):
        self.extracted_text = []
    
    def extract_text_from_pdf(self, file_path: str) -> List[Dict[str, str]]:
        """
        Extract text from PDF file, page by page
        
        Args:
            file_path: Path to the PDF file
            
        Returns:
            List of dictionaries with page number and text content
        """
        pages_data = []
        
        try:
            with open(file_path, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                num_pages = len(pdf_reader.pages)
                
                for page_num in range(num_pages):
                    page = pdf_reader.pages[page_num]
                    text = page.extract_text()
                    
                    pages_data.append({
                        "page_number": page_num + 1,
                        "text": text.strip(),
                        "word_count": len(text.split())
                    })
        
        except Exception as e:
            raise Exception(f"Error extracting text from PDF: {str(e)}")
        
        self.extracted_text = pages_data
        return pages_data
    
    def get_page_text(self, page_number: int) -> str:
        """Get text from a specific page"""
        for page in self.extracted_text:
            if page["page_number"] == page_number:
                return page["text"]
        return ""
    
    def get_total_pages(self) -> int:
        """Get total number of pages"""
        return len(self.extracted_text)
