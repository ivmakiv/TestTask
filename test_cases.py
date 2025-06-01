import os
from pathlib import Path

def create_test_environment():
    test_dir = Path("test_dir")
    test_dir.mkdir(exist_ok=True)

    # 1. Text file (~1 MB)
    with open(test_dir / "text1.txt", "w") as f:
        f.write("Hello world!\n" * 100_000)  # ~1 MB

    # 2. Image file (~5 MB fake binary)
    (test_dir / "image1.jpg").write_bytes(os.urandom(1024 * 1024 * 5))  # 5 MB

    # 3. World-writable shell script (~500 KB)
    script = test_dir / "script.sh"
    script.write_text("#!/bin/bash\n" + "echo Hello\n" * 10_000)
    script.chmod(0o777)

    # 4. Large file (~150 MB)
    with open(test_dir / "bigfile.zip", "wb") as f:
        f.write(os.urandom(1024 * 1024 * 150))  # 150 MB

    # 5. Nested subdirectory with code file (~1 MB)
    sub_dir = test_dir / "subdir"
    sub_dir.mkdir(exist_ok=True)
    (sub_dir / "nested.py").write_text("print('nested')\n" * 50_000)

    print("✅ Test environment created in ./test_dir with realistic file sizes")

if __name__ == "__main__":
    create_test_environment()
