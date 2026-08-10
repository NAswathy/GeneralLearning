# Quick Start Guide - PDF Summarizer Agent

## 🚀 5-Minute Setup

### Option 1: Using Docker (Easiest)

```bash
# Prerequisites: Docker and Docker Compose installed

# 1. Build and run
docker-compose up -d

# 2. Open browser
# Backend API: http://localhost:8000
# Frontend: http://localhost:3000
# API Docs: http://localhost:8000/docs

# 3. View logs
docker-compose logs -f backend
```

### Option 2: Manual Setup (Linux/Mac)

```bash
# 1. Run setup script
chmod +x setup.sh
./setup.sh

# 2. In Terminal 1 - Start Backend
source venv/bin/activate
python main.py

# 3. In Terminal 2 - Start Frontend (if chosen)
cd pdf-summarizer-ui
npm start

# 4. Open http://localhost:3000
```

### Option 3: Manual Setup (Windows)

```bash
# 1. Create virtual environment
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
copy .env.example .env

# 4. Start backend
python main.py

# 5. In another terminal - Start frontend
cd pdf-summarizer-ui
npm start
```

## 🧪 Testing the API

### Option A: Web Interface (Visual)
```
Open: http://localhost:3000
Upload a PDF and click "Summarize PDF"
```

### Option B: Command Line
```bash
# 1. Test API health
python pdf_cli.py health

# 2. Summarize a PDF
python pdf_cli.py summarize document.pdf

# 3. Get JSON output
python pdf_cli.py summarize document.pdf --json

# 4. List all summaries
python pdf_cli.py list

# 5. View specific summary
python pdf_cli.py get document.pdf
```

### Option C: Python Script
```python
import requests

# Upload and summarize
with open('document.pdf', 'rb') as f:
    response = requests.post(
        'http://localhost:8000/api/summarize',
        files={'file': f}
    )

result = response.json()
print(result['document_summary'])
```

### Option D: cURL
```bash
# Summarize PDF
curl -X POST -F "file=@document.pdf" \
  http://localhost:8000/api/summarize

# Check health
curl http://localhost:8000/health

# List summaries
curl http://localhost:8000/api/summaries

# View interactive docs
open http://localhost:8000/docs
```

## 📋 Features

✅ **Extract Text** - Automatically extract text from PDF files
✅ **Page-by-Page** - Summarize each page individually
✅ **AI Summaries** - Use OpenAI GPT-3.5 for quality summaries
✅ **Offline Mode** - Local summarization works without API key
✅ **REST API** - Full API for programmatic access
✅ **Web UI** - Beautiful React interface
✅ **Storage** - Keep summaries in memory for quick retrieval

## 🔑 Add OpenAI API Key (Optional)

1. Get key from: https://platform.openai.com/api-keys
2. Edit `.env` file:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```
3. Restart backend for changes to take effect

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Check API status |
| POST | `/api/summarize` | Upload and summarize PDF |
| GET | `/api/summary/{filename}` | Get stored summary |
| GET | `/api/summaries` | List all summaries |
| DELETE | `/api/summary/{filename}` | Delete summary |
| GET | `/docs` | Interactive API documentation |

## 🐛 Troubleshooting

### Backend won't start
```bash
# Check if port 8000 is in use
lsof -i :8000
# Kill process and try again
kill -9 <PID>
```

### Frontend won't connect
```bash
# Make sure backend is running
curl http://localhost:8000/health
# Check backend logs for errors
```

### PDF upload fails
- Check file is valid PDF
- Check file size < 50MB
- Check backend logs

### No summaries shown
- Check OpenAI API key if using GPT-3.5
- Fallback to local summarization is automatic

## 📖 Documentation

- **Full Docs**: See `README.md`
- **API Docs**: http://localhost:8000/docs (Swagger UI)
- **Source Code**: See individual Python files for docstrings

## 🛑 Stop Services

### Docker
```bash
docker-compose down
```

### Manual
```bash
# Terminal 1: Ctrl+C
# Terminal 2: Ctrl+C
```

## 💡 Next Steps

1. ✅ Test with sample PDF
2. ✅ Add your OpenAI API key for better quality
3. ✅ Explore the `/docs` page for full API reference
4. ✅ Integrate into your application using REST API
5. ✅ Deploy to cloud (AWS, GCP, Azure)

## 🎓 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com/
- **React**: https://react.dev/
- **OpenAI API**: https://platform.openai.com/docs/
- **PyPDF2**: https://github.com/py-pdf/PyPDF2

## 🤝 Support

- Check logs: `python main.py` (backend)
- Browser console: F12 (frontend)
- API health: `curl http://localhost:8000/health`
- Full README: `README.md`

## 📦 Project Structure

```
PDF_Summarizer/
├── main.py              # FastAPI application
├── config.py            # Configuration
├── pdf_processor.py     # PDF extraction
├── summarizer.py        # Summarization engine
├── PDFSummarizer.tsx    # React component
├── PDFSummarizer.css    # Styling
├── pdf_cli.py           # CLI tool
├── test_api.py          # Test suite
├── setup.sh             # Setup script
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
└── README.md            # Full documentation
```

---

**Happy Summarizing! 📚✨**

For more details, see `README.md` in the project directory.
