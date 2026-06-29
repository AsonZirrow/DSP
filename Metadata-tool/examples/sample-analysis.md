



# Sample Analysis

## Example Input

The toolkit was executed against a Python source file:

```text
main.py
```

The user provides a file path and the analysis engine processes the file through all registered analyzers.

---

## Analysis Workflow

```text
User
  ↓
main.py
  ↓
FileAnalyzer Core
  ↓
Metadata Analyzer
Content Analyzer
Structure Analyzer
Security Analyzer
Checksum Analyzer
  ↓
Formatter
  ↓
Structured Report
```

---

## Example Output

### Metadata

```text
name: main.py
type: .py
size: 10826
is_file: True
is_dir: False
```

The metadata analyzer extracts file-system information such as file type, size, location, timestamps, permissions, and ownership attributes.

---

### Content Analysis

```text
total_words: 1129
unique_words: 378
```

The content analyzer examines the file contents and produces statistics including:

* total word count
* unique word count
* keyword frequency
* content preview

Example keywords:

```text
('#', 328)
('=', 49)
(':', 21)
('import', 15)
('def', 13)
```

---

### Structure Analysis

```text
total_lines: 428
unique_lines: 255
duplicate_lines: 173
```

The structure analyzer examines organizational characteristics of the file and identifies repeated content.

---

### Security Analysis

```text
hidden: False
readable: True
writable: True
executable: True
```

The security analyzer reports basic file access characteristics and visibility information.

---

### Checksum

```text
822d0c665d9d65e023c65840dc07aac5
```

A checksum is generated to support file integrity verification and change detection.

---

## Summary

The toolkit combines multiple analyzers into a single report, transforming raw file data into structured information that can be inspected, compared, or processed by other systems.
