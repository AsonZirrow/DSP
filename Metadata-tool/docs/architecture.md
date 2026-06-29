

# Architecture

## Overview

The Metadata Extraction Toolkit is organized as a modular analysis pipeline.

Rather than embedding all analysis logic into a single script, the system separates responsibilities into specialized components that cooperate through a central orchestration layer.

The architecture is designed to support maintainability, extensibility, and independent development of analysis capabilities.

---

## High-Level Flow

```text
User
  ↓
main.py
  ↓
FileAnalyzer Core
  ↓
Registered Analysis Modules
  ├── metadata.py
  ├── content.py
  ├── structure.py
  └── security.py
  ↓
Unified Results
  ↓
formatter.py
  ↓
Structured Report
```

---

## Core Components

### main.py

The entry point of the application.

Responsibilities:

* Accept user input
* Select files for analysis
* Initialize the analysis engine
* Trigger execution
* Display results

The main module does not perform analysis itself.

---

### core.py

The orchestration engine of the toolkit.

Responsibilities:

* Register analysis modules
* Coordinate execution
* Aggregate results
* Maintain a unified analysis workflow

The core engine acts as the central controller that connects independent analyzers.

---

### metadata.py

Responsible for file-system and operating-system metadata.

Examples include:

* file name
* file size
* file type
* timestamps
* path information

---

### content.py

Responsible for content-level analysis.

Examples include:

* word counts
* keyword frequency
* previews
* checksums

---

### structure.py

Responsible for structural characteristics.

Examples include:

* line counts
* duplicate lines
* repeated content
* structural patterns

---

### security.py

Responsible for security-related attributes.

Examples include:

* permissions
* access flags
* executable status
* ownership information

---

### formatter.py

Responsible for presentation.

Responsibilities:

* organize output
* group related information
* create consistent reports
* separate analysis from display logic

---

## Architectural Principles

The architecture is based on:

* Separation of concerns
* Modular analysis components
* Explicit responsibilities
* Extensibility through composition
* Reusable functionality

Each module focuses on a single responsibility while the core engine coordinates overall execution.

---

## Result

The final result is a modular analysis framework that transforms raw files into structured information through independent, reusable analysis components.
