"""
Factory for creating PDF parser instances.
"""

from functools import lru_cache

from src.config import get_settings
from src.services.pdf_parser.docling_parser import DoclingPDFParser


@lru_cache()
def make_pdf_parser() -> DoclingPDFParser:
    """
    Create and cache PDF parser instance.

    Returns:
        DoclingPDFParser: Configured PDF parser
    """
    settings = get_settings()
    return DoclingPDFParser(settings.pdf_parser)
