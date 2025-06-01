# Entry point for the File System Analyzer tool.
# This script coordinates CLI parsing and calls all major analysis functions:
# - file type categorization
# - world-writable permission detection
# - large file identification

from cli import parse_arguments
from file_utils import analyze_file_types
from permissions import find_world_writable_files
from large_files import find_large_files
import os

def main():
    """
    Main function that coordinates the file system analysis:
    - Parses CLI arguments
    - Checks path validity
    - Runs type analysis, permission scan, and large file detection
    - Prints results in readable format
    """
    # Parse command-line arguments using argparse (defined in cli.py)
    args = parse_arguments()
    directory = args.path
    threshold_mb = args.threshold

    # Ensure the provided directory exists
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    print(f"Analyzing {directory} ...\n")

    # Analyze file types and sizes
    type_summary = analyze_file_types(directory)

    # Identify files with world-writable permissions
    perm_issues = find_world_writable_files(directory)

    # Identify files larger than the given threshold (in MB)
    large_files = find_large_files(directory, threshold_mb)

    # Display file type statistics
    print("File Type Breakdown:")
    for category, (count, total_size) in type_summary.items():
        print(f"- {category}: {count} files, {total_size / 1024**2:.2f} MB")

    # Display world-writable files
    print("\nUnusual Permissions (world-writable files):")
    if perm_issues:
        for path in perm_issues:
            print(f"- {path}")
    else:
        print("None")

    # Display large files
    print(f"\nLarge Files (> {threshold_mb} MB):")
    if large_files:
        for path, size in large_files:
            print(f"- {path}: {size / 1024**2:.2f} MB")
    else:
        print("None")

# Run the analyzer only if this file is executed directly
if __name__ == "__main__":
    main()
