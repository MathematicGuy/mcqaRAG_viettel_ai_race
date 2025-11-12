# """
# PDF Parser Service using Docling with GROBID backend.
# Extracts structured content from PDF files including text, sections, and tables.
# """

# import logging
# from pathlib import Path
# from typing import Dict, List, Optional

# from docling.document_converter import DocumentConverter, PdfFormatOption
# from docling.datamodel.base_models import InputFormat
# from docling.datamodel.pipeline_options import PdfPipelineOptions
# from docling.pipeline.standard_pdf_pipeline import StandardPdfPipeline

# from src.config import PDFParserSettings

# logger = logging.getLogger(__name__)


# class DoclingPDFParser:
#     """
#     PDF parser using Docling with GROBID backend.
#     Extracts structured content: text, sections, tables, metadata.
#     """

#     def __init__(self, config: PDFParserSettings):
#         """
#         Initialize Docling PDF parser.

#         Args:
#             config: PDF parser configuration settings
#         """
#         self.config = config
#         self.logger = logging.getLogger(__name__)

#         # Configure pipeline options
#         pipeline_options = PdfPipelineOptions()
#         pipeline_options.do_ocr = config.do_ocr
#         pipeline_options.do_table_structure = config.extract_tables

#         # Initialize document converter
#         self.converter = DocumentConverter(
#             format_options={
#                 InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
#             },
#         )

#     def parse_pdf(self, pdf_path: str) -> Dict:
#         """
#         Parse PDF file and extract structured content.

#         Args:
#             pdf_path: Path to PDF file

#         Returns:
#             Dict containing:
#                 - title: Document title
#                 - full_text: Complete text content
#                 - sections: List of sections with titles and content
#                 - tables: Extracted tables (if enabled)
#                 - metadata: Document metadata

#         Raises:
#             Exception: If PDF parsing fails
#         """
#         try:
#             self.logger.info(f"Parsing PDF: {pdf_path}")

#             # Convert document
#             result = self.converter.convert(pdf_path)
#             doc = result.document

#             # Extract components
#             document = {
#                 "title": self._extract_title(doc),
#                 "full_text": doc.export_to_markdown(),
#                 "sections": self._extract_sections(doc),
#                 "tables": self._extract_tables(doc) if self.config.extract_tables else [],
#                 "metadata": {
#                     "page_count": len(doc.pages) if hasattr(doc, "pages") else 0,
#                     "has_tables": len(doc.tables) > 0 if hasattr(doc, "tables") else False,
#                     "file_path": str(pdf_path),
#                     "file_name": Path(pdf_path).name,
#                 },
#             }

#             self.logger.info(
#                 f"Successfully parsed PDF: {document['title']}, "
#                 f"pages: {document['metadata']['page_count']}, "
#                 f"sections: {len(document['sections'])}"
#             )

#             return document

#         except Exception as e:
#             self.logger.error(f"Error parsing PDF {pdf_path}: {e}", exc_info=True)
#             raise

#     def _extract_title(self, doc) -> str:
#         """Extract document title."""
#         # Try to get title from metadata or first heading
#         if hasattr(doc, "name") and doc.name:
#             return doc.name

#         # Try to find first heading
#         for item in doc.main_text:
#             if hasattr(item, "label") and item.label == "title":
#                 return item.text

#         # Fallback to filename
#         return "Untitled Document"

#     def _extract_sections(self, doc) -> List[Dict]:
#         """
#         Extract document sections with headers.

#         Returns:
#             List of sections with title, level, and content
#         """
#         sections = []
#         current_section = None

#         for item in doc.main_text:
#             label = getattr(item, "label", "")

#             if label in ["section_header", "title", "subtitle"]:
#                 # Save previous section
#                 if current_section and current_section.get("content"):
#                     sections.append(current_section)

#                 # Start new section
#                 current_section = {
#                     "title": item.text,
#                     "level": self._get_header_level(label),
#                     "content": "",
#                 }

#             elif current_section is not None:
#                 # Add content to current section
#                 if label == "paragraph" or label == "text":
#                     current_section["content"] += item.text + "\n\n"

#         # Add last section
#         if current_section and current_section.get("content"):
#             sections.append(current_section)

#         return sections

#     def _extract_tables(self, doc) -> List[Dict]:
#         """Extract tables from document."""
#         tables = []

#         if not hasattr(doc, "tables"):
#             return tables

#         for idx, table in enumerate(doc.tables):
#             try:
#                 table_data = {
#                     "table_id": f"table_{idx}",
#                     "data": self._table_to_dict(table),
#                     "caption": getattr(table, "caption", ""),
#                 }
#                 tables.append(table_data)
#             except Exception as e:
#                 self.logger.warning(f"Failed to extract table {idx}: {e}")
#                 continue

#         return tables

#     def _table_to_dict(self, table) -> List[List[str]]:
#         """Convert table to list of lists."""
#         rows = []
#         if hasattr(table, "data"):
#             for row in table.data:
#                 rows.append([str(cell) for cell in row])
#         return rows

#     def _get_header_level(self, label: str) -> int:
#         """Get header level from label."""
#         if label == "title":
#             return 1
#         elif label == "subtitle":
#             return 2
#         elif label == "section_header":
#             return 3
#         return 4

#     def parse_multiple_pdfs(self, pdf_paths: List[str]) -> List[Dict]:
#         """
#         Parse multiple PDF files.

#         Args:
#             pdf_paths: List of PDF file paths

#         Returns:
#             List of parsed documents
#         """
#         documents = []
#         for pdf_path in pdf_paths:
#             try:
#                 doc = self.parse_pdf(pdf_path)
#                 documents.append(doc)
#             except Exception as e:
#                 self.logger.error(f"Failed to parse {pdf_path}: {e}")
#                 continue
#         return documents

"""
PDF Parser Service using Docling with GROBID backend.
Extracts structured content from PDF files including text, sections, and tables.
"""

import logging
from pathlib import Path
from typing import Dict, List

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode

from src.config import PDFParserSettings

logger = logging.getLogger(__name__)

class DoclingPDFParser:
    """
    PDF parser using Docling.
    Extracts structured content: text, sections, tables, metadata.
    """

    def __init__(self, config: PDFParserSettings):
        """
        Initialize Docling PDF parser.

        Args:
            config: PDF parser configuration settings
        """
        self.config = config
        self.logger = logging.getLogger(__name__)

        # Configure pipeline options
        pipeline_options = PdfPipelineOptions()
        pipeline_options.do_ocr = bool(config.do_ocr)
        pipeline_options.do_table_structure = bool(config.extract_tables)
        pipeline_options.do_code_enrichment = True
        pipeline_options.do_formula_enrichment = True
        # pipeline_options.table_structure_options.do_cell_matching = False
        pipeline_options.table_structure_options.mode = TableFormerMode.ACCURATE

        # Initialize document converter with format option for PDF
        self.converter = DocumentConverter(
            format_options={
                InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
            }
        )

    def parse_pdf(self, pdf_path: str) -> Dict:
        """
        Parse PDF file and extract structured content.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Dict containing:
                - title: Document title
                - full_text: Complete text content (Markdown)
                - sections: List of sections with titles and content
                - tables: Extracted tables (if enabled)
                - metadata: Document metadata
        """
        try:
            self.logger.info(f"Parsing PDF: {pdf_path}")

            result = self.converter.convert(pdf_path)
            doc = result.document

            # Full text content
            full_text = doc.export_to_markdown()

            # Export to dict for deeper structure
            doc_dict = doc.export_to_dict()

            # Sections extraction
            sections = self._extract_sections_from_dict(doc_dict, full_text, pdf_path)

            # Tables
            tables = []
            if self.config.extract_tables:
                tables = self._extract_tables_from_doc(doc, doc_dict)

            # Metadata
            metadata = {
                "file_path": str(pdf_path),
                "file_name": Path(pdf_path).name,
                "page_count": getattr(doc, "num_pages", None) or len(getattr(doc, "pages", {})),
                "has_tables": bool(tables),
            }

            document = {
                "title": self._extract_title(doc, sections, pdf_path),
                "full_text": full_text,
                "sections": sections,
                "tables": tables,
                "metadata": metadata,
            }

            self.logger.info(
                f"Successfully parsed PDF: {document['title']}, "
                f"pages: {metadata.get('page_count')}, "
                f"sections: {len(sections)}"
            )

            return document

        except Exception as e:
            self.logger.error(f"Error parsing PDF {pdf_path}: {e}", exc_info=True)
            raise

    def _extract_title(self, doc, sections: List[Dict], pdf_path: str) -> str:
        """Extract document title from doc metadata, first section, or filename."""
        if hasattr(doc, "name") and doc.name:
            return doc.name
        if sections and len(sections) > 0:
            return sections[0].get("title", "")
        return Path(pdf_path).stem or "Untitled Document"

    def _extract_sections_from_dict(self, doc_dict: dict, full_text: str, pdf_path: str) -> List[Dict]:
        """
        Extract sections from document. If structured nodes exist in dict use them,
        otherwise fallback to Markdown heading parsing.
        """
        sections: List[Dict] = []

        # Try structured node list from dict
        items = doc_dict.get("texts") or []
        if items and isinstance(items, list) and isinstance(items[0], dict) and "label" in items[0]:
            current_section = None
            for item in items:
                label = item.get("label", "")
                text = item.get("text", "")
                if label in ["title", "section_header", "subtitle"]:
                    if current_section:
                        sections.append(current_section)
                    current_section = {"title": text, "level": self._get_header_level(label), "content": ""}
                else:
                    if current_section is None:
                        current_section = {"title": "Introduction", "level": 1, "content": ""}
                    current_section["content"] += text + "\n\n"
            if current_section:
                sections.append(current_section)
            return sections

        # Fallback: parse markdown full_text by headings (#, ##, ###)
        current_section = None
        for line in full_text.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if stripped.startswith("# "):
                if current_section:
                    sections.append(current_section)
                current_section = {"title": stripped[2:].strip(), "level": 1, "content": ""}
            elif stripped.startswith("## "):
                if current_section:
                    sections.append(current_section)
                current_section = {"title": stripped[3:].strip(), "level": 2, "content": ""}
            elif stripped.startswith("### "):
                if current_section:
                    sections.append(current_section)
                current_section = {"title": stripped[4:].strip(), "level": 3, "content": ""}
            else:
                if current_section is None:
                    current_section = {"title": "Introduction", "level": 1, "content": ""}
                current_section["content"] += stripped + "\n"
        if current_section:
            sections.append(current_section)
        return sections

    def _extract_tables_from_doc(self, doc, doc_dict: dict) -> List[Dict]:
        """
        Extract tables: first try doc.tables attribute, else from dict tables list
        """
        tables: List[Dict] = []
        if hasattr(doc, "tables") and isinstance(doc.tables, list):
            for idx, table in enumerate(doc.tables):
                try:
                    tables.append({
                        "table_id": f"table_{idx}",
                        "data": self._table_to_dict(table),
                        "caption": getattr(table, "caption", "")
                    })
                except Exception as e:
                    self.logger.warning(f"Failed to extract table {idx} via doc.tables: {e}")
        else:
            # fallback: look into dict
            tbls = doc_dict.get("tables") or []
            for idx, tbl in enumerate(tbls):
                try:
                    tables.append({
                        "table_id": f"table_{idx}",
                        "data": tbl.get("data", []),
                        "caption": tbl.get("caption", "")
                    })
                except Exception as e:
                    self.logger.warning(f"Failed to extract table {idx} via dict: {e}")
        return tables

    def _table_to_dict(self, table) -> List[List[str]]:
        rows: List[List[str]] = []
        if hasattr(table, "data"):
            for row in table.data:
                rows.append([str(cell) for cell in row])
        return rows

    def _get_header_level(self, label: str) -> int:
        if label == "title":
            return 1
        elif label == "subtitle":
            return 2
        elif label == "section_header":
            return 3
        return 4

    def parse_multiple_pdfs(self, pdf_paths: List[str]) -> List[Dict]:
        documents: List[Dict] = []
        for pdf_path in pdf_paths:
            try:
                doc = self.parse_pdf(pdf_path)
                documents.append(doc)
            except Exception as e:
                self.logger.error(f"Failed to parse {pdf_path}: {e}")
                continue
        return documents
