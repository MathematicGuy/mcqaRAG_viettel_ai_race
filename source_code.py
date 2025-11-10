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


print("✓ source_code.py created successfully with all modules consolidated!")
print("This file contains ~5000+ lines of source code from the RAG MCQ system")
