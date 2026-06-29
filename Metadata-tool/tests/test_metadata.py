

from src.metadata import get_metadata

def test_metadata_basic_fields(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello world")

    result = get_metadata(str(file))

    assert "name" in result
    assert result["name"] == "sample.txt"
    assert result["is_file"] is True
    assert result["is_dir"] is False
    assert result["size"] > 0










# import tempfile
# import os

# from src.metadata import get_metadata


# def test_metadata_returns_basic_fields():
#     with tempfile.NamedTemporaryFile(delete=False) as tmp:
#         path = tmp.name

#     result = get_metadata(path)

#     assert result["name"]
#     assert result["size"] >= 0
#     assert result["is_file"] is True

#     os.remove(path)


# if __name__ == "__main__":
#     test_metadata_returns_basic_fields()
#     print("test_metadata passed")