#!/usr/bin/env python3
"""
CLI Tool for PDF Summarizer Agent
Provides command-line interface to interact with the API
"""

import argparse
import sys
from pathlib import Path
import requests
import json
from tabulate import tabulate

API_BASE_URL = "http://localhost:8000"

class PDFSummarizerCLI:
    def __init__(self):
        self.api_url = API_BASE_URL
    
    def health(self):
        """Check API health"""
        try:
            response = requests.get(f"{self.api_url}/health", timeout=5)
            data = response.json()
            print("✅ API Status:")
            print(f"  Service: {data.get('service')}")
            print(f"  Version: {data.get('version')}")
            print(f"  Status: {data.get('status')}")
            print(f"  OpenAI Available: {data.get('openai_available')}")
        except Exception as e:
            print(f"❌ Error: Could not connect to API at {self.api_url}")
            print(f"   Make sure backend is running: python main.py")
    
    def summarize(self, pdf_path, output_format='text'):
        """Summarize a PDF file"""
        pdf_file = Path(pdf_path)
        
        if not pdf_file.exists():
            print(f"❌ File not found: {pdf_path}")
            return
        
        if not pdf_file.suffix.lower() == '.pdf':
            print(f"❌ File must be a PDF: {pdf_path}")
            return
        
        print(f"📄 Processing: {pdf_file.name}")
        print("⏳ Uploading and summarizing...")
        
        try:
            with open(pdf_file, 'rb') as f:
                files = {'file': f}
                response = requests.post(
                    f"{self.api_url}/api/summarize",
                    files=files,
                    timeout=300
                )
            
            if response.status_code != 200:
                print(f"❌ Error: {response.json().get('detail', 'Unknown error')}")
                return
            
            data = response.json()
            
            if output_format == 'json':
                print(json.dumps(data, indent=2))
            else:
                self._print_summary_text(data)
        
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def _print_summary_text(self, data):
        """Pretty print summary in text format"""
        print(f"\n{'='*70}")
        print(f"SUMMARY: {data['file_name']}")
        print(f"{'='*70}\n")
        
        print(f"📊 Document Info:")
        print(f"   Total Pages: {data['total_pages']}")
        print(f"   Upload Time: {data['upload_time']}")
        print(f"   Status: {data['status']}\n")
        
        print(f"📋 DOCUMENT SUMMARY:")
        print(f"{'-'*70}")
        print(data['document_summary'])
        print()
        
        print(f"📑 PAGE-BY-PAGE SUMMARIES:")
        print(f"{'-'*70}\n")
        
        for page in data['page_summaries']:
            print(f"📄 PAGE {page['page_number']}")
            print(f"   Method: {page['method']}")
            if 'word_count' in page:
                print(f"   Words: {page['word_count']}")
            print(f"   Summary: {page['summary']}")
            print()
    
    def list_summaries(self):
        """List all processed summaries"""
        try:
            response = requests.get(f"{self.api_url}/api/summaries", timeout=5)
            data = response.json()
            
            if data['total'] == 0:
                print("No summaries stored yet.")
                return
            
            print(f"📚 Stored Summaries ({data['total']}):")
            for filename in data['summaries']:
                print(f"   • {filename}")
        
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def get_summary(self, filename, output_format='text'):
        """Get a stored summary"""
        try:
            response = requests.get(
                f"{self.api_url}/api/summary/{filename}",
                timeout=5
            )
            
            if response.status_code == 404:
                print(f"❌ Summary not found: {filename}")
                return
            
            data = response.json()
            
            if output_format == 'json':
                print(json.dumps(data, indent=2))
            else:
                self._print_summary_text(data)
        
        except Exception as e:
            print(f"❌ Error: {e}")
    
    def delete_summary(self, filename):
        """Delete a stored summary"""
        try:
            response = requests.delete(
                f"{self.api_url}/api/summary/{filename}",
                timeout=5
            )
            
            if response.status_code == 200:
                print(f"✅ Deleted: {filename}")
            else:
                print(f"❌ Error: {response.json().get('detail', 'Unknown error')}")
        
        except Exception as e:
            print(f"❌ Error: {e}")

def main():
    parser = argparse.ArgumentParser(
        description='PDF Summarizer Agent CLI',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python pdf_cli.py summarize document.pdf
  python pdf_cli.py summarize document.pdf --json
  python pdf_cli.py list
  python pdf_cli.py get document.pdf
  python pdf_cli.py delete document.pdf
  python pdf_cli.py health
        '''
    )
    
    parser.add_argument(
        '--api-url',
        default='http://localhost:8000',
        help='API base URL (default: http://localhost:8000)'
    )
    
    parser.add_argument(
        '--json',
        action='store_true',
        help='Output as JSON'
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commands')
    
    # Health command
    subparsers.add_parser('health', help='Check API health status')
    
    # Summarize command
    summarize_parser = subparsers.add_parser('summarize', help='Summarize a PDF file')
    summarize_parser.add_argument('pdf_file', help='Path to PDF file')
    
    # List command
    subparsers.add_parser('list', help='List all stored summaries')
    
    # Get command
    get_parser = subparsers.add_parser('get', help='Get a stored summary')
    get_parser.add_argument('filename', help='Filename of stored summary')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete', help='Delete a stored summary')
    delete_parser.add_argument('filename', help='Filename of stored summary')
    
    args = parser.parse_args()
    
    cli = PDFSummarizerCLI()
    cli.api_url = args.api_url
    
    output_format = 'json' if args.json else 'text'
    
    if args.command == 'health':
        cli.health()
    elif args.command == 'summarize':
        cli.summarize(args.pdf_file, output_format)
    elif args.command == 'list':
        cli.list_summaries()
    elif args.command == 'get':
        cli.get_summary(args.filename, output_format)
    elif args.command == 'delete':
        cli.delete_summary(args.filename)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
