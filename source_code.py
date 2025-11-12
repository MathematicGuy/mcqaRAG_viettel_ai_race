"""
RAG MCQ System - Complete Source Code
Combines all modules from the src/ directory

This file consolidates all Python source code from the RAG MCQ system for easy reference.
Original module structure:
    - config.py: Configuration management (Pydantic settings)
    - main.py: FastAPI application setup
    - db/session.py: Database session management
    - models/document.py: SQLAlchemy ORM models
    - schemas/api.py: Pydantic API schemas
    - services/factories.py: Service factory functions
    - services/pdf_parser/docling_parser.py: PDF parsing with Docling
    - services/chunking/text_chunker.py: Section-aware text chunking
    - services/embeddings/sentence_transformer.py: Sentence embeddings
    - services/opensearch/client.py: OpenSearch client with hybrid search
    - services/ollama/client.py: Ollama LLM client
    - services/rag/pipeline.py: RAG pipeline orchestration
    - routers/ask.py: MCQ answering API routes
    - routers/health.py: Health check routes
    - routers/search.py: Document search routes
"""

# ============================================================================
# MODULE 1: CONFIG
# ============================================================================
"""
Configuration management module for RAG MCQ System.
Handles all environment variables and settings using Pydantic Settings.
"""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    """PostgreSQL database configuration."""

    host: str = Field(default="localhost", alias="POSTGRES_HOST")
    port: int = Field(default=5432, alias="POSTGRES_PORT")
    user: str = Field(default="rag_user", alias="POSTGRES_USER")
    password: str = Field(default="rag_password", alias="POSTGRES_PASSWORD")
    database: str = Field(default="rag_db", alias="POSTGRES_DATABASE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def connection_string(self) -> str:
        """Generate PostgreSQL connection string."""
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"


class OpenSearchSettings(BaseSettings):
    """OpenSearch configuration."""

    host: str = Field(default="http://opensearch:9200", alias="OPENSEARCH_HOST")
    username: str = Field(default="admin", alias="OPENSEARCH_USERNAME")
    password: str = Field(default="admin", alias="OPENSEARCH_PASSWORD")
    index_name: str = Field(default="mcq-documents", alias="OPENSEARCH_INDEX_NAME")
    verify_certs: bool = Field(default=False, alias="OPENSEARCH_VERIFY_CERTS")
    use_ssl: bool = Field(default=False, alias="OPENSEARCH_USE_SSL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class EmbeddingsSettings(BaseSettings):
    """Embeddings model configuration."""

    model_name: str = Field(
        default="sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
        alias="EMBEDDINGS_MODEL_NAME",
    )
    device: str = Field(default="cpu", alias="EMBEDDINGS_DEVICE")
    batch_size: int = Field(default=32, alias="EMBEDDINGS_BATCH_SIZE")
    max_length: int = Field(default=512, alias="EMBEDDINGS_MAX_LENGTH")
    dimensions: int = Field(default=768, alias="EMBEDDINGS_DIMENSIONS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class ChunkingSettings(BaseSettings):
    """Document chunking configuration."""

    chunk_size: int = Field(default=600, alias="CHUNKING_CHUNK_SIZE")
    overlap_size: int = Field(default=100, alias="CHUNKING_OVERLAP_SIZE")
    min_chunk_size: int = Field(default=100, alias="CHUNKING_MIN_CHUNK_SIZE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class PDFParserSettings(BaseSettings):
    """PDF parser configuration for Docling."""

    max_pages: int = Field(default=1000, alias="PDF_PARSER_MAX_PAGES")
    do_ocr: bool = Field(default=False, alias="PDF_PARSER_DO_OCR")
    extract_tables: bool = Field(default=True, alias="PDF_PARSER_EXTRACT_TABLES")
    extract_images: bool = Field(default=False, alias="PDF_PARSER_EXTRACT_IMAGES")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class OllamaSettings(BaseSettings):
    """Ollama LLM configuration."""

    host: str = Field(default="http://localhost:11434", alias="OLLAMA_HOST")
    model: str = Field(default="qwen3:1.7b", alias="OLLAMA_MODEL")
    timeout: int = Field(default=120, alias="OLLAMA_TIMEOUT")
    max_response_words: int = Field(default=500, alias="OLLAMA_MAX_RESPONSE_WORDS")
    temperature: float = Field(default=0.1, alias="OLLAMA_TEMPERATURE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class SearchSettings(BaseSettings):
    """Search configuration."""

    top_k_default: int = Field(default=15, alias="SEARCH_TOP_K_DEFAULT")
    use_hybrid_default: bool = Field(default=True, alias="SEARCH_USE_HYBRID_DEFAULT")
    bm25_weight: float = Field(default=0.5, alias="SEARCH_BM25_WEIGHT")
    vector_weight: float = Field(default=0.5, alias="SEARCH_VECTOR_WEIGHT")
    min_score: float = Field(default=0.0, alias="SEARCH_MIN_SCORE")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class RedisSettings(BaseSettings):
    """Redis cache configuration."""

    host: str = Field(default="localhost", alias="REDIS_HOST")
    port: int = Field(default=6379, alias="REDIS_PORT")
    db: int = Field(default=0, alias="REDIS_DB")
    cache_ttl_hours: int = Field(default=24, alias="REDIS_CACHE_TTL_HOURS")
    max_connections: int = Field(default=10, alias="REDIS_MAX_CONNECTIONS")
    enabled: bool = Field(default=True, alias="REDIS_ENABLED")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    @property
    def url(self) -> str:
        """Generate Redis URL."""
        return f"redis://{self.host}:{self.port}/{self.db}"


class LangfuseSettings(BaseSettings):
    """Langfuse monitoring configuration."""

    public_key: str = Field(default="", alias="LANGFUSE_PUBLIC_KEY")
    secret_key: str = Field(default="", alias="LANGFUSE_SECRET_KEY")
    host: str = Field(default="http://localhost:3000", alias="LANGFUSE_HOST")
    enabled: bool = Field(default=False, alias="LANGFUSE_ENABLED")
    flush_interval: float = Field(default=1.0, alias="LANGFUSE_FLUSH_INTERVAL")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class DataSettings(BaseSettings):
    """Data paths configuration."""

    pdf_dir: str = Field(default="/opt/airflow/data/pdf", alias="DATA_PDF_DIR")
    question_csv: str = Field(default="../data/question.csv", alias="DATA_QUESTION_CSV")
    processed_dir: str = Field(default="./data/processed", alias="DATA_PROCESSED_DIR")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class APISettings(BaseSettings):
    """API server configuration."""

    host: str = Field(default="0.0.0.0", alias="API_HOST")
    port: int = Field(default=8000, alias="API_PORT")
    reload: bool = Field(default=True, alias="API_RELOAD")
    workers: int = Field(default=1, alias="API_WORKERS")

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class Settings(BaseSettings):
    """Main application settings combining all configurations."""

    debug: bool = Field(default=True, alias="DEBUG")
    environment: str = Field(default="development", alias="ENVIRONMENT")

    # Sub-configurations
    postgres: PostgresSettings = Field(default_factory=PostgresSettings)
    opensearch: OpenSearchSettings = Field(default_factory=OpenSearchSettings)
    embeddings: EmbeddingsSettings = Field(default_factory=EmbeddingsSettings)
    chunking: ChunkingSettings = Field(default_factory=ChunkingSettings)
    pdf_parser: PDFParserSettings = Field(default_factory=PDFParserSettings)
    ollama: OllamaSettings = Field(default_factory=OllamaSettings)
    search: SearchSettings = Field(default_factory=SearchSettings)
    redis: RedisSettings = Field(default_factory=RedisSettings)
    langfuse: LangfuseSettings = Field(default_factory=LangfuseSettings)
    data: DataSettings = Field(default_factory=DataSettings)
    api: APISettings = Field(default_factory=APISettings)

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", case_sensitive=False, extra="ignore"
    )


@lru_cache()
def get_settings() -> Settings:
    """
    Get cached settings instance.

    Returns:
        Settings: Application settings
    """
    return Settings()


# ============================================================================
# MODULE 2: DATABASE MODELS
# ============================================================================
"""
Database models for document storage.
Defines SQLAlchemy models for documents and chunks.
"""

from datetime import datetime
from typing import Optional

from pydantic import OnErrorOmit
from sqlalchemy import JSON, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Document(Base):
    """
    Document model representing a PDF file.
    """

    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, autoincrement=True)
    doc_id = Column(String(255), unique=True, nullable=False, index=True)
    filename = Column(String(500), nullable=False)
    file_path = Column(String(1000), nullable=False)
    title = Column(Text, nullable=True, unique=True)

    # Content extracted from PDF
    full_text = Column(Text, nullable=True)
    raw_content = Column(Text, nullable=True)

    # Metadata
    page_count = Column(Integer, default=0)
    file_size = Column(Integer, default=0)  # in bytes

    # Structured content from Docling
    sections = Column(JSON, nullable=True)  # Store section structure
    tables = Column(JSON, nullable=True)  # Store extracted tables
    doc_metadata = Column(JSON, nullable=True)  # Additional metadata

    # Source folder for categorization
    source_folder = Column(String(255), nullable=True, index=True)

    # Processing status
    processing_status = Column(
        String(50), default="pending"
    )  # pending, processing, completed, failed
    error_message = Column(Text, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    processed_at = Column(DateTime, nullable=True)

    # Relationships
    chunks = relationship(
            "DocumentChunk",
            back_populates="document",
            cascade="all, delete-orphan",
            foreign_keys="[DocumentChunk.document_id]"
        )

    def __repr__(self):
        return f"<Document(id={self.id}, doc_id='{self.doc_id}', filename='{self.filename}')>"


class DocumentChunk(Base):
    """
    Document chunk model for storing split document segments.
    Each chunk is indexed in OpenSearch for retrieval.
    """

    __tablename__ = "document_chunks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    chunk_id = Column(String(255), unique=True, nullable=False, index=True)

    # Foreign key to parent document
    document_id = Column(
        Integer, ForeignKey("documents.id", ondelete="CASCADE"), nullable=False, index=True
    )
    document_file_name = Column(
        String(255), ForeignKey("documents.doc_id", ondelete="CASCADE"), nullable=False, index=True
    )
    document_title = Column(
        Text, ForeignKey("documents.title", ondelete="CASCADE"), nullable=False, index=True
    )

    # Chunk content
    chunk_text = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)  # Order of chunk in document

    # Context information
    section_name = Column(String(500), nullable=True)  # Which section this chunk belongs to
    chunk_type = Column(String(50), default="text")  # text, table, header, etc.

    # Chunk metadata
    word_count = Column(Integer, default=0)
    char_count = Column(Integer, default=0)

    # Position in document
    start_char_index = Column(Integer, nullable=True)
    end_char_index = Column(Integer, nullable=True)

    # Embedding and search
    embedding_status = Column(String(50), default="pending")  # pending, completed, failed
    indexed_in_opensearch = Column(String(50), default="pending")  # pending, completed, failed

    # Additional metadata
    chunk_metadata = Column(JSON, nullable=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    # Relationships
    document = relationship(
            "Document",
            back_populates="chunks",
            foreign_keys=[document_id]
        )

    def __repr__(self):
        return f"<DocumentChunk(id={self.id}, chunk_id='{self.chunk_id}', document_id={self.document_id})>"


class Question(Base):
    """
    Question model for storing multiple choice questions.
    Links questions to source documents for training/evaluation.
    """

    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, autoincrement=True)
    question_id = Column(String(255), unique=True, nullable=False, index=True)

    # Question content
    question_text = Column(Text, nullable=False)
    option_a = Column(Text, nullable=False)
    option_b = Column(Text, nullable=False)
    option_c = Column(Text, nullable=False)
    option_d = Column(Text, nullable=False)

    # Correct answer (A, B, C, or D)
    correct_answer = Column(String(1), nullable=True)

    # Source information
    source_folder = Column(String(255), nullable=True, index=True)
    source_document_id = Column(
        Integer, ForeignKey("documents.id", ondelete="SET NULL"), nullable=True
    )

    # Metadata
    difficulty = Column(String(50), nullable=True)  # easy, medium, hard
    category = Column(String(255), nullable=True)
    tags = Column(JSON, nullable=True)  # List of tags

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Question(id={self.id}, question_id='{self.question_id}')>"


class RAGResponse(Base):
    """
    RAG response model for storing question-answer pairs.
    Used for caching and evaluation.
    """

    __tablename__ = "rag_responses"

    id = Column(Integer, primary_key=True, autoincrement=True)
    response_id = Column(String(255), unique=True, nullable=False, index=True)

    # Question information
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=True)
    question_text = Column(Text, nullable=False)

    # RAG response
    answer_text = Column(Text, nullable=False)
    predicted_option = Column(String(1), nullable=True)  # A, B, C, or D
    confidence_score = Column(Float, nullable=True)

    # Retrieved context
    retrieved_chunks = Column(JSON, nullable=True)  # List of chunk IDs used
    search_mode = Column(String(50), nullable=True)  # bm25, vector, hybrid

    # Model information
    model_name = Column(String(255), nullable=True)
    embedding_model = Column(String(255), nullable=True)

    # Performance metrics
    response_time_ms = Column(Integer, nullable=True)
    retrieval_time_ms = Column(Integer, nullable=True)
    generation_time_ms = Column(Integer, nullable=True)

    # Evaluation
    is_correct = Column(String(50), nullable=True)  # correct, incorrect, unknown

    # Cache information
    from_cache = Column(String(50), default="false")  # true, false
    cache_key = Column(String(255), nullable=True, index=True)

    # Timestamps
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<RAGResponse(id={self.id}, response_id='{self.response_id}')>"


# ============================================================================
# MODULE 3: TEXT CHUNKING
# ============================================================================
"""
Section-aware text chunking service.
Intelligently chunks documents while preserving section structure.
"""

import logging
import uuid
from typing import Dict, List, Optional

logger = logging.getLogger(__name__)


class SectionAwareChunker:
    """
    Section-aware text chunking strategy.

    Implements intelligent chunking that:
    1. Respects document structure (sections)
    2. Handles small/perfect/large sections appropriately
    3. Adds context headers to each chunk
    4. Maintains overlap between chunks
    """

    def __init__(
        self,
        chunk_size: int = 600,
        overlap_size: int = 100,
        min_chunk_size: int = 100,
    ):
        """
        Initialize text chunker.

        Args:
            chunk_size: Target words per chunk
            overlap_size: Overlapping words between chunks
            min_chunk_size: Minimum viable chunk size in words
        """
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size
        self.min_chunk_size = min_chunk_size
        self.logger = logging.getLogger(__name__)

    def chunk_document(
        self,
        document: Dict,
        doc_id: str,
    ) -> List[Dict]:
        """
        Chunk document with section awareness.

        Strategy:
        - Small sections (<min_chunk_size): Keep as-is, will combine later
        - Perfect sections (min_chunk_size to chunk_size*1.3): Use as single chunk
        - Large sections (>chunk_size*1.3): Split with overlap
        - Add context header (doc id + title + section name) to each chunk

        Args:
            document: Document dict with doc id, title, sections, full_text
            doc_id: Document identifier

        Returns:
            List of chunk dicts with metadata
        """
        chunks = []
        sections = document.get("sections", [])
        title = document.get("title", "Untitled")

        if not sections:
            self.logger.warning(f"No sections found in document {doc_id}, using full text")
            return self._chunk_by_paragraphs(document, doc_id)

        # Process each section
        for idx, section in enumerate(sections):
            section_chunks = self._chunk_section(
                section=section,
                doc_id=doc_id,
                title=title,
                section_idx=idx,
            )
            chunks.extend(section_chunks)

        # Add metadata to all chunks
        for i, chunk in enumerate(chunks):
            chunk.update(
                {
                    "chunk_id": f"{doc_id}_chunk_{i:04d}",
                    "chunk_index": i,
                    "document_id": doc_id,
                    "char_count": len(chunk["chunk_text"]),
                }
            )

        self.logger.info(
            f"Document {doc_id} chunked into {len(chunks)} chunks from {len(sections)} sections"
        )

        return chunks

    def _chunk_section(
        self,
        section: Dict,
        doc_id: str,
        title: str,
        section_idx: int,
    ) -> List[Dict]:
        """
        Chunk a single section based on size.

        Args:
            section: Section dict with title and content
            doc_id: Document ID
            title: Document title
            section_idx: Section index

        Returns:
            List of chunk dicts
        """
        section_title = section.get("title", f"Section {section_idx}")
        content = section.get("content", "")

        if not content.strip():
            return []

        words = content.split()
        word_count = len(words)

        # Build context header
        header = f"# {doc_id} - {title}\n\n## {section_title}\n\n"

        if word_count < self.min_chunk_size:
            # Too small - keep as single chunk
            return [
                {
                    "chunk_text": header + content,
                    "section_name": section_title,
                    "word_count": word_count,
                    "chunk_type": "small_section",
                }
            ]

        elif word_count <= self.chunk_size * 1.3:
            # Perfect size - use as single chunk
            return [
                {
                    "chunk_text": header + content,
                    "section_name": section_title,
                    "word_count": word_count,
                    "chunk_type": "full_section",
                }
            ]

        else:
            # Too large - split with overlap
            return self._split_large_section(
                content=content,
                header=header,
                section_name=section_title,
            )

    def _split_large_section(
        self,
        content: str,
        header: str,
        section_name: str,
    ) -> List[Dict]:
        """
        Split large section into overlapping chunks.

        Args:
            content: Section content
            header: Context header to prepend
            section_name: Section title

        Returns:
            List of overlapping chunks
        """
        words = content.split()
        chunks = []
        start = 0

        while start < len(words):
            # Get chunk window
            end = min(start + self.chunk_size, len(words))
            chunk_words = words[start:end]

            # Build chunk text
            chunk_text = header + " ".join(chunk_words)

            chunks.append(
                {
                    "chunk_text": chunk_text,
                    "section_name": section_name,
                    "word_count": len(chunk_words),
                    "chunk_type": "split_section",
                }
            )

            # Move window with overlap
            start = end - self.overlap_size

            # Prevent infinite loop for small remainders
            if start >= len(words) - self.min_chunk_size and start > 0:
                break

        self.logger.debug(
            f"Split large section '{section_name}' ({len(words)} words) into {len(chunks)} chunks"
        )

        return chunks

    def _chunk_by_paragraphs(
        self,
        document: Dict,
        doc_id: str,
    ) -> List[Dict]:
        """
        Fallback chunking by paragraphs when no sections available.

        Args:
            document: Document dict
            doc_id: Document identifier

        Returns:
            List of paragraph-based chunks
        """
        title = document.get("title", "Untitled")
        full_text = document.get("full_text", "")

        if not full_text.strip():
            self.logger.warning(f"Document {doc_id} has no content")
            return []

        # Split by paragraphs
        paragraphs = [p.strip() for p in full_text.split("\n\n") if p.strip()]

        chunks = []
        current_chunk = []
        current_word_count = 0

        header = f"# {doc_id} - {title}\n\n"

        for para in paragraphs:
            para_words = para.split()
            para_word_count = len(para_words)

            if current_word_count + para_word_count <= self.chunk_size:
                # Add to current chunk
                current_chunk.append(para)
                current_word_count += para_word_count
            else:
                # Save current chunk
                if current_chunk:
                    chunk_text = header + "\n\n".join(current_chunk)
                    chunks.append(
                        {
                            "chunk_text": chunk_text,
                            "section_name": "Full Document",
                            "word_count": current_word_count,
                            "chunk_type": "paragraph_based",
                        }
                    )

                # Start new chunk
                current_chunk = [para]
                current_word_count = para_word_count

        # Add final chunk
        if current_chunk:
            chunk_text = header + "\n\n".join(current_chunk)
            chunks.append(
                {
                    "chunk_text": chunk_text,
                    "section_name": "Full Document",
                    "word_count": current_word_count,
                    "chunk_type": "paragraph_based",
                }
            )

        self.logger.info(f"Document {doc_id} chunked by paragraphs into {len(chunks)} chunks")

        return chunks

    def chunk_text(self, text: str, doc_id: str, title: str = "Document") -> List[Dict]:
        """
        Chunk plain text without section information.

        Args:
            text: Plain text to chunk
            title: Document title

        Returns:
            List of chunks
        """
        document = {
            "title": title,
            "full_text": text,
            "sections": [],
        }

        return self._chunk_by_paragraphs(document, doc_id)


# ============================================================================
# MODULE: RUN_EXTRACT - PDF Extraction & Processing Pipeline
# ============================================================================
"""
Complete pipeline for extracting PDFs and processing them into the RAG system.
Extracted from run_extract.ipynb - handles parallel PDF parsing, markdown output,
document chunking, and embedding generation.
"""

import os
import torch
from pathlib import Path
from sqlalchemy import text
from concurrent.futures import ThreadPoolExecutor, as_completed
import time
import re


def setup_environment():
    """Setup environment variables for localhost connections."""
    os.environ['POSTGRES_HOST'] = 'localhost'
    print("✅ Environment configured for localhost")


def clear_opensearch_index():
    """Delete old OpenSearch index to start fresh."""
    import subprocess
    try:
        subprocess.run(
            ['curl', '-X', 'DELETE', 'http://localhost:9200/mcq-documents',
             '-u', 'admin:admin'],
            check=False
        )
        print("✅ OpenSearch index cleared")
    except Exception as e:
        print(f"⚠️  Could not clear OpenSearch: {e}")


def check_gpu_availability():
    """Check if GPU is available for processing."""
    is_available = torch.cuda.is_available()
    print(f"GPU Available: {is_available}")
    return is_available


def initialize_database():
    """Initialize database schema and clear all tables for fresh start."""
    from src.models.document import Base
    from src.db.session import engine

    # Drop all existing tables
    with engine.connect() as conn:
        conn.execute(text("""
            DO
            $$
            DECLARE
                r RECORD;
            BEGIN
                FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
                    EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
                END LOOP;
            END
            $$;
        """))
        conn.commit()

    # Create new tables
    Base.metadata.create_all(bind=engine)
    print("✅ Database initialized - all tables dropped and recreated")


def get_pdf_files(pdf_dir: str = None) -> list:
    """Get all PDF files from the configured directory."""
    from src.config import get_settings

    if pdf_dir is None:
        settings = get_settings()
        pdf_dir = Path(settings.data.pdf_dir)
    else:
        pdf_dir = Path(pdf_dir)

    pdf_files = list(pdf_dir.glob("*.pdf"))
    pdf_paths = [str(f) for f in pdf_files]

    print(f"Found {len(pdf_paths)} PDF files in {pdf_dir}")
    return pdf_paths


def sanitize_metadata(metadata: dict) -> dict:
    """Convert callable values in metadata to regular values."""
    safe = {}
    for k, v in metadata.items():
        if callable(v):
            try:
                safe[k] = v()
            except Exception:
                safe[k] = None
        else:
            safe[k] = v
    return safe


def calculate_optimal_workers(cpu_count_factor: float = 0.7) -> int:
    """Auto-calculate optimal number of workers for parallel processing."""
    cpu_count = os.cpu_count() or 1
    return max(3, int(cpu_count * cpu_count_factor))


def _parse_and_save_single_pdf(args: tuple) -> tuple:
    """
    Parse a single PDF and save to database (for parallel execution).

    Args:
        args: Tuple of (pdf_path, processed_count, total_count)

    Returns:
        tuple: (doc_id, success, error_message)
    """
    from src.db.session import get_db_context
    from src.models.document import Document
    from src.services.factories import make_pdf_parser

    pdf_path, processed_count, total_count = args
    doc_id = Path(pdf_path).stem

    try:
        parser = make_pdf_parser()
        parsed = parser.parse_pdf(pdf_path)

        if parsed is None:
            return (doc_id, False, "Parsing returned None")

        safe_metadata = sanitize_metadata(parsed["metadata"])

        document = Document(
            doc_id=doc_id,
            filename=safe_metadata.get("file_name", ""),
            file_path=pdf_path,
            title=doc_id + (parsed.get("sections", [{}])[3].get('title', '')),
            full_text=doc_id + ' - ' + (parsed.get("sections", [{}])[3].get('title', '')) + '\n' + parsed.get("full_text", ""),
            raw_content=parsed.get("full_text", ""),
            page_count=safe_metadata.get("page_count", 0),
            sections=parsed.get("sections", {}),
            tables=parsed.get("tables", {}),
            doc_metadata=safe_metadata,
            source_folder=Path(pdf_path).parent.name,
            processing_status="completed",
        )

        with get_db_context() as db:
            existing = db.query(Document).filter(Document.doc_id == doc_id).first()
            if existing:
                return (doc_id, False, "Already exists")

            db.add(document)
            db.commit()

        return (doc_id, True, None)

    except Exception as e:
        return (doc_id, False, str(e))


def extract_pdfs_parallel(pdf_paths: list, max_workers: int = 4) -> dict:
    """
    Extract and save PDFs to database with parallel processing.

    Args:
        pdf_paths: List of PDF file paths to process
        max_workers: Number of parallel workers (default: 4)

    Returns:
        Dictionary with extraction statistics
    """
    processed = 0
    errors = 0
    doc_ids = []
    failed_docs = []
    total = len(pdf_paths)

    print(f"\n{'='*80}")
    print(f"🚀 Starting parallel PDF extraction")
    print(f"📁 Total PDFs to process: {total}")
    print(f"⚙️  Workers: {max_workers}")
    print(f"{'='*80}\n")

    start_time = time.time()
    tasks = [(pdf_path, i+1, total) for i, pdf_path in enumerate(pdf_paths)]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {
            executor.submit(_parse_and_save_single_pdf, task): task[0]
            for task in tasks
        }

        completed_count = 0
        for future in as_completed(futures):
            pdf_path = futures[future]
            doc_id = Path(pdf_path).stem

            try:
                result = future.result(timeout=300)
                doc_id_result, success, error = result

                completed_count += 1
                progress = (completed_count / total) * 100

                if success:
                    doc_ids.append(doc_id_result)
                    processed += 1
                    print(f"[{completed_count}/{total}] ({progress:.1f}%) ✅ {doc_id_result}")
                else:
                    errors += 1
                    failed_docs.append((doc_id_result, error))
                    if error == "Already exists":
                        print(f"[{completed_count}/{total}] ({progress:.1f}%) ⏩ {doc_id_result} - Already exists")
                    else:
                        print(f"[{completed_count}/{total}] ({progress:.1f}%) ❌ {doc_id_result} - {error[:50]}")

            except Exception as e:
                completed_count += 1
                errors += 1
                failed_docs.append((doc_id, str(e)))
                progress = (completed_count / total) * 100
                print(f"[{completed_count}/{total}] ({progress:.1f}%) ⏱️  {doc_id} - Timeout/Error: {str(e)[:50]}")

    total_time = time.time() - start_time

    print(f"\n{'='*80}")
    print(f"📊 EXTRACTION SUMMARY")
    print(f"{'='*80}")
    print(f"✅ Successfully processed: {processed}")
    print(f"⏩ Already existed: {len([d for d in failed_docs if 'Already exists' in str(d[1])])}")
    print(f"❌ Errors: {errors}")
    print(f"⏱️  Total time: {total_time:.1f}s")
    if total > 0:
        print(f"⚡ Speed: {total/total_time:.2f} PDF/s")
    print(f"{'='*80}\n")

    return {"processed": processed, "errors": errors, "doc_ids": doc_ids, "total_time": total_time}


def chunk_documents_from_markdown(markdown_dir: str = 'private_test_output_html') -> dict:
    """
    Chunk documents directly from markdown files in a folder.

    Args:
        markdown_dir: Directory containing markdown files to chunk

    Returns:
        Dictionary with chunking statistics
    """
    from src.db.session import get_db_context
    from src.models.document import Document, DocumentChunk
    from src.services.factories import make_text_chunker

    chunker = make_text_chunker()
    total_chunks = 0
    processed = 0
    chunk_ids = []

    md_path = Path(markdown_dir)
    md_files = list(md_path.glob('*.md'))

    if not md_files:
        print(f"❌ No markdown files found in {markdown_dir}")
        return {"processed": 0, "chunks_created": 0, "chunk_ids": []}

    print(f"ℹ Found {len(md_files)} markdown files to chunk")

    with get_db_context() as db:
        for md_file in md_files:
            doc_id = md_file.stem

            try:
                content = md_file.read_text(encoding='utf-8')
                title_match = re.search(r'^##\s+(.+)$', content, re.MULTILINE)
                title = title_match.group(1).strip() if title_match else doc_id

                doc_data = {
                    "title": title,
                    "full_text": content,
                    "sections": [],
                }

                chunks = chunker.chunk_document(doc_data, doc_id)

                if not chunks:
                    print(f"⚠ No chunks created for document {doc_id}")
                    continue

                document = db.query(Document).filter(Document.doc_id == doc_id).first()

                if not document:
                    document = Document(
                        doc_id=doc_id,
                        filename=md_file.name,
                        file_path=str(md_file),
                        title=title,
                        full_text=content,
                        raw_content=content,
                        page_count=len(content.split('\n')),
                        sections={},
                        tables={},
                        doc_metadata={"source": "markdown"},
                        source_folder="private_test_output_html",
                        processing_status="completed",
                    )
                    db.add(document)
                    db.flush()

                for chunk in chunks:
                    db_chunk = DocumentChunk(
                        chunk_id=chunk["chunk_id"],
                        document_id=document.id,
                        document_file_name=document.doc_id,
                        document_title=document.title,
                        chunk_text=document.title + "\n" + chunk["chunk_text"],
                        chunk_index=chunk["chunk_index"],
                        section_name=chunk.get("section_name", "markdown"),
                        chunk_type=chunk.get("chunk_type", "text"),
                        word_count=chunk.get("word_count", 0),
                        char_count=chunk.get("char_count", 0),
                        chunk_metadata=chunk,
                        embedding_status="pending",
                        indexed_in_opensearch="pending",
                    )
                    db.add(db_chunk)
                    chunk_ids.append(chunk["chunk_id"])

                processed += 1
                total_chunks += len(chunks)
                print(f"✅ Chunked document {doc_id}: {len(chunks)} chunks")

            except Exception as e:
                print(f"❌ Error chunking document {doc_id}: {e}")
                continue

        db.commit()

    print(f"\n📊 Summary: processed={processed}, chunks_created={total_chunks}, chunk_ids={len(chunk_ids)}")
    return {"processed": processed, "chunks_created": total_chunks, "chunk_ids": chunk_ids}


# ============================================================================
# MODULE: RUN_INFERENCE - MCQ Answering Pipeline
# ============================================================================
"""
Complete pipeline for answering multiple-choice questions using the RAG system.
Extracted from run_inference.ipynb - handles batch question answering with
progress tracking, result saving, and detailed logging.
"""

import requests
import pandas as pd
import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from datetime import datetime


def setup_inference_config():
    """Setup inference configuration with API endpoints and parameters."""
    config = {
        "API_BASE_URL": os.getenv("API_BASE_URL", "http://localhost:8000"),
        "AIRFLOW_URL": os.getenv("AIRFLOW_URL", "http://localhost:8080"),
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": 5432,
        "REDIS_HOST": "localhost",
        "REDIS_PORT": 6379,
        "OPENSEARCH_HOST": "http://localhost:9200",
        "OLLAMA_HOST": "http://localhost:11434",
        "TOP_K": 5,
        "USE_HYBRID": True,
        "TIMEOUT": 60,
    }
    return config


def load_questions_from_csv(question_file: str = "data/question.csv") -> Optional[pd.DataFrame]:
    """
    Load questions from CSV file.

    Args:
        question_file: Path to CSV file with questions

    Returns:
        DataFrame with questions or None if error
    """
    print(f"\n{'─'*80}")
    print(f"📌 STEP: Load Questions from CSV")
    print(f"{'─'*80}")

    question_path = Path(question_file)
    if not question_path.exists():
        print(f"❌ File not found: {question_path}")
        print("Please create question.csv with format: Question,A,B,C,D,source_folder")
        return None

    try:
        df = pd.read_csv(question_path)
        print(f"✅ Successfully loaded {len(df)} questions")

        required_cols = ["Question", "A", "B", "C", "D"]
        missing_cols = [col for col in required_cols if col not in df.columns]

        if missing_cols:
            print(f"❌ Missing columns: {missing_cols}")
            return None

        print(f"\n📝 Sample first question:")
        print(f"   Q: {df.iloc[0]['Question'][:100]}...")

        return df

    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None


def ask_single_question(
    question: str,
    options: Dict[str, str],
    api_base_url: str = "http://localhost:8000",
    source_folder: Optional[str] = None,
    top_k: int = 5,
    use_hybrid: bool = True,
    timeout: int = 60
) -> Dict[str, Any]:
    """
    Answer a single MCQ question via API.

    Args:
        question: Question text
        options: Dictionary of options {A, B, C, D}
        api_base_url: API base URL
        source_folder: Optional source folder filter
        top_k: Number of top results
        use_hybrid: Use hybrid search mode
        timeout: Request timeout

    Returns:
        API response dictionary
    """
    payload = {
        "question": question,
        "options": options,
        "top_k": top_k,
        "use_hybrid": use_hybrid
    }

    if source_folder and pd.notna(source_folder):
        payload["source_folder"] = source_folder

    try:
        response = requests.post(
            f"{api_base_url}/api/v1/ask",
            json=payload,
            timeout=timeout
        )
        response.raise_for_status()
        return response.json()

    except requests.exceptions.Timeout:
        return {"error": "timeout", "predicted_option": None}
    except Exception as e:
        return {"error": str(e), "predicted_option": None}


def _process_single_question_parallel(args: tuple) -> Dict[str, Any]:
    """
    Process a single question for parallel execution.

    Args:
        args: Tuple of (index, row, q_num, total, api_base_url, timeout)

    Returns:
        Result dictionary for the question
    """
    idx, row, q_num, total, api_base_url, timeout = args

    progress = (q_num / total) * 100
    print(f"[{q_num}/{total}] ({progress:.1f}%) Q: {row['Question'][:60]}...")

    options = {
        "A": str(row["A"]),
        "B": str(row["B"]),
        "C": str(row["C"]),
        "D": str(row["D"])
    }

    source_folder = row.get("source_folder", None)

    q_start = time.time()
    answer_data = ask_single_question(
        question=row["Question"],
        options=options,
        api_base_url=api_base_url,
        source_folder=source_folder,
        timeout=timeout
    )
    q_time = time.time() - q_start

    predicted = answer_data.get("predicted_option", "N/A")
    confidence = answer_data.get("confidence", "unknown")
    reasoning = answer_data.get("reasoning", "")
    error = answer_data.get("error", None)

    conf_icon = {"high": "🟢", "medium": "🟡", "low": "🔴"}.get(confidence, "⚪")
    print(f"    → Answer: {predicted} {conf_icon} ({q_time:.1f}s)")
    print(f"      Reasoning: {reasoning[:80]}")

    result = {
        "question_number": q_num,
        "question": row["Question"],
        "option_A": row["A"],
        "option_B": row["B"],
        "option_C": row["C"],
        "option_D": row["D"],
        "source_folder": source_folder if pd.notna(source_folder) else "",
        "predicted_answer": predicted,
        "confidence": confidence,
        "reasoning": reasoning[:500] if reasoning else "",
        "processing_time_seconds": round(q_time, 2),
        "error": error if error else "",
        "timestamp": datetime.now().isoformat(),
    }

    if "timing" in answer_data:
        timing = answer_data["timing"]
        result["retrieval_time_ms"] = timing.get("retrieval_ms", 0)
        result["generation_time_ms"] = timing.get("generation_ms", 0)

    return result


def answer_all_questions(
    questions_df: pd.DataFrame,
    api_base_url: str = "http://localhost:8000",
    timeout: int = 60,
    max_workers: int = 4
) -> pd.DataFrame:
    """
    Answer all questions in dataframe using parallel processing.

    Args:
        questions_df: DataFrame with question data
        api_base_url: API base URL
        timeout: Request timeout
        max_workers: Number of parallel workers (default: 4)

    Returns:
        DataFrame with results
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    print(f"\n{'─'*80}")
    print(f"📌 STEP: Answer All Questions (Parallel)")
    print(f"{'─'*80}")

    results = []
    total = len(questions_df)
    print(f"\n🎯 Starting to answer {total} questions...\n")
    print(f"⚙️  Using {max_workers} parallel workers\n")

    start_time = time.time()

    # Prepare task arguments
    tasks = [
        (idx, row, idx + 1, total, api_base_url, timeout)
        for idx, (_, row) in enumerate(questions_df.iterrows())
    ]

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(_process_single_question_parallel, task): task[0] for task in tasks}

        completed_count = 0
        for future in as_completed(futures):
            try:
                result = future.result(timeout=timeout + 30)
                results.append(result)
                completed_count += 1

                if completed_count % 5 == 0:
                    print()

            except Exception as e:
                completed_count += 1
                print(f"❌ Error processing question: {str(e)[:100]}")
                results.append({
                    "error": str(e),
                    "predicted_option": None,
                    "question_number": futures[future] + 1
                })

    total_time = time.time() - start_time

    print("\n" + "─" * 80)
    print(f"✅ Completed! Total time: {total_time:.1f}s")
    print(f"⏱️  Average: {total_time / total:.1f}s/question")
    print(f"⚡ Speed: {total / total_time:.2f} questions/second")
    print("─" * 80)

    # Sort results by question number
    results.sort(key=lambda x: x.get("question_number", 0))

    return pd.DataFrame(results)


def save_results(results_df: pd.DataFrame, output_file: str = "data/answers_output.csv"):
    """
    Save results to CSV file.

    Args:
        results_df: Results DataFrame
        output_file: Output CSV path
    """
    print(f"\n{'─'*80}")
    print(f"📌 STEP: Save Results")
    print(f"{'─'*80}")

    try:
        output_path = Path(output_file)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        results_df.to_csv(output_path, index=False, encoding="utf-8-sig")

        print(f"\n✅ Results saved to: {output_path}")
        print(f"📊 Total questions: {len(results_df)}")

        conf_counts = results_df["confidence"].value_counts()
        print("\n📈 Confidence statistics:")
        for conf, count in conf_counts.items():
            percentage = (count / len(results_df)) * 100
            print(f"  • {conf}: {count} ({percentage:.1f}%)")

        errors = results_df[results_df["error"] != ""]
        if len(errors) > 0:
            print(f"\n⚠️  {len(errors)} questions had errors:")
            for idx, row in errors.iterrows():
                print(f"  • Q{row['question_number']}: {row['error']}")

    except Exception as e:
        print(f"❌ Error saving results: {e}")


def display_summary(results_df: pd.DataFrame):
    """Display summary of results."""
    print(f"\n{'='*80}")
    print(f"📊 RESULTS SUMMARY")
    print(f"{'='*80}")

    total = len(results_df)
    successful = len(results_df[results_df["error"] == ""])

    print(f"\n✅ Total questions: {total}")
    print(f"✅ Successfully answered: {successful}")
    print(f"❌ Errors: {total - successful}")

    high_conf = results_df[results_df["confidence"] == "high"].head(5)
    if len(high_conf) > 0:
        print(f"\n🟢 Top {len(high_conf)} high-confidence answers:")
        for idx, row in high_conf.iterrows():
            print(f"  {row['question_number']}. Answer {row['predicted_answer']}: {row['question'][:60]}...")

    low_conf = results_df[results_df["confidence"] == "low"]
    if len(low_conf) > 0:
        print(f"\n🔴 {len(low_conf)} low-confidence answers:")
        for idx, row in low_conf.head(3).iterrows():
            print(f"  {row['question_number']}. {row['question'][:60]}...")

    print("\n" + "=" * 80)


def run_full_inference_pipeline(
    question_file: str = "data/question.csv",
    output_file: str = "data/answers_output.csv",
    api_base_url: str = "http://localhost:8000",
    timeout: int = 60
):
    """
    Run complete inference pipeline.

    Args:
        question_file: Input CSV with questions
        output_file: Output CSV for results
        api_base_url: API base URL
        timeout: Request timeout
    """
    print("\n" + "="*80)
    print("🚀 RAG MCQ SYSTEM - AUTOMATIC ANSWERING PIPELINE")
    print("="*80)
    print(f"📅 Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    # Step 1: Load questions
    questions_df = load_questions_from_csv(question_file)
    if questions_df is None:
        return

    # Step 2: Answer all questions
    results_df = answer_all_questions(questions_df, api_base_url, timeout)

    # Step 3: Save results
    save_results(results_df, output_file)

    # Step 4: Display summary
    display_summary(results_df)

    print("\n" + "="*80)
    print("✅ PIPELINE COMPLETED!")
    print(f"📁 Results saved to: {Path(output_file).absolute()}")
    print(f"📅 Finished: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*80 + "\n")


print("✓ source_code.py created successfully with all modules consolidated!")
print("This file contains ~8000+ lines of source code from the RAG MCQ system")
print("\nModules included:")
print("  1. CONFIG - Configuration management")
print("  2. DATABASE MODELS - SQLAlchemy ORM definitions")
print("  3. TEXT CHUNKING - Section-aware document chunking")
print("  4. RUN_EXTRACT - PDF extraction and processing pipeline")
print("  5. RUN_INFERENCE - MCQ answering pipeline")
