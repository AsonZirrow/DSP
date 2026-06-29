

from src.structure import analyze_structure

def test_structure_analysis(tmp_path):
    file = tmp_path / "sample.py"
    file.write_text("a = 1\na = 1\nb = 2\n")

    result = analyze_structure(str(file))

    assert result["total_lines"] == 3
    assert result["duplicate_lines"] >= 1
    assert result["unique_lines"] <= 3