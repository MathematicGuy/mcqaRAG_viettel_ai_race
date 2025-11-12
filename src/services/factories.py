"""
Factory functions for creating service instances.
Centralizes service creation with proper dependency injection.
"""

from functools import lru_cache

from src.config import get_settings
from src.services.chunking.text_chunker import SectionAwareChunker
from src.services.embeddings.sentence_transformer import EmbeddingsService
from src.services.llamacpp.client import OllamaClient
from src.services.llamacpp.llamacpp_client import OllamaCppClient
from src.services.opensearch.client import OpenSearchClient
from src.services.pdf_parser.docling_parser import DoclingPDFParser


@lru_cache()
def make_pdf_parser() -> DoclingPDFParser:
    """Create and cache PDF parser instance."""
    settings = get_settings()
    return DoclingPDFParser(settings.pdf_parser)


@lru_cache()
def make_text_chunker() -> SectionAwareChunker:
    """Create and cache text chunker instance."""
    settings = get_settings()
    return SectionAwareChunker(
        chunk_size=settings.chunking.chunk_size,
        overlap_size=settings.chunking.overlap_size,
        min_chunk_size=settings.chunking.min_chunk_size,
    )


@lru_cache()
def make_embeddings_service() -> EmbeddingsService:
    """Create and cache embeddings service instance."""
    settings = get_settings()
    return EmbeddingsService(
        model_name=settings.embeddings.model_name,
        device=settings.embeddings.device,
        batch_size=settings.embeddings.batch_size,
        max_length=settings.embeddings.max_length,
    )


@lru_cache()
def make_opensearch_client() -> OpenSearchClient:
    """Create and cache OpenSearch client instance."""
    settings = get_settings()
    return OpenSearchClient(
        host=settings.opensearch.host,
        index_name=settings.opensearch.index_name,
        username=settings.opensearch.username,
        password=settings.opensearch.password,
        use_ssl=settings.opensearch.use_ssl,
        verify_certs=settings.opensearch.verify_certs,
    )


@lru_cache()
def make_ollama_client() -> OllamaClient:
    """Create and cache Ollama client instance."""
    settings = get_settings()
    return OllamaClient(
        host=settings.ollama.host,
        model=settings.ollama.model,
        temperature=settings.ollama.temperature,
        max_response_words=settings.ollama.max_response_words,
        timeout=settings.ollama.timeout,
    )


# Export all factories
__all__ = [
    "make_pdf_parser",
    "make_text_chunker",
    "make_embeddings_service",
    "make_opensearch_client",
    "make_ollama_client",
]