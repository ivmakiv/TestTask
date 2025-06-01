# This module defines logic to detect files that exceed a user-defined size threshold.

import os
from pathlib import Path

def find_large_files(root_dir, threshold_mb):
    """
    Traverse the given directory recursively and return a list of files
    that are larger than the specified size threshold.

    Args:
        root_dir (str or Path): The root directory to start scanning from.
        threshold_mb (int): The size threshold in megabytes.

    Returns:
        list of tuples: Each tuple contains (file_path, size_in_bytes) for large files.
    """
    # Convert threshold from MB to bytes
    threshold_bytes = threshold_mb * 1024 * 1024

    # This will hold all large files found
    large_files = []

    # Recursively walk through the directory
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                # Construct full file path
                file_path = Path(dirpath) / file

                # Get file size in bytes
                size = file_path.stat().st_size

                # Check if file exceeds the size threshold
                if size > threshold_bytes:
                    # Add as (path, size) tuple
                    large_files.append((str(file_path), size))

            except Exception:
                # If any error occurs (e.g., permission denied), skip this file
                continue

    return large_files
