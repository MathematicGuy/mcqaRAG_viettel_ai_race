"""
RAG MCQ System - Production-ready RAG for Multiple Choice Question Answering.

This package provides a complete RAG system for answering multiple choice questions
from PDF documents, following production best practices from arxiv-paper-curator.

Main components:
- PDF parsing with Docling
- Section-aware text chunking
- Hybrid search (BM25 + Vector)
- LLM integration with Ollama
- Caching and monitoring

Example usage:
    from src.config import get_settings
    from src.services.rag.pipeline import RAGPipeline

    settings = get_settings()
    pipeline = RAGPipeline(...)

    result = await pipeline.answer_question(
        question="What is active learning?",
        options={"A": "...", "B": "...", "C": "...", "D": "..."},
        top_k=30
    )
"""

__version__ = "0.1.0"
__author__ = "Do Hai Nam"
__email__ = "dohainam@example.com"

# Export commonly used components
from src.config import get_settings

__all__ = [
    "get_settings",
    "__version__",
]
