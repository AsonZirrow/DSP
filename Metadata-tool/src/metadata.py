

# extractors/metadata.py

import os
import datetime
import psutil
import hashlib


def get_metadata(file_path):
    stat = os.stat(file_path)

    return {
        "name": os.path.basename(file_path),
        "type": os.path.splitext(file_path)[1],
        "size": stat.st_size,
        "path": os.path.abspath(file_path),
        "location": os.path.dirname(file_path),

        "created": datetime.datetime.fromtimestamp(stat.st_ctime).isoformat(),
        "modified": datetime.datetime.fromtimestamp(stat.st_mtime).isoformat(),
        "accessed": datetime.datetime.fromtimestamp(stat.st_atime).isoformat(),

        "user_id": psutil.Process().uids().real if hasattr(psutil.Process(), "uids") else None,
        "group_id": stat.st_gid,
        "permissions": stat.st_mode,
        "links": stat.st_nlink,

        "is_file": os.path.isfile(file_path),
        "is_dir": os.path.isdir(file_path),
    }