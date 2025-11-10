from pathlib import Path
from typing import List
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def extract_md_files_to_answers(
    output_path: str = 'private_test_output',
    output_file: str = 'data/answer.md'
) -> None:
    """
    Extract all .md files from OUTPUT_PATH and combine them into a single answers.md file.

    Args:
        output_path: Path to the directory containing .md files
        output_file: Path to the output answers.md file

    Structure:
        ### TASK EXTRACT
        # Public_427
        <content of Public_427.md>

        # Public_428
        <content of Public_428.md>
        ...
    """
    try:
        output_dir = Path(output_path)

        if not output_dir.exists():
            logger.error(f"Output directory does not exist: {output_path}")
            return

        # Get all .md files and sort them by name
        md_files: List[Path] = sorted(output_dir.glob('*.md'))

        if not md_files:
            logger.warning(f"No .md files found in {output_path}")
            return

        logger.info(f"Found {len(md_files)} .md files")

        # Create output file
        output_file_path = Path(output_file)
        output_file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_file_path, 'w', encoding='utf-8') as outfile:
            # Write header
            outfile.write("### TASK EXTRACT\n\n")

            # Process each .md file
            for md_file in md_files:
                file_name = md_file.stem  # Get filename without extension
                logger.info(f"Processing: {file_name}")

                # Write file header
                outfile.write(f"# {file_name}\n")

                # Read and write content
                try:
                    content = md_file.read_text(encoding='utf-8')
                    outfile.write(content)

                    # Add spacing between files
                    if not content.endswith('\n'):
                        outfile.write('\n')
                    outfile.write('\n')

                except Exception as e:
                    logger.error(f"Error reading {md_file}: {e}")
                    continue

        logger.info(f"Successfully created {output_file} with {len(md_files)} files")

    except Exception as e:
        logger.error(f"Error extracting md files: {e}", exc_info=True)


if __name__ == "__main__":
    # Example usage
    extract_md_files_to_answers(
        output_path='../private_test_output_html',
        output_file='../data/answer4.md'
    )