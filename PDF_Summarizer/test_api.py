#!/usr/bin/env python3
"""
Test script for PDF Summarizer API
Tests all endpoints with sample data
"""

import requests
import json
from pathlib import Path

# Configuration
API_BASE_URL = "http://localhost:8000"
TIMEOUT = 30

def print_section(title):
    """Print formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")

def test_health():
    """Test health endpoint"""
    print_section("TEST 1: Health Check")
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=TIMEOUT)
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_root():
    """Test root endpoint"""
    print_section("TEST 2: Root Endpoint")
    try:
        response = requests.get(f"{API_BASE_URL}/", timeout=TIMEOUT)
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Service: {data.get('service')}")
        print(f"Version: {data.get('version')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def create_test_pdf():
    """Create a simple test PDF file"""
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        test_pdf_path = Path("test_document.pdf")
        
        c = canvas.Canvas(str(test_pdf_path), pagesize=letter)
        
        # Page 1
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, 750, "Test Document - Page 1")
        c.setFont("Helvetica", 12)
        c.drawString(50, 700, "This is a test PDF document for the summarizer.")
        c.drawString(50, 680, "It contains multiple pages with different content.")
        c.drawString(50, 660, "The summarizer should extract and summarize this text.")
        c.drawString(50, 640, "Page 1 introduces the document structure and purpose.")
        
        # Page 2
        c.showPage()
        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, 750, "Test Document - Page 2")
        c.setFont("Helvetica", 12)
        c.drawString(50, 700, "This is the second page of the test document.")
        c.drawString(50, 680, "It contains additional content for testing.")
        c.drawString(50, 660, "The summarizer should handle multiple pages correctly.")
        c.drawString(50, 640, "Page 2 provides more detail about the test content.")
        
        c.save()
        print(f"✅ Test PDF created: {test_pdf_path}")
        return test_pdf_path
    
    except ImportError:
        print("⚠️  reportlab not installed. Using existing PDF or skipping upload test.")
        # Look for any existing PDF in current directory
        pdfs = list(Path(".").glob("*.pdf"))
        if pdfs:
            return pdfs[0]
        return None

def test_summarize(pdf_path):
    """Test PDF summarization"""
    print_section("TEST 3: Summarize PDF")
    
    if not pdf_path or not pdf_path.exists():
        print("❌ No PDF file found. Skipping upload test.")
        return False
    
    try:
        with open(pdf_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(
                f"{API_BASE_URL}/api/summarize",
                files=files,
                timeout=TIMEOUT
            )
        
        print(f"Status: {response.status_code}")
        data = response.json()
        
        print(f"File: {data.get('file_name')}")
        print(f"Total Pages: {data.get('total_pages')}")
        print(f"Status: {data.get('status')}")
        print(f"\nDocument Summary:")
        print(f"{data.get('document_summary')}")
        
        print(f"\nPage Summaries:")
        for page_summary in data.get('page_summaries', []):
            print(f"\n  Page {page_summary['page_number']}:")
            print(f"  Method: {page_summary['method']}")
            print(f"  Summary: {page_summary['summary'][:200]}...")
        
        return response.status_code == 200
    
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_list_summaries():
    """Test listing summaries"""
    print_section("TEST 4: List Summaries")
    try:
        response = requests.get(f"{API_BASE_URL}/api/summaries", timeout=TIMEOUT)
        print(f"Status: {response.status_code}")
        data = response.json()
        print(f"Total Summaries: {data.get('total')}")
        print(f"Files: {data.get('summaries')}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_api_documentation():
    """Test API documentation availability"""
    print_section("TEST 5: API Documentation")
    try:
        response = requests.get(f"{API_BASE_URL}/docs", timeout=TIMEOUT)
        if response.status_code == 200:
            print("✅ API documentation available at /docs")
            return True
        else:
            print(f"⚠️  Status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def run_all_tests():
    """Run all tests"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║         PDF Summarizer API - Test Suite                   ║")
    print("║  Make sure backend is running on http://localhost:8000    ║")
    print("╚════════════════════════════════════════════════════════════╝")
    
    results = []
    
    # Basic connectivity tests
    results.append(("Health Check", test_health()))
    results.append(("Root Endpoint", test_root()))
    results.append(("API Documentation", test_api_documentation()))
    
    # File upload test
    pdf_path = create_test_pdf()
    results.append(("Summarize PDF", test_summarize(pdf_path)))
    
    # Data retrieval tests
    results.append(("List Summaries", test_list_summaries()))
    
    # Summary
    print_section("TEST SUMMARY")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! API is working correctly.")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Check backend logs.")

if __name__ == "__main__":
    run_all_tests()
