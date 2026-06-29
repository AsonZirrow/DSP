

# main.py

from core import FileAnalyzer

from metadata import get_metadata
from content import get_content_analysis, get_checksum
from structure import analyze_structure
from security import analyze_security

from formatter import print_report


file_path = r"C:\Users\Godmylord\Desktop\TESTDOM\main.py"


analyzer = FileAnalyzer()

# REGISTER MODULES (THIS IS THE MAGIC)
analyzer.register("metadata", get_metadata)
analyzer.register("content", get_content_analysis)
analyzer.register("structure", analyze_structure)
analyzer.register("security", analyze_security)

# extra computed section
analyzer.register("checksum", get_checksum)


# RUN ANALYSIS
results = analyzer.analyze(file_path)

# PRINT CLEAN REPORT
print_report(results)