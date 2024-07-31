
# File and Directory Content Masking Tool

## Project Description

This script is designed to mask sensitive information in files or directories by using regex patterns or specific keywords. It processes either a single file or all files within a directory, replacing matched patterns or keywords with a masked version. The tool supports a variety of file types and generates statistics on the masking process.

## Features
- Mask sensitive data in files using regex patterns and/or keywords.
- Process a single file or all files within a directory.
- Generate statistics on the number of matches for each regex pattern and keyword.
- Supports multiple file extensions, including `.txt`, `.py`, `.md`, `.json`, and `.csv`.

## Technologies Used
- Python 3
- `os`, `re`, `shutil` (Standard Python libraries for file and directory operations)
- `collections.defaultdict` (for easy statistics collection)

## Installation Steps

1. **Clone the repository:**
   - Clone this repository to your local machine.

2. **Prepare Configuration Files:**
   - Ensure you have the necessary configuration files in the `config` directory:
     - `regex_patterns.txt`: Contains the regex patterns to search for.
     - `keywords.txt`: Contains the keywords to search for.

3. **Running the Script:**
   - To start the masking process, run the script:
     ```sh
     python main.py
     ```

   **Example Usages:**
   - Mask a single file:
     1. Choose `dosya` when prompted.
     2. Enter the file path.
     3. Select whether to mask using regex, keywords, or both.
   - Mask all files in a directory:
     1. Choose `dizin` when prompted.
     2. Enter the directory path.
     3. Select whether to mask using regex, keywords, or both.

## Supported File Extensions
- **.txt**
- **.py**
- **.md**
- **.json**
- **.csv**

## Potential Enhancements
- Add support for more file extensions.
- Improve error handling and user feedback.
- Add more complex masking rules based on the file type.

## Support and Contact
If you have any questions or suggestions, feel free to contact at [kilicbartu@gmail.com](mailto:kilicbartu@gmail.com).
