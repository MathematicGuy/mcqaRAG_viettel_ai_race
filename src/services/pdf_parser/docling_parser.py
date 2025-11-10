import logging
from pathlib import Path
from typing import Dict, List
import re

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
            pdf_path: Path to PDF file e.g. data\\pdf\\Public_428.pdf

        Returns:
            Dict containing:
                - title: Document title
                - full_text: Complete text content (Markdown with post-processing)
                - sections: List of sections with titles and content
                - tables: Extracted tables (if enabled)
                - metadata: Document metadata
        """
        try:
            OUTPUT_PATH = 'private_test_output'
            self.logger.info(f"Parsing PDF: {pdf_path}")

            result = self.converter.convert(pdf_path)
            doc = result.document

            # Full text content
            full_text = doc.export_to_markdown()

            # Clean VIETTEL patterns and convert tables
            full_text = self._post_process_markdown(full_text)

            # save markdown to OUTPUT_PATH/filename.md for debug
            output_md_path = Path(OUTPUT_PATH) / (Path(pdf_path).stem + '.md')
            output_md_path.parent.mkdir(parents=True, exist_ok=True)
            output_md_path.write_text(full_text, encoding='utf-8')
            self.logger.info(f"Saved markdown to: {output_md_path}")

            # Export to dict for deeper structure
            doc_dict = doc.export_to_dict()

            # Sections extraction (uses cleaned full_text)
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


    def _post_process_markdown(self, markdown_text: str) -> str:
        """
        Post-process markdown: remove VIETTEL patterns and convert tables to HTML.

        Args:
            markdown_text: Raw markdown from docling

        Returns:
            Cleaned markdown with HTML tables
        """
        # Remove VIETTEL header sections
        markdown_text = re.sub(
            r'##\s*VIETTEL\s*AI\s*RACE\s*\n?',
            '',
            markdown_text,
            flags=re.IGNORECASE
        )

        # Remove VIETTEL table rows with separators
        markdown_text = re.sub(
            r'\|\s*VIETTEL\s*AI\s*RACE\s*\|[^\n]*\n\s*\|[-\s|]*\|\s*\n?',
            '',
            markdown_text,
            flags=re.IGNORECASE
        )

        # Convert markdown tables to HTML
        markdown_text = self._markdown_table_to_html(markdown_text)

        return markdown_text


    def _markdown_table_to_html(self, markdown_text: str) -> str:
        """
        Convert markdown tables to HTML tables.

        Args:
            markdown_text: Markdown content containing tables

        Returns:
            HTML formatted text with tables converted
        """
        # Pattern to match markdown tables
        table_pattern = r'\|[^\n]+\|\n\|[-:\s|]+\|\n(?:\|[^\n]+\|\n)+'

        def convert_single_table(match):
            table_md = match.group(0)
            lines = table_md.strip().split('\n')

            if len(lines) < 3:  # Need header, separator, and at least one row
                return table_md

            # Extract header
            header_line = lines[0]
            headers = [cell.strip() for cell in header_line.split('|')[1:-1]]

            # Skip separator line (lines[1])

            # Extract data rows
            data_rows = []
            for line in lines[2:]:
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                if cells:  # Skip empty rows
                    data_rows.append(cells)

            # Build HTML table
            html = ['<table border="1" cellpadding="5" cellspacing="0">']

            # Add header
            html.append('  <thead>')
            html.append('    <tr>')
            for header in headers:
                html.append(f'      <th>{header}</th>')
            html.append('    </tr>')
            html.append('  </thead>')

            # Add body
            html.append('  <tbody>')
            for row in data_rows:
                html.append('    <tr>')
                for cell in row:
                    html.append(f'      <td>{cell}</td>')
                html.append('    </tr>')
            html.append('  </tbody>')

            html.append('</table>')

            return '\n'.join(html)

        # Replace all markdown tables with HTML tables
        result = re.sub(table_pattern, convert_single_table, markdown_text)
        return result


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
