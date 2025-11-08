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