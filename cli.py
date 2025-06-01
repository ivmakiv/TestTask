# Handles command-line argument parsing for the File System Analyzer tool.

import argparse

def parse_arguments():
    """
    Parses command-line arguments provided by the user.

    Returns:
        argparse.Namespace: Parsed arguments with fields 'path' and 'threshold'.
    """
    # Create an ArgumentParser object with a helpful description
    parser = argparse.ArgumentParser(description="File System Analyzer")

    # --path argument (REQUIRED)
    # This is the root directory the user wants to analyze
    parser.add_argument(
        '--path',
        required=True,
        help='Directory to analyze (must exist and be accessible)'
    )

    # --threshold argument (OPTIONAL)
    # Sets the minimum size (in MB) for files to be reported as "large"
    parser.add_argument(
        '--threshold',
        type=int,
        default=100,
        help='Size threshold in MB for large file detection (default: 100MB)'
    )

    # Parse the arguments from the command line and return them as a Namespace object
    return parser.parse_args()
