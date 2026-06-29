

# core.py

class FileAnalyzer:
    def __init__(self):
        self.sections = []

    def register(self, name, func):
        """Register analysis modules dynamically"""
        self.sections.append((name, func))

    def analyze(self, file_path):
        results = {}

        for name, func in self.sections:
            try:
                results[name] = func(file_path)
            except Exception as e:
                results[name] = {"error": str(e)}

        return results