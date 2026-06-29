

from src.content import get_content_analysis, get_checksum

def test_content_analysis(tmp_path):
    file = tmp_path / "sample.txt"
    file.write_text("hello hello world")

    result = get_content_analysis(str(file))

    assert result["total_words"] == 3
    assert result["unique_words"] <= 3
    assert len(result["top_keywords"]) > 0


def test_checksum_changes(tmp_path):
    file1 = tmp_path / "a.txt"
    file2 = tmp_path / "b.txt"

    file1.write_text("data1")
    file2.write_text("data2")

    assert get_checksum(str(file1)) != get_checksum(str(file2))









# import tempfile
# import os

# from src.content import analyze_content


# def test_word_count():
#     with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp:

#         tmp.write("hollo world hello")
#         path = tmp.name

#         result = analyze_content(path)

#         assert result["total_words"] == 3
#         assert result["unique_words"] == 2

#         os.remove(path)

# # with tempfile.NamedTemporaryFile(
# # mode="w",
# # delete=False
# # ) as tmp:

# # ```
# #     tmp.write("hello world hello")
# #     path = tmp.name

# # result = analyze_content(path)

# # assert result["total_words"] == 3
# # assert result["unique_words"] == 2

# # os.remove(path)
