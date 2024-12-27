import os
from datetime import datetime
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def list_files_in_folder(folder_path: Path, output_file: Path) -> None:
    """
    Generates a list of all files in the specified folder, including their
    last modification date and size in megabytes, and writes it to a text file.

    Args:
        folder_path (Path): Path to the folder containing the files.
        output_file (Path): Path to the output text file.
    """
    try:
        with open(output_file, "w", encoding="utf-8") as file:
            _write_header(file)
            for item in folder_path.iterdir():
                if item.is_file():
                    _write_file_details(item, file)
            logging.info(f"File details successfully written to '{output_file}'.")

    except Exception as e:
        logging.error(f"An error occurred: {e}", exc_info=True)


def _write_header(file) -> None:
    """Writes the header to the output file."""
    header = (
        "======================================================================================================================\n"
        "This file contains a list of all files in the current folder, along with their last modification date and size in MB.\n"
        "======================================================================================================================\n"
    )
    file.write(header)


def _write_file_details(file_path: Path, file) -> None:
    """Writes the details of a single file to the output file."""
    try:
        modification_time = file_path.stat().st_mtime
        formatted_time = datetime.fromtimestamp(modification_time).strftime('%Y-%m-%d %H:%M:%S')
        file_size_bytes = file_path.stat().st_size
        file_size_mb = round(file_size_bytes / (1024 * 1024), 2)

        file.write(f"{file_path.name} ({formatted_time} - {file_size_mb} MB)\n")
    except Exception as e:
        logging.warning(f"Could not retrieve file details for '{file_path}': {e}", exc_info=True)


if __name__ == "__main__":
    # Get the current working directory
    folder_path = Path.cwd()
    output_file = Path("file_details.txt")
    list_files_in_folder(folder_path, output_file)
