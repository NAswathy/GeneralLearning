#!/bin/bash

# PDF Summarizer Setup Script
# This script sets up both backend and frontend

set -e

echo "╔════════════════════════════════════════════════════════════╗"
echo "║     PDF Summarizer Agent - Setup Script                   ║"
echo "╚════════════════════════════════════════════════════════════╝"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check Python
echo -e "\n${BLUE}Checking Python installation...${NC}"
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
echo -e "${GREEN}✅ Found Python $PYTHON_VERSION${NC}"

# Setup Backend
echo -e "\n${BLUE}Setting up Backend...${NC}"

# Create virtual environment
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo -e "${GREEN}✅ Virtual environment created${NC}"
else
    echo -e "${GREEN}✅ Virtual environment already exists${NC}"
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
echo "Installing Python dependencies..."
pip install --upgrade pip setuptools wheel > /dev/null 2>&1
pip install -r requirements.txt > /dev/null 2>&1
echo -e "${GREEN}✅ Backend dependencies installed${NC}"

# Create .env file if it doesn't exist
if [ ! -f ".env" ]; then
    cp .env.example .env
    echo -e "${GREEN}✅ Created .env file (edit to add OpenAI API key)${NC}"
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

# Create uploads directory
mkdir -p uploads
echo -e "${GREEN}✅ Uploads directory ready${NC}"

# Setup Frontend (Optional)
echo -e "\n${BLUE}Frontend Setup (Optional)${NC}"
echo "Choose an option:"
echo "1. Setup React frontend with npm"
echo "2. Skip frontend setup (use API directly)"
read -p "Enter choice (1 or 2): " choice

if [ "$choice" = "1" ]; then
    if ! command -v npm &> /dev/null; then
        echo "❌ npm is not installed. Please install Node.js and npm."
        exit 1
    fi
    
    NPM_VERSION=$(npm --version)
    echo -e "${GREEN}✅ Found npm $NPM_VERSION${NC}"
    
    if [ ! -d "pdf-summarizer-ui" ]; then
        echo "Creating React app..."
        npx create-react-app pdf-summarizer-ui --template typescript
    fi
    
    cd pdf-summarizer-ui
    echo "Installing frontend dependencies..."
    npm install axios > /dev/null 2>&1
    echo -e "${GREEN}✅ Frontend dependencies installed${NC}"
    
    # Copy component files
    mkdir -p src/components
    cp ../PDFSummarizer.tsx src/components/
    cp ../PDFSummarizer.css src/components/
    
    echo -e "${GREEN}✅ React components copied${NC}"
    
    cd ..
fi

# Print next steps
echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}"
echo -e "${GREEN}Setup Complete! 🎉${NC}"
echo -e "${BLUE}═══════════════════════════════════════════════════════════${NC}"

echo -e "\n${BLUE}Next Steps:${NC}"
echo -e "\n1. ${GREEN}Start Backend:${NC}"
echo "   source venv/bin/activate"
echo "   python main.py"
echo "   Backend will run at: http://localhost:8000"

if [ "$choice" = "1" ]; then
    echo -e "\n2. ${GREEN}Start Frontend (in another terminal):${NC}"
    echo "   cd pdf-summarizer-ui"
    echo "   npm start"
    echo "   Frontend will run at: http://localhost:3000"
else
    echo -e "\n2. ${GREEN}Test API:${NC}"
    echo "   python test_api.py"
fi

echo -e "\n3. ${GREEN}View API Documentation:${NC}"
echo "   http://localhost:8000/docs"

echo -e "\n4. ${GREEN}Optional: Add OpenAI API Key${NC}"
echo "   Edit .env file and add your OPENAI_API_KEY for better summarization"

echo -e "\n${BLUE}═══════════════════════════════════════════════════════════${NC}\n"
