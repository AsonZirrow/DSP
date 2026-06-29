

# extractors/security.py

import os


def analyze_security(file_path):
    return {
        "hidden": os.path.basename(file_path).startswith("."),
        "readable": os.access(file_path, os.R_OK),
        "writable": os.access(file_path, os.W_OK),
        "executable": os.access(file_path, os.X_OK),
    }
