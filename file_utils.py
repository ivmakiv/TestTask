# Contains file categorization and size analysis logic

import os
from collections import defaultdict
from pathlib import Path

# Predefined file type categories based on common file extensions
# These are used to classify files into meaningful groups during analysis
CATEGORY_EXTENSIONS = {
    'Text': ['.txt', '.log', '.md', '.csv', '.ini', '.cfg'],
    'Code': ['.py', '.js', '.ts', '.java', '.cpp', '.c', '.cs', '.php', '.html', '.css', '.json', '.xml', '.yml', '.yaml', '.ipynb'],
    'Image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg'],
    'Audio': ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a'],
    'Video': ['.mp4', '.avi', '.mkv', '.mov', '.wmv', '.flv', '.webm'],
    'Archive': ['.zip', '.rar', '.tar', '.gz', '.7z', '.bz2', '.xz', '.iso'],
    'Document': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.odt', '.ods'],
    'Executable': ['.exe', '.msi', '.sh', '.bin', '.app', '.bat', '.com', '.run'],
    'Database': ['.db', '.sqlite', '.sql', '.mdb', '.accdb'],
    'GeoData': ['.shp', '.shx', '.dbf', '.gml', '.kml', '.kmz', '.gpkg', '.geojson', '.tif', '.tiff', '.vrt', '.nc'],
    'Presentation': ['.key', '.odp'],
    'Spreadsheet': ['.csv', '.xls', '.xlsx', '.ods'],
}

def categorize_file(path):
    """
    Determine the category of a file based on its extension or executable permission.

    Args:
        path (Path): The path to the file.

    Returns:
        str: The category name (e.g., 'Text', 'Image', 'Executable', etc.)
    """
    ext = path.suffix.lower()  # Get the file extension (e.g., '.txt')

    # Check if the extension matches any known category
    for category, extensions in CATEGORY_EXTENSIONS.items():
        if ext in extensions:
            return category

    # If extension is unknown but file is executable, treat as 'Executable'
    if os.access(path, os.X_OK):
        return 'Executable'

    # If not matched, return 'Other' as fallback category
    return 'Other'

def analyze_file_types(root_dir):
    """
    Recursively scan the given directory and summarize file counts and sizes by category.

    Args:
        root_dir (str or Path): The root directory to analyze.

    Returns:
        dict: A dictionary where keys are category names and values are [file_count, total_size_in_bytes].
    """
    # Initialize a dictionary with default values: [count, total_size]
    summary = defaultdict(lambda: [0, 0])

    # Traverse the directory tree
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            try:
                # Build full file path
                file_path = Path(dirpath) / file

                # Classify the file by type
                category = categorize_file(file_path)

                # Increment the file count and accumulate the file size
                summary[category][0] += 1
                summary[category][1] += file_path.stat().st_size

            except Exception:
                # Skip files that can't be accessed (e.g., due to permissions or errors)
                continue

    return summary
