"""
Airflow DAG for PDF ingestion and indexing pipeline.
Automates the complete flow: PDF → Parse → Chunk → Embed → Index to OpenSearch.
"""

import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List
import asyncio

from airflow import DAG
from airflow.operators.python import PythonOperator

# Add src to path for imports
sys.path.insert(0, "/opt/airflow")

from src.config import get_settings
from src.db.session import get_db_context
from src.models.document import Document, DocumentChunk
from src.services.factories import (
    make_embeddings_service,
    make_opensearch_client,
    make_pdf_parser,
    make_text_chunker,
)

logger = logging.getLogger(__name__)
settings = get_settings()

# DAG default arguments
default_args = {
    "owner": "rag-system",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 2,
    "retry_delay": timedelta(minutes=5),
    "execution_timeout": timedelta(hours=2),
}

# Create DAG
dag = DAG(
    "pdf_ingestion_dag",
    default_args=default_args,
    description="Process PDFs and index into OpenSearch for RAG system",
    schedule_interval="@daily",  # Run daily
    start_date=datetime.now() - timedelta(days=1),
    catchup=False,
    tags=["rag", "pdf", "ingestion", "mcq"],
    max_active_runs=1,
)


def scan_pdf_files(**context) -> List[str]:
    """
    Scan PDF directory for new files.
    Returns list of PDF file paths.
    """
    pdf_dir = Path(settings.data.pdf_dir)

    if not pdf_dir.exists():
        logger.warning(f"PDF directory does not exist: {pdf_dir}")
        return []

    # Find all PDF files
    pdf_files = list(pdf_dir.glob("*.pdf"))
    pdf_paths = [str(f) for f in pdf_files]

    logger.info(f"Found {len(pdf_paths)} PDF files in {pdf_dir}")

    # Push to XCom for next task
    context["ti"].xcom_push(key="pdf_paths", value=pdf_paths)

    return pdf_paths


def extract_pdfs(**context) -> Dict:
    """
    Extract content from PDF files using Docling.
    Stores documents in PostgreSQL.
    """
    # Get PDF paths from previous task
    pdf_paths = context["ti"].xcom_pull(key="pdf_paths", task_ids="scan_files")

    if not pdf_paths:
        logger.warning("No PDF files to process")
        return {"processed": 0, "errors": 0}

    parser = make_pdf_parser()
    processed = 0
    errors = 0
    doc_ids = []

    with get_db_context() as db:
        for pdf_path in pdf_paths:
            try:
                logger.info(f"Processing PDF: {pdf_path}")

                # Generate doc_id
                doc_id = Path(pdf_path).stem

                # Check if already processed
                existing = db.query(Document).filter(Document.doc_id == doc_id).first()
                if existing:
                    logger.info(f"Document {doc_id} already exists, skipping")
                    continue

                # Parse PDF
                parsed = parser.parse_pdf(pdf_path)

                # Create document record
                document = Document(
                    doc_id=doc_id,
                    filename=parsed["metadata"]["file_name"],
                    file_path=pdf_path,
                    title=parsed["title"],
                    full_text=parsed["full_text"],
                    raw_content=parsed["full_text"],
                    page_count=parsed["metadata"]["page_count"],
                    sections=parsed["sections"],
                    tables=parsed["tables"],
                    doc_metadata=parsed["metadata"],
                    source_folder=Path(pdf_path).parent.name,
                    processing_status="completed",
                )

                db.add(document)
                db.commit()

                doc_ids.append(doc_id)
                processed += 1
                logger.info(f"Successfully processed: {doc_id}")

            except Exception as e:
                logger.error(f"Error processing {pdf_path}: {e}", exc_info=True)
                errors += 1
                continue

    # Push doc_ids to XCom
    context["ti"].xcom_push(key="doc_ids", value=doc_ids)

    result = {
        "processed": processed,
        "errors": errors,
        "doc_ids": doc_ids,
    }

    logger.info(f"PDF extraction complete: {result}")
    return result


def chunk_documents(**context) -> Dict:
    """
    Chunk documents using section-aware strategy.
    Stores chunks in PostgreSQL.
    """
    # Get doc_ids from previous task
    doc_ids = context["ti"].xcom_pull(key="doc_ids", task_ids="extract_pdfs")

    if not doc_ids:
        logger.warning("No documents to chunk")
        return {"processed": 0, "chunks_created": 0}

    chunker = make_text_chunker()
    total_chunks = 0
    processed = 0
    chunk_ids = []

    with get_db_context() as db:
        for doc_id in doc_ids:
            try:
                # Get document
                document = db.query(Document).filter(Document.doc_id == doc_id).first()
                if not document:
                    logger.warning(f"Document {doc_id} not found")
                    continue

                # Prepare document for chunking
                doc_data = {
                    "title": document.title,
                    "full_text": document.full_text,
                    "sections": document.sections or [],
                }

                # Chunk document
                chunks = chunker.chunk_document(doc_data, doc_id)

                # Store chunks
                for chunk in chunks:
                    db_chunk = DocumentChunk(
                        chunk_id=chunk["chunk_id"],
                        document_id=document.id,
                        chunk_text=chunk["chunk_text"],
                        chunk_index=chunk["chunk_index"],
                        section_name=chunk.get("section_name"),
                        chunk_type=chunk.get("chunk_type", "text"),
                        word_count=chunk.get("word_count", 0),
                        char_count=chunk.get("char_count", 0),
                        chunk_metadata=chunk,
                        embedding_status="pending",
                        indexed_in_opensearch="pending",
                    )
                    db.add(db_chunk)
                    chunk_ids.append(chunk["chunk_id"])

                db.commit()
                total_chunks += len(chunks)
                processed += 1

                logger.info(f"Chunked document {doc_id}: {len(chunks)} chunks")

            except Exception as e:
                logger.error(f"Error chunking document {doc_id}: {e}", exc_info=True)
                continue

    # Push chunk_ids to XCom
    context["ti"].xcom_push(key="chunk_ids", value=chunk_ids)

    result = {
        "processed": processed,
        "chunks_created": total_chunks,
        "chunk_ids": chunk_ids,
    }

    logger.info(f"Chunking complete: {result}")
    return result

def generate_embeddings(**context) -> Dict:
    """
    Generate embeddings for all chunks (synchronous for Airflow).
    """
    chunk_ids = context["ti"].xcom_pull(key="chunk_ids", task_ids="chunk_documents")
    if not chunk_ids:
        logger.warning("No chunks to embed")
        return {"processed": 0}

    embeddings_service = make_embeddings_service()
    processed = 0

    with get_db_context() as db:
        chunks = db.query(DocumentChunk).filter(DocumentChunk.chunk_id.in_(chunk_ids)).all()
        if not chunks:
            logger.warning("No chunks found in database")
            return {"processed": 0}

        texts = [chunk.chunk_text for chunk in chunks]

        try:
            logger.info(f"Generating embeddings for {len(texts)} chunks...")
            # Chạy async code trong sync context
            embeddings = asyncio.run(embeddings_service.embed_texts(texts))

            for chunk, embedding in zip(chunks, embeddings):
                chunk.embedding_status = "completed"
                chunk.chunk_metadata = chunk.chunk_metadata or {}
                chunk.chunk_metadata["embedding"] = embedding.tolist()

            db.commit()
            processed = len(chunks)
            logger.info(f"Generated {processed} embeddings")

        except Exception as e:
            logger.error(f"Error generating embeddings: {e}", exc_info=True)
            return {"processed": 0, "error": str(e)}

    return {"processed": processed}


def index_to_opensearch(**context) -> Dict:
    """
    Index chunks to OpenSearch (sync version).
    """
    chunk_ids = context["ti"].xcom_pull(key="chunk_ids", task_ids="chunk_documents")
    if not chunk_ids:
        logger.warning("No chunks to index")
        return {"indexed": 0}

    opensearch = make_opensearch_client()
    indexed = 0
    errors = 0

    # Chạy async code sync
    try:
        asyncio.run(opensearch.create_index(dimensions=settings.embeddings.dimensions))
    except Exception as e:
        logger.warning(f"Index may already exist: {e}")

    with get_db_context() as db:
        chunks = (
            db.query(DocumentChunk)
            .filter(DocumentChunk.chunk_id.in_(chunk_ids))
            .filter(DocumentChunk.embedding_status == "completed")
            .all()
        )

        if not chunks:
            logger.warning("No chunks with embeddings found")
            return {"indexed": 0}

        documents = []
        for chunk in chunks:
            documents.append({
                "chunk_id": chunk.chunk_id,
                "document_id": chunk.document.doc_id,
                "chunk_text": chunk.chunk_text,
                "section_name": chunk.section_name,
                "embedding": chunk.chunk_metadata.get("embedding", []),
                "word_count": chunk.word_count,
                "chunk_index": chunk.chunk_index,
                "chunk_type": chunk.chunk_type,
                "source_folder": chunk.document.source_folder,
                "created_at": chunk.created_at.isoformat() if chunk.created_at else None,
            })

        try:
            result = asyncio.run(opensearch.index_chunks_bulk(documents))
            indexed = result["success"]
            errors = result["errors"]

            for chunk in chunks:
                chunk.indexed_in_opensearch = "completed"

            db.commit()
            logger.info(f"Indexed {indexed} chunks, {errors} errors")

        except Exception as e:
            logger.error(f"Error indexing to OpenSearch: {e}", exc_info=True)
            return {"indexed": 0, "errors": len(documents), "error": str(e)}

    return {"indexed": indexed, "errors": errors}

# Define tasks
scan_task = PythonOperator(
    task_id="scan_files",
    python_callable=scan_pdf_files,
    dag=dag,
)

extract_task = PythonOperator(
    task_id="extract_pdfs",
    python_callable=extract_pdfs,
    dag=dag,
)

chunk_task = PythonOperator(
    task_id="chunk_documents",
    python_callable=chunk_documents,
    dag=dag,
)

embed_task = PythonOperator(
    task_id="generate_embeddings",
    python_callable=generate_embeddings,
    dag=dag,
)

index_task = PythonOperator(
    task_id="index_to_opensearch",
    python_callable=index_to_opensearch,
    dag=dag,
)

# Set task dependencies
scan_task >> extract_task >> chunk_task >> embed_task >> index_task