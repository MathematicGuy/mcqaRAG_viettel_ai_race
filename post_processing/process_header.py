import re
from pathlib import Path
from typing import List, Dict, Tuple
import logging
from concurrent.futures import ThreadPoolExecutor, as_completed
from transformers import pipeline

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Vietnamese correction model
MAX_NEW_TOKENS = 256
corrector = pipeline("text2text-generation", model="bmd1905/vietnamese-correction-v2")


class HeaderExtractor:
    """Extract and process markdown headers from files."""

    @staticmethod
    def extract_headers_from_file(file_path: str) -> List[Tuple[str, str]]:
        """
        Extract all headers from a markdown file.

        Args:
            file_path: Path to markdown file

        Returns:
            List of (header_level, header_text) tuples
        """
        try:
            content = Path(file_path).read_text(encoding='utf-8')
            headers = []

            # Pattern to match markdown headers (# or ##, ###, etc.)
            pattern = r'^(#{1,6})\s+(.+)$'

            for line in content.split('\n'):
                match = re.match(pattern, line)
                if match:
                    level = match.group(1)
                    text = match.group(2).strip()
                    headers.append((level, text))

            return headers

        except Exception as e:
            logger.error(f"Error extracting headers from {file_path}: {e}")
            return []

    @staticmethod
    def extract_headers_from_directory(
        input_dir: str,
        file_pattern: str = '*.md'
    ) -> Dict[str, List[Tuple[str, str]]]:
        """
        Extract headers from all markdown files in a directory.

        Args:
            input_dir: Directory containing markdown files
            file_pattern: File pattern to match (default: '*.md')

        Returns:
            Dictionary mapping file names to list of headers
        """
        try:
            input_path = Path(input_dir)

            if not input_path.exists():
                logger.error(f"Directory does not exist: {input_dir}")
                return {}

            md_files = list(input_path.glob(file_pattern))

            if not md_files:
                logger.warning(f"No files matching {file_pattern} found in {input_dir}")
                return {}

            logger.info(f"Found {len(md_files)} files")

            headers_dict = {}
            for md_file in md_files:
                headers = HeaderExtractor.extract_headers_from_file(str(md_file))
                if headers:
                    headers_dict[md_file.name] = headers

            return headers_dict

        except Exception as e:
            logger.error(f"Error extracting headers from directory {input_dir}: {e}")
            return {}


class HeaderCorrector:
    """Correct headers using Vietnamese text correction model."""

    def __init__(self, max_new_tokens: int = 256, batch_size: int = 32):
        """
        Initialize the header corrector.

        Args:
            max_new_tokens: Maximum new tokens to generate (replaces max_length)
            batch_size: Batch size for processing
        """
        self.max_new_tokens = max_new_tokens
        self.batch_size = batch_size
        self.corrector = pipeline(
            "text2text-generation",
            model="bmd1905/vietnamese-correction-v2"
        )

    def _lowercase_header(self, text: str) -> str:
        """
        Convert header text to lowercase for LLM processing.

        Args:
            text: Header text to lowercase

        Returns:
            Lowercased text
        """
        return text.lower()

    def _uppercase_header(self, text: str) -> str:
        """
        Convert header text back to uppercase after correction.

        Args:
            text: Corrected header text to uppercase

        Returns:
            Uppercased text
        """
        return text.upper()

    def correct_single_header(self, text: str) -> str:
        """
        Correct a single header text.

        Args:
            text: Header text to correct

        Returns:
            Corrected header text (uppercased)
        """
        try:
            if not text or len(text.strip()) == 0:
                return text

            # Convert to lowercase for LLM
            lowercase_text = self._lowercase_header(text)

            # Correct using LLM (use max_new_tokens instead of max_length)
            result = self.corrector(lowercase_text, max_new_tokens=self.max_new_tokens)
            corrected = result[0]['generated_text']

            # Convert back to uppercase
            uppercase_text = self._uppercase_header(corrected)

            logger.debug(f"Original: {text}")
            logger.debug(f"Lowercase: {lowercase_text}")
            logger.debug(f"Corrected: {corrected}")
            logger.debug(f"Uppercase: {uppercase_text}")

            return uppercase_text

        except Exception as e:
            logger.error(f"Error correcting header '{text}': {e}")
            return text

    def correct_headers_batch(self, headers: List[str]) -> List[str]:
        """
        Correct multiple headers in batch.

        Args:
            headers: List of header texts to correct

        Returns:
            List of corrected header texts (uppercased)
        """
        try:
            if not headers:
                return []

            # Process in batches
            corrected = []
            for i in range(0, len(headers), self.batch_size):
                batch = headers[i:i + self.batch_size]

                # Filter out empty headers
                batch = [h for h in batch if h.strip()]

                if batch:
                    # Convert to lowercase for LLM
                    lowercase_batch = [self._lowercase_header(h) for h in batch]

                    # Correct using LLM (use max_new_tokens instead of max_length)
                    results = self.corrector(lowercase_batch, max_new_tokens=self.max_new_tokens)

                    # Convert back to uppercase
                    corrected_batch = [self._uppercase_header(r['generated_text']) for r in results]

                    corrected.extend(corrected_batch)
                else:
                    corrected.extend(batch)

            return corrected

        except Exception as e:
            logger.error(f"Error correcting headers batch: {e}")
            return headers

    def correct_file_headers(
        self,
        input_file: str,
        output_file: str = None
    ) -> Dict:
        """
        Correct all headers in a markdown file.

        Args:
            input_file: Input markdown file
            output_file: Output file (optional, overwrites input if not specified)

        Returns:
            Dictionary with correction statistics
        """
        try:
            input_path = Path(input_file)

            if not input_path.exists():
                logger.error(f"File does not exist: {input_file}")
                return {'status': 'error', 'message': 'File not found'}

            # Extract headers
            headers = HeaderExtractor.extract_headers_from_file(input_file)

            if not headers:
                logger.warning(f"No headers found in {input_file}")
                return {'status': 'warning', 'message': 'No headers found', 'corrected_count': 0}

            # Extract just the text for correction
            header_texts = [text for _, text in headers]

            # Correct headers
            corrected_texts = self.correct_headers_batch(header_texts)

            # Read original content
            content = input_path.read_text(encoding='utf-8')

            # Replace headers with corrected versions
            for (level, original), corrected in zip(headers, corrected_texts):
                original_header = f"{level} {original}"
                corrected_header = f"{level} {corrected}"
                content = content.replace(original_header, corrected_header, 1)

            # Write output
            if output_file:
                output_path = Path(output_file)
            else:
                output_path = input_path

            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(content, encoding='utf-8')

            logger.info(f"✓ Corrected {len(headers)} headers in {input_path.name}")

            return {
                'status': 'success',
                'file': input_path.name,
                'corrected_count': len(headers),
                'output_file': str(output_path)
            }

        except Exception as e:
            logger.error(f"Error processing file {input_file}: {e}")
            return {'status': 'error', 'message': str(e)}


class ParallelHeaderProcessor:
    """Process headers from multiple files in parallel."""

    def __init__(self, max_workers: int = 4):
        """
        Initialize parallel processor.

        Args:
            max_workers: Number of parallel workers
        """
        self.max_workers = max_workers
        self.corrector = HeaderCorrector()

    def process_directory(
        self,
        input_dir: str,
        output_dir: str = None,
        file_pattern: str = '*.md'
    ) -> None:
        """
        Process all markdown files in a directory in parallel.

        Args:
            input_dir: Input directory
            output_dir: Output directory (optional, overwrites input if not specified)
            file_pattern: File pattern to match
        """
        try:
            input_path = Path(input_dir)

            if not input_path.exists():
                logger.error(f"Directory does not exist: {input_dir}")
                return

            md_files = list(input_path.glob(file_pattern))

            if not md_files:
                logger.warning(f"No files found in {input_dir}")
                return

            logger.info(f"Processing {len(md_files)} files in parallel with {self.max_workers} workers...")

            # Process files in parallel
            with ThreadPoolExecutor(max_workers=self.max_workers) as executor:
                futures = {}

                for md_file in md_files:
                    if output_dir:
                        output_file = Path(output_dir) / md_file.name
                    else:
                        output_file = None

                    future = executor.submit(
                        self.corrector.correct_file_headers,
                        str(md_file),
                        str(output_file) if output_file else None
                    )
                    futures[future] = md_file.name

                # Process completed tasks
                completed = 0
                for future in as_completed(futures):
                    completed += 1
                    file_name = futures[future]
                    try:
                        result = future.result()
                        logger.info(f"[{completed}/{len(md_files)}] {result}")
                    except Exception as e:
                        logger.error(f"Error processing {file_name}: {e}")

            logger.info(f"✓ Completed processing {len(md_files)} files")

        except Exception as e:
            logger.error(f"Error processing directory {input_dir}: {e}")


def test_single_file(test_file='../private_test_output_html/Public_447.md', output_file='../private_test_output_html_corrected/Public_447.md'):
    """Test correction with a single file."""
    logger.info("="*60)
    logger.info("TESTING SINGLE FILE CORRECTION")
    logger.info("="*60)

    # Check if test file exists
    if not Path(test_file).exists():
        logger.error(f"Test file not found: {test_file}")
        logger.info("Available files in private_test_output_html:")
        test_dir = Path('private_test_output_html')
        if test_dir.exists():
            for f in list(test_dir.glob('*.md'))[:5]:
                logger.info(f"  - {f.name}")
        return

    # Extract headers from test file
    logger.info(f"\n1. Extracting headers from {test_file}...")
    headers = HeaderExtractor.extract_headers_from_file(test_file)
    logger.info(f"   Found {len(headers)} headers:")
    for level, text in headers[:5]:  # Show first 5
        logger.info(f"   {level} {text}")

    if len(headers) > 5:
        logger.info(f"   ... and {len(headers) - 5} more")

    # Correct headers
    logger.info(f"\n2. Correcting headers...")
    corrector = HeaderCorrector()
    result = corrector.correct_file_headers(test_file, output_file)

    logger.info(f"   Result: {result}")

    # Show corrected headers
    if Path(output_file).exists():
        logger.info(f"\n3. Corrected headers:")
        corrected_headers = HeaderExtractor.extract_headers_from_file(output_file)
        for level, text in corrected_headers[:5]:  # Show first 5
            logger.info(f"   {level} {text}")

        if len(corrected_headers) > 5:
            logger.info(f"   ... and {len(corrected_headers) - 5} more")

        logger.info(f"\n✓ Test completed! Output saved to: {output_file}")

    logger.info("="*60)


def main():
    """Main function to process headers."""

    # Option 1: Test with single file first
    test_file = '../private_test_output_html/Public_447.md'
    output_file = '../private_test_output_html_corrected/Public_447.md'

    test_single_file(test_file, output_file)

    # Option 2: Uncomment below to process entire directory
    # logger.info("\n" + "="*60)
    # logger.info("PROCESSING ALL FILES")
    # logger.info("="*60 + "\n")
    #
    # # Configuration
    # input_dir = 'private_test_output_html'
    # output_dir = 'private_test_output_html_corrected'
    #
    # # Create parallel processor
    # processor = ParallelHeaderProcessor(max_workers=4)
    #
    # # Process all files
    # processor.process_directory(
    #     input_dir=input_dir,
    #     output_dir=output_dir,
    #     file_pattern='*.md'
    # )


if __name__ == "__main__":
    main()