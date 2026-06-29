

# extractors/content.py

from collections import Counter
import hashlib


def read_file(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()


def get_content_analysis(file_path):
    content = read_file(file_path)
    lines = content.splitlines()
    words = content.split()

    counter = Counter(words)

    return {
        "total_words": len(words),
        "unique_words": len(counter),
        "top_keywords": counter.most_common(10),
        "preview": content[:300]
    }


def get_checksum(file_path):
    with open(file_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()