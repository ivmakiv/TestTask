# This module provides functionality to detect files that are world-writable (i.e., writable by any user on the system).

import os
import stat
from pathlib import Path

def find_world_writable_files(root_dir):
    """
    Traverse the given directory recursively and return a list of files
    that have world-writable permissions (chmod o+w).

    Args:
        root_dir (str or Path): The root directory to scan.

    Returns:
        list of str: Paths to files that are world-writable.
    """
    result = []  # List to store paths of detected world-writable files

    # Walk through the directory tree
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                # Build full path to the file
                file_path = Path(dirpath) / file

                # Get file permission mode (bitmask)
                mode = file_path.stat().st_mode

                # Check if the "others" write permission bit is set (world-writable)
                if mode & stat.S_IWOTH:
                    result.append(str(file_path))  # Save the file path as a string

            except Exception:
                # Skip files that can't be accessed (e.g., due to permissions)
                continue

    return result
