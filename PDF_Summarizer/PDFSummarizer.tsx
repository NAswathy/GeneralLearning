import React, { useState, useRef } from 'react';
import axios from 'axios';
import './PDFSummarizer.css';

const API_BASE_URL = 'http://localhost:8000';

interface PageSummary {
  page_number: number;
  summary: string;
  word_count?: number;
  method: string;
}

interface SummaryResponse {
  file_name: string;
  total_pages: number;
  page_summaries: PageSummary[];
  document_summary: string;
  status: string;
}

const PDFSummarizer: React.FC = () => {
  const [file, setFile] = useState<File | null>(null);
  const [loading, setLoading] = useState(false);
  const [summary, setSummary] = useState<SummaryResponse | null>(null);
  const [error, setError] = useState<string>('');
  const [expandedPage, setExpandedPage] = useState<number | null>(null);
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileSelect = (e: React.ChangeEvent<HTMLInputElement>) => {
    const selectedFile = e.target.files?.[0];
    if (selectedFile && selectedFile.type === 'application/pdf') {
      setFile(selectedFile);
      setError('');
    } else {
      setError('Please select a valid PDF file');
      setFile(null);
    }
  };

  const handleUpload = async () => {
    if (!file) {
      setError('Please select a PDF file');
      return;
    }

    setLoading(true);
    setError('');

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post(`${API_BASE_URL}/api/summarize`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });

      setSummary(response.data);
      setFile(null);
      if (fileInputRef.current) {
        fileInputRef.current.value = '';
      }
    } catch (err: any) {
      setError(
        err.response?.data?.detail ||
        'Error uploading PDF. Make sure the backend is running.'
      );
    } finally {
      setLoading(false);
    }
  };

  const togglePageExpansion = (pageNumber: number) => {
    setExpandedPage(expandedPage === pageNumber ? null : pageNumber);
  };

  return (
    <div className="pdf-summarizer">
      <header className="header">
        <h1>📄 PDF Summarizer Agent</h1>
        <p>Upload a PDF and get intelligent page-by-page summaries</p>
      </header>

      <div className="container">
        {/* Upload Section */}
        <div className="upload-section">
          <div className="upload-box">
            <input
              ref={fileInputRef}
              type="file"
              accept=".pdf"
              onChange={handleFileSelect}
              className="file-input"
              disabled={loading}
            />
            <label className="file-label">
              <span className="upload-icon">📁</span>
              <span className="upload-text">
                {file ? file.name : 'Click to select PDF or drag and drop'}
              </span>
            </label>
          </div>

          <button
            onClick={handleUpload}
            disabled={!file || loading}
            className="upload-button"
          >
            {loading ? 'Processing...' : 'Summarize PDF'}
          </button>

          {error && <div className="error-message">{error}</div>}
        </div>

        {/* Results Section */}
        {summary && (
          <div className="results-section">
            <div className="summary-header">
              <h2>Summary Results</h2>
              <span className="file-info">
                {summary.file_name} • {summary.total_pages} pages
              </span>
            </div>

            {/* Document Summary */}
            <div className="document-summary">
              <h3>📋 Document Overview</h3>
              <p>{summary.document_summary}</p>
            </div>

            {/* Page Summaries */}
            <div className="pages-section">
              <h3>📑 Page-by-Page Summaries</h3>
              <div className="pages-list">
                {summary.page_summaries.map((page) => (
                  <div
                    key={page.page_number}
                    className={`page-item ${
                      expandedPage === page.page_number ? 'expanded' : ''
                    }`}
                  >
                    <div
                      className="page-header"
                      onClick={() => togglePageExpansion(page.page_number)}
                    >
                      <span className="page-number">
                        Page {page.page_number}
                      </span>
                      <span className="page-meta">
                        {page.word_count && `${page.word_count} words`}
                        <span className="method-badge">{page.method}</span>
                      </span>
                      <span className="expand-icon">
                        {expandedPage === page.page_number ? '▼' : '▶'}
                      </span>
                    </div>
                    {expandedPage === page.page_number && (
                      <div className="page-summary">
                        <p>{page.summary}</p>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>

            <button
              onClick={() => setSummary(null)}
              className="reset-button"
            >
              ← Process Another PDF
            </button>
          </div>
        )}

        {/* Empty State */}
        {!summary && !loading && (
          <div className="empty-state">
            <p>Upload a PDF to get started! 🚀</p>
          </div>
        )}
      </div>
    </div>
  );
};

export default PDFSummarizer;
