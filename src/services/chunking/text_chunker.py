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
        - Add context header (title + section name) to each chunk

        Args:
            document: Document dict with title, sections, full_text
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
        title: str,
        section_idx: int,
    ) -> List[Dict]:
        """
        Chunk a single section based on size.

        Args:
            section: Section dict with title and content
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
        header = f"# {title}\n\n## {section_title}\n\n"

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

        header = f"# {title}\n\n"

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

    def chunk_text(self, text: str, title: str = "Document") -> List[Dict]:
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

        return self._chunk_by_paragraphs(document, "temp_doc")
