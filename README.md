# 🗂️ File System Analyzer

A command-line tool that analyzes and reports on the file system structure and usage in a specified Linux directory.

## ✅ Features

- 🔍 Recursively traverses a given directory
- 🗂️ Categorizes files by type (text, image, code, archive, executable, other)
- 📏 Calculates total size per file type
- 🔐 Identifies files with world-writable permissions
- 🐘 Lists files larger than a user-defined threshold (MB)
- 💥 Robust error handling for inaccessible files or directories

---

## 📁 Project Structure

```bash
.
├── analyzer.py         # Main script
├── cli.py              # Command-line argument parser
├── file_utils.py       # File classification and size logic
├── permissions.py      # World-writable detection
├── large_files.py      # Large file detection
├── test_cases.py       # Test file generator
├── test_dir/           # (Generated) Test data folder
└── README.md           
```

## 🚀 How to Run

```bash
python analyzer.py --path <directory_path> --threshold <size_in_MB>
```
## 🔧 Arguments

| Flag         | Description                              | Required | Default |
|--------------|------------------------------------------|----------|---------|
| `--path`     | Path to the directory to analyze         | Yes      | —       |
| `--threshold`| Size threshold (in MB) for large files   | No       | 100     |

---

## 📤 Example

```bash
python analyzer.py --path ./test_dir --threshold 50

Output:

Analyzing ./test_dir ...

File Type Breakdown:
- Text: 4 files, 0.45 MB
- Image: 2 files, 18.72 MB

Unusual Permissions (world-writable files):
- ./test_dir/logs/public.log

Large Files (> 50 MB):
- ./test_dir/videos/big_video.mp4: 220.30 MB
```