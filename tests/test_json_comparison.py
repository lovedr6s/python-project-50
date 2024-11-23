import json
from pathlib import Path

def test_compare_flat_json():
    file1 = Path("tests/fixtures/file1.json")
    file2 = Path("tests/fixtures/file2.json")

    with file1.open() as f1, file2.open() as f2:
        json1 = json.load(f1)
        json2 = json.load(f2)

    assert json1 != json2
