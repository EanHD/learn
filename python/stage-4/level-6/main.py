#!/usr/bin/env python3
"""
Automated File Organizer
A script that automatically organizes files in a directory based on their file types.
"""

import os
import shutil
from pathlib import Path
import argparse
import sys

class FileOrganizer:
    def __init__(self, target_directory, dry_run=False):
        self.target_directory = Path(target_directory)
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'files_moved': 0,
            'directories_created': 0,
            'errors': 0
        }

        # Define file type categories and their extensions
        self.categories = {
            'Documents': ['.pdf', '.doc', '.docx', '.txt', '.rtf', '.odt', '.xls', '.xlsx', '.ppt', '.pptx'],
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp', '.ico'],
            'Videos': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm', '.m4v'],
            'Music': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'],
            'Archives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
            'Code': ['.py', '.js', '.html', '.css', '.java', '.cpp', '.c', '.php', '.rb', '.go', '.rs'],
            'Executables': ['.exe', '.msi', '.dmg', '.app', '.deb', '.rpm'],
            'Others': []  # Catch-all for unrecognized extensions
        }

    def get_category(self, file_path):
        """Determine the category for a file based on its extension."""
        extension = file_path.suffix.lower()

        for category, extensions in self.categories.items():
            if extension in extensions:
                return category

        return 'Others'

    def create_category_directory(self, category):
        """Create a directory for the specified category if it doesn't exist."""
        category_dir = self.target_directory / category

        if not category_dir.exists():
            if not self.dry_run:
                try:
                    category_dir.mkdir(parents=True, exist_ok=True)
                    print(f"Created directory: {category_dir}")
                except Exception as e:
                    print(f"Error creating directory {category_dir}: {e}")
                    self.stats['errors'] += 1
                    return None
            else:
                print(f"Would create directory: {category_dir}")

            self.stats['directories_created'] += 1

        return category_dir

    def move_file(self, source_path, destination_dir):
        """Move a file to the destination directory."""
        filename = source_path.name
        destination_path = destination_dir / filename

        # Handle filename conflicts
        counter = 1
        while destination_path.exists():
            stem = source_path.stem
            suffix = source_path.suffix
            new_filename = f"{stem}_{counter}{suffix}"
            destination_path = destination_dir / new_filename
            counter += 1

        if not self.dry_run:
            try:
                shutil.move(str(source_path), str(destination_path))
                print(f"Moved: {source_path} → {destination_path}")
            except Exception as e:
                print(f"Error moving {source_path}: {e}")
                self.stats['errors'] += 1
                return False
        else:
            print(f"Would move: {source_path} → {destination_path}")

        self.stats['files_moved'] += 1
        return True

    def organize_files(self):
        """Main method to organize all files in the target directory."""
        if not self.target_directory.exists():
            print(f"Error: Directory '{self.target_directory}' does not exist.")
            return False

        if not self.target_directory.is_dir():
            print(f"Error: '{self.target_directory}' is not a directory.")
            return False

        print(f"Starting file organization in: {self.target_directory}")
        if self.dry_run:
            print("DRY RUN MODE - No files will be moved")
        print("-" * 50)

        # Get all files in the directory (not subdirectories)
        files = [f for f in self.target_directory.iterdir() if f.is_file()]

        if not files:
            print("No files found to organize.")
            return True

        for file_path in files:
            self.stats['files_processed'] += 1

            # Skip the script itself if it's in the target directory
            if file_path.name == 'main.py':
                continue

            category = self.get_category(file_path)
            category_dir = self.create_category_directory(category)

            if category_dir:
                self.move_file(file_path, category_dir)

        return True

    def print_summary(self):
        """Print a summary of the organization process."""
        print("\n" + "="*50)
        print("ORGANIZATION SUMMARY")
        print("="*50)
        print(f"Files processed: {self.stats['files_processed']}")
        print(f"Files moved: {self.stats['files_moved']}")
        print(f"Directories created: {self.stats['directories_created']}")
        print(f"Errors encountered: {self.stats['errors']}")

        if self.dry_run:
            print("\nThis was a dry run. No files were actually moved.")
            print("Run without --dry-run to perform the actual organization.")
        else:
            print("\nFile organization completed successfully!")

def main():
    """Main application entry point."""
    parser = argparse.ArgumentParser(description='Automatically organize files by type')
    parser.add_argument('directory', help='Directory to organize')
    parser.add_argument('--dry-run', action='store_true',
                       help='Show what would be done without making changes')

    args = parser.parse_args()

    # If no directory provided, use current directory
    if not args.directory:
        args.directory = '.'

    organizer = FileOrganizer(args.directory, args.dry_run)

    success = organizer.organize_files()
    organizer.print_summary()

    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()