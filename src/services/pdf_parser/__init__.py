"""
PDF Parser Service Module.
Handles PDF parsing using Docling with GROBID backend.
"""

from src.services.pdf_parser.docling_parser import DoclingPDFParser
from src.services.pdf_parser.factory import make_pdf_parser

__all__ = [
    "DoclingPDFParser",
    "make_pdf_parser",
]
