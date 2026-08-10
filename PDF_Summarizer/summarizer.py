from typing import List, Dict
import os
from config import settings


class PDFSummarizer:
    """Handles PDF summarization using AI"""
    
    def __init__(self):
        self.use_openai = bool(settings.openai_api_key)
        if self.use_openai:
            try:
                from openai import OpenAI
                self.client = OpenAI(api_key=settings.openai_api_key)
            except ImportError:
                raise ImportError("openai package required for AI summarization")
    
    def summarize_page(self, page_text: str, page_number: int) -> Dict[str, str]:
        """
        Summarize a single page
        
        Args:
            page_text: Text content of the page
            page_number: Page number for reference
            
        Returns:
            Dictionary with page number and summary
        """
        if not page_text.strip():
            return {
                "page_number": page_number,
                "summary": "[Empty page]",
                "method": "local"
            }
        
        if self.use_openai:
            return self._summarize_with_openai(page_text, page_number)
        else:
            return self._summarize_local(page_text, page_number)
    
    def _summarize_with_openai(self, page_text: str, page_number: int) -> Dict[str, str]:
        """Summarize using OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {
                        "role": "system",
                        "content": "You are a helpful assistant that summarizes document content concisely and accurately."
                    },
                    {
                        "role": "user",
                        "content": f"Please summarize the following text in 3-5 sentences:\n\n{page_text[:2000]}"
                    }
                ],
                max_tokens=300,
                temperature=0.5
            )
            
            summary = response.choices[0].message.content
            
            return {
                "page_number": page_number,
                "summary": summary,
                "method": "openai"
            }
        
        except Exception as e:
            # Fallback to local summarization on error
            return self._summarize_local(page_text, page_number)
    
    def _summarize_local(self, page_text: str, page_number: int) -> Dict[str, str]:
        """Local summarization using simple heuristics"""
        sentences = page_text.split('. ')
        word_count = len(page_text.split())
        
        # Extract summary sentences (first and important ones)
        summary_sentences = []
        for i, sentence in enumerate(sentences[:3]):
            if sentence.strip():
                summary_sentences.append(sentence.strip() + ".")
        
        summary = " ".join(summary_sentences) if summary_sentences else "[No extractable summary]"
        
        return {
            "page_number": page_number,
            "summary": summary,
            "method": "local",
            "word_count": word_count
        }
    
    def summarize_all_pages(self, pages_data: List[Dict]) -> List[Dict[str, str]]:
        """
        Summarize all pages
        
        Args:
            pages_data: List of page data from PDFProcessor
            
        Returns:
            List of summaries for each page
        """
        summaries = []
        for page in pages_data:
            summary = self.summarize_page(page["text"], page["page_number"])
            summaries.append(summary)
        
        return summaries
    
    def generate_document_summary(self, pages_summaries: List[Dict]) -> str:
        """
        Generate an overall document summary from page summaries
        
        Args:
            pages_summaries: List of page summaries
            
        Returns:
            Overall document summary
        """
        combined_summaries = "\n".join([
            f"Page {s['page_number']}: {s['summary']}"
            for s in pages_summaries
        ])
        
        if self.use_openai:
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {
                            "role": "system",
                            "content": "You are an expert at creating concise document summaries."
                        },
                        {
                            "role": "user",
                            "content": f"Based on these page summaries, create a comprehensive document summary (5-7 sentences):\n\n{combined_summaries}"
                        }
                    ],
                    max_tokens=500,
                    temperature=0.5
                )
                
                return response.choices[0].message.content
            
            except Exception as e:
                return combined_summaries[:500]  # Fallback
        
        return combined_summaries
