# Automated File Organizer

A command-line utility that automatically scans a directory and organizes files into categorized folders based on their file extensions. This automated application demonstrates batch processing and file system operations.

## Features

- **Automatic Categorization**: Sorts files by type (Documents, Images, Videos, etc.)
- **Safe Operation**: Includes dry-run mode to preview changes
- **Conflict Resolution**: Handles duplicate filenames automatically
- **Comprehensive Coverage**: Supports 40+ file extensions
- **Error Handling**: Robust error handling for file operations
- **Progress Reporting**: Detailed summary of operations performed

## How to Run

```bash
# Organize files in current directory
python3 main.py .

# Organize files in a specific directory
python3 main.py /path/to/directory

# Preview changes without moving files
python3 main.py /path/to/directory --dry-run
```

## Supported Categories

- **Documents**: PDF, DOC, XLS, PPT, TXT, etc.
- **Images**: JPG, PNG, GIF, BMP, SVG, etc.
- **Videos**: MP4, AVI, MKV, MOV, etc.
- **Music**: MP3, WAV, FLAC, AAC, etc.
- **Archives**: ZIP, RAR, 7Z, TAR, etc.
- **Code**: PY, JS, HTML, CSS, JAVA, etc.
- **Executables**: EXE, MSI, DMG, DEB, etc.
- **Others**: Files with unrecognized extensions

## Example Usage

```bash
# Create some test files
touch document.pdf image.jpg video.mp4 script.py

# Run the organizer
python3 main.py .

# Output:
Starting file organization in: .
--------------------------------------------------
Created directory: ./Documents
Created directory: ./Images
Created directory: ./Videos
Created directory: ./Code
Moved: document.pdf → ./Documents/document.pdf
Moved: image.jpg → ./Images/image.jpg
Moved: video.mp4 → ./Videos/video.mp4
Moved: script.py → ./Code/script.py

==================================================
ORGANIZATION SUMMARY
==================================================
Files processed: 4
Files moved: 4
Directories created: 4
Errors encountered: 0

File organization completed successfully!
```

## Learning Concepts

This application demonstrates:
- Command-line argument parsing with argparse
- File system operations using pathlib
- Batch processing of multiple files
- Error handling and exception management
- Dictionary-based categorization systems
- Automated workflow implementation