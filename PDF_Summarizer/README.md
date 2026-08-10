# 📄 PDF Summarizer Agent

A complete web-based PDF summarization tool that extracts text from PDF files and generates intelligent summaries page by page. Built with FastAPI backend and React frontend.

## Features

✨ **Key Capabilities:**
- **Page-by-Page Summarization**: Get summaries for each page of your PDF
- **Document Overview**: Automatic generation of overall document summary
- **Dual Summarization Modes**: 
  - OpenAI GPT-3.5 (if API key provided)
  - Local heuristic-based summarization (works offline)
- **RESTful API**: Full API for integration with other applications
- **Modern UI**: Beautiful React interface with real-time processing
- **File Management**: Upload, store, and retrieve PDF summaries
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Architecture

```
PDF_Summarizer/
├── Backend (Python/FastAPI)
│   ├── main.py              # FastAPI application
│   ├── config.py            # Configuration management
│   ├── pdf_processor.py     # PDF text extraction
│   ├── summarizer.py        # Summarization engine
│   └── requirements.txt     # Python dependencies
├── Frontend (React/TypeScript)
│   ├── PDFSummarizer.tsx    # Main React component
│   └── PDFSummarizer.css    # Styling
├── .env.example             # Environment template
└── README.md               # This file
```

## Installation

### Prerequisites
- Python 3.8+
- Node.js 14+
- npm or yarn
- pip

### Backend Setup

1. **Clone/Navigate to project:**
```bash
cd PDF_Summarizer
```

2. **Create Python virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements.txt
```

4. **Setup environment variables:**
```bash
cp .env.example .env
# Edit .env and add your OpenAI API key (optional)
```

### Frontend Setup

1. **Create React app** (if not already created):
```bash
npx create-react-app pdf-summarizer-ui
cd pdf-summarizer-ui
```

2. **Install frontend dependencies:**
```bash
npm install axios
```

3. **Add the React component:**
- Copy `PDFSummarizer.tsx` to `src/components/`
- Copy `PDFSummarizer.css` to `src/components/`
- Import and use in your App.tsx:

```typescript
import PDFSummarizer from './components/PDFSummarizer';

function App() {
  return <PDFSummarizer />;
}
```

## Running the Application

### Start Backend

```bash
# From PDF_Summarizer directory with activated venv
python main.py
# or with uvicorn
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend runs at: `http://localhost:8000`

### Start Frontend

```bash
# From pdf-summarizer-ui directory
npm start
```

Frontend runs at: `http://localhost:3000`

## API Documentation

### Health Check
```bash
GET /health

Response:
{
  "status": "healthy",
  "service": "PDF Summarizer Agent",
  "version": "1.0.0",
  "openai_available": true
}
```

### Upload and Summarize PDF
```bash
POST /api/summarize
Content-Type: multipart/form-data

Request:
- file: <PDF file>

Response:
{
  "file_name": "document.pdf",
  "total_pages": 5,
  "upload_time": "2024-01-15T10:30:00",
  "page_summaries": [
    {
      "page_number": 1,
      "summary": "This page introduces...",
      "word_count": 450,
      "method": "openai"
    },
    ...
  ],
  "document_summary": "This document covers...",
  "status": "completed"
}
```

### Get Summary by Filename
```bash
GET /api/summary/{filename}

Response: Full summary object
```

### List All Summaries
```bash
GET /api/summaries

Response:
{
  "total": 3,
  "summaries": ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
}
```

### Delete Summary
```bash
DELETE /api/summary/{filename}

Response:
{
  "status": "deleted",
  "filename": "document.pdf"
}
```

## Using the Web Interface

1. **Open** `http://localhost:3000` in your browser
2. **Select a PDF** by clicking the upload area or dragging and dropping
3. **Click "Summarize PDF"** and wait for processing
4. **View Results**:
   - 📋 **Document Overview**: High-level summary of entire PDF
   - 📑 **Page Summaries**: Click to expand individual page summaries
   - **Method Badge**: Shows whether OpenAI or local summarization was used

## Configuration

Edit `.env` file to customize:

```env
# OpenAI Configuration
OPENAI_API_KEY=sk-your-api-key-here

# Application Settings
DEBUG=False
API_TITLE=PDF Summarizer Agent
API_VERSION=1.0.0

# File Upload Settings
MAX_FILE_SIZE=52428800  # 50MB in bytes
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | `` | OpenAI API key for GPT-3.5 summarization |
| `DEBUG` | `False` | Enable debug mode (reload on code changes) |
| `MAX_FILE_SIZE` | `52428800` | Max file size in bytes (default 50MB) |

## Summarization Methods

### OpenAI (Recommended)
- Requires: OpenAI API key
- Quality: High-quality, context-aware summaries
- Speed: 2-10 seconds per page
- Cost: ~$0.001-0.002 per page

### Local Heuristic
- Requires: None (offline)
- Quality: Extracts first 3 sentences
- Speed: Instant
- Cost: Free

The system automatically falls back to local summarization if OpenAI API fails.

## Examples

### Python Example
```python
import requests

# Upload PDF
with open('document.pdf', 'rb') as f:
    files = {'file': f}
    response = requests.post(
        'http://localhost:8000/api/summarize',
        files=files
    )

result = response.json()
print(f"Pages: {result['total_pages']}")
print(f"Summary: {result['document_summary']}")
```

### cURL Example
```bash
# Upload PDF
curl -X POST \
  -F "file=@document.pdf" \
  http://localhost:8000/api/summarize

# Get health status
curl http://localhost:8000/health

# List all summaries
curl http://localhost:8000/api/summaries
```

## Troubleshooting

### Backend won't start
```bash
# Check port 8000 is free
lsof -i :8000
# or kill process: kill -9 <PID>

# Check Python version
python --version  # Should be 3.8+

# Reinstall dependencies
pip install --upgrade -r requirements.txt
```

### Frontend won't connect to backend
- Ensure backend is running on port 8000
- Check CORS is enabled (it is by default)
- Check browser console for errors
- Try: `curl http://localhost:8000/health`

### OpenAI summarization not working
- Verify API key in `.env` file
- Test with: `echo $OPENAI_API_KEY`
- Fallback to local summarization is automatic

### PDF upload fails
- Check file size (max 50MB)
- Verify it's a valid PDF file
- Try a different PDF
- Check backend logs

## Performance Tips

- **Large PDFs**: Local summarization is faster for PDFs over 50 pages
- **Batch Processing**: Call API endpoint programmatically for bulk PDFs
- **Caching**: Keep processed summaries (they're stored in memory)

## Security Considerations

- ⚠️ Remove `OPENAI_API_KEY` before committing to version control
- File uploads stored temporarily, auto-deleted after processing
- Use HTTPS in production
- Validate file uploads on both frontend and backend
- Consider adding authentication for production

## Development

### Adding Custom Summarization Logic

Edit `summarizer.py`:
```python
def _summarize_custom(self, page_text: str, page_number: int):
    # Your custom summarization logic here
    pass
```

### Adding More Summarization Backends

1. Add new method to `PDFSummarizer` class
2. Update `summarize_page()` to use it
3. Add configuration option to `.env`

## Dependencies

### Python
- **fastapi**: Web framework
- **uvicorn**: ASGI server
- **PyPDF2**: PDF text extraction
- **openai**: OpenAI API client
- **pydantic**: Data validation

### Frontend
- **React**: UI framework
- **TypeScript**: Type safety
- **axios**: HTTP client

## License

MIT License - Feel free to use and modify!

## Contributing

Contributions welcome! Feel free to submit issues and pull requests.

## Support

For issues or questions, please check:
1. This README
2. Backend logs: `python main.py`
3. Frontend console: DevTools F12
4. API docs: `http://localhost:8000/docs`

## Roadmap

- [ ] Add document parsing for images (OCR)
- [ ] Support for multiple languages
- [ ] Batch PDF processing
- [ ] Export summaries (PDF, Word, Excel)
- [ ] Advanced summarization options (length control)
- [ ] User authentication and history
- [ ] Database integration (PostgreSQL)
- [ ] Docker containerization

---

**Happy Summarizing! 📚**
