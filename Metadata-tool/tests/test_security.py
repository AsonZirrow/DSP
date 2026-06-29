

from src.security import analyze_security

def test_security_flags(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("data")

    result = analyze_security(str(file))

    assert isinstance(result["hidden"], bool)
    assert isinstance(result["readable"], bool)
    assert isinstance(result["writable"], bool)
    assert isinstance(result["executable"], bool)
