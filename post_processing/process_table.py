import re
from pathlib import Path
from typing import List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def markdown_table_to_html(markdown_text: str) -> str:
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
            for i, cell in enumerate(row):
                html.append(f'      <td>{cell}</td>')
            html.append('    </tr>')
        html.append('  </tbody>')

        html.append('</table>')

        return '\n'.join(html)

    # Replace all markdown tables with HTML tables
    result = re.sub(table_pattern, convert_single_table, markdown_text)

    return result


def process_markdown_file(
    input_file: str,
    output_file: Optional[str] = None,
    convert_to_html: bool = True
) -> str:
    """
    Process a markdown file and convert tables to HTML.

    Args:
        input_file: Path to input markdown file
        output_file: Path to output file (optional, defaults to input_file with .html extension)
        convert_to_html: Whether to convert tables to HTML

    Returns:
        Processed content
    """
    try:
        input_path = Path(input_file)

        if not input_path.exists():
            logger.error(f"Input file does not exist: {input_file}")
            return ""

        # Read content
        content = input_path.read_text(encoding='utf-8')

        # Remove unwanted VIETTEL patterns
        # Pattern 1: Header section "## VIETTEL AI RACE"
        content = re.sub(
            r'##\s*VIETTEL\s*AI\s*RACE\s*\n?',
            '',
            content,
            flags=re.IGNORECASE
        )

        # Pattern 2: Table rows with VIETTEL AI RACE and separator
        # e.g., "| VIETTEL AI RACE   | TD448   |" and "|-------------------|---------|"
        content = re.sub(
            r'\|\s*VIETTEL\s*AI\s*RACE\s*\|[^\n]*\n\s*\|[-\s|]*\|\s*\n?',
            '',
            content,
            flags=re.IGNORECASE
        )

        if convert_to_html:
            # Convert tables to HTML
            processed_content = markdown_table_to_html(content)
        else:
            processed_content = content

        # Determine output path
        if output_file is None:
            output_path = input_path.with_suffix('.html')
        else:
            output_path = Path(output_file)

        # Write output
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(processed_content, encoding='utf-8')

        logger.info(f"Processed file saved to: {output_path}")

        return processed_content

    except Exception as e:
        logger.error(f"Error processing file {input_file}: {e}", exc_info=True)
        return ""


def process_all_markdown_files(
    input_dir: str = 'private_test_output',
    output_dir: str = 'private_test_output_html'
) -> None:
    """
    Process all markdown files in a directory and convert tables to HTML.

    Args:
        input_dir: Directory containing markdown files
        output_dir: Directory to save HTML files
    """
    try:
        input_path = Path(input_dir)
        output_path = Path(output_dir)

        if not input_path.exists():
            logger.error(f"Input directory does not exist: {input_dir}")
            return

        # Get all .md files
        md_files = list(input_path.glob('*.md'))

        if not md_files:
            logger.warning(f"No .md files found in {input_dir}")
            return

        logger.info(f"Found {len(md_files)} markdown files to process")

        # Process each file
        for md_file in md_files:
            output_file = output_path / md_file.name
            process_markdown_file(
                input_file=str(md_file),
                output_file=str(output_file),
                convert_to_html=True
            )

        logger.info(f"Successfully processed {len(md_files)} files to {output_dir}")

    except Exception as e:
        logger.error(f"Error processing directory {input_dir}: {e}", exc_info=True)


def create_html_document(
    markdown_content: str,
    title: str = "Document"
) -> str:
    """
    Create a complete HTML document with tables converted.

    Args:
        markdown_content: Markdown content
        title: Document title

    Returns:
        Complete HTML document
    """
    # Convert tables
    body_content = markdown_table_to_html(markdown_content)

    # Replace markdown headers with HTML headers
    body_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', body_content, flags=re.MULTILINE)
    body_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', body_content, flags=re.MULTILINE)

    # Replace line breaks
    body_content = body_content.replace('\n\n', '<br><br>')

    html_template = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            line-height: 1.6;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #f2f2f2;
            font-weight: bold;
        }}
        tr:nth-child(even) {{
            background-color: #f9f9f9;
        }}
        h1, h2 {{
            color: #333;
        }}
    </style>
</head>
<body>
{body_content}
</body>
</html>
"""

    return html_template


if __name__ == "__main__":
    # Example 1: Process single file
    # process_markdown_file(
    #     input_file='private_test_output\\Public_427.md',
    #     output_file='private_test_output_html\\Public_427.md'
    # )

    # Example 2: Process all files in directory
    process_all_markdown_files(
        input_dir='../private_test_output',
        output_dir='../private_test_output_html'
    )

    # Example 3: Create complete HTML document
    # md_content = Path('private_test_output/Public_427.md').read_text(encoding='utf-8')
    # html_doc = create_html_document(md_content, title="Public_427")
    # Path('private_test_output_html/Public_427_complete.html').write_text(html_doc, encoding='utf-8')