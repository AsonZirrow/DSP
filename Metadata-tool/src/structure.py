

# extractors/structure.py

from collections import Counter

def analyze_structure(file_path):
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        lines = f.readlines()

    stripped = [l.strip() for l in lines if l.strip()]

    counts = Counter(stripped)

    return {
        "total_lines": len(lines),
        "unique_lines": len(counts),
        "duplicate_lines": len(lines) - len(counts)
    }
