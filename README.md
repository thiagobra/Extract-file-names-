# File Lister

## Description

File Lister is a Python utility that generates a list of all files within a specified directory. For each file, it provides the last modification date and the file size in megabytes. The output is written to a text file, making it easy to review the contents of a folder. This tool is helpful for quickly getting an overview of files, their sizes, and when they were last updated.

## Features

*   Lists all files in a given directory.
*   Provides the last modification date for each file.
*   Displays file sizes in megabytes (MB).
*   Writes the output to a user-specified text file.
*   Uses `pathlib` for robust file path handling.
*   Includes comprehensive error handling and logging.
*   Adheres to modern Python best practices (type hinting, f-strings, etc.).

## Installation

This project does not require any external dependencies outside the Python standard library. You can run it directly after cloning the repository.

**No other installation is needed.**

## Usage

1. **Navigate to the directory:**

    Open your terminal or command prompt and navigate to the directory where you saved the Python script (`file_lister.py` or similar name).

2. **Run the script:**

    Execute the script using the following command:

    ```bash
    python file_lister.py
    ```

    *   The script will list the files in the current directory (where the script is located).
    *   The output will be saved to a file named `file_details.txt` in the same directory.

**Customization:**

You can modify the `folder_path` and `output_file` variables in the `if __name__ == "__main__":` block of the script to specify a different directory or output file name. For example:

```python
if __name__ == "__main__":
    folder_path = Path("./my_folder")  # List files in the "my_folder" subdirectory
    output_file = Path("my_files.txt")  # Save output to "my_files.txt"
    list_files_in_folder(folder_path, output_file)
Use code with caution.
Markdown
Error Handling
The script includes error handling to catch potential issues (e.g., invalid directory path, file access errors). Error messages are logged using Python's logging module and displayed in the console, with the most important part of the error and the stack trace.

Logging
The script uses the logging module to provide information about its execution, warnings, and any errors that occur. The log messages include timestamps and severity levels (INFO, WARNING, ERROR). This helps you to understand what happened, and to debug any potential issues.

Contributing
Contributions are welcome! If you find a bug or want to suggest an enhancement, please open an issue or submit a pull request on the project's repository.

License
This project is licensed under the MIT License - see the LICENSE file for details. (You should create a LICENSE file and put the MIT License text in there if you choose this license). Or you can use any license you want.

Author
thiagobra