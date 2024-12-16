from pathlib import Path
import json
from gendiff.generate_diff import generate_diff


FIXTURES_PATH = Path("tests/fixtures")


def read_file(filepath):
    """Утилита для чтения содержимого файла."""
    with open(filepath, 'r') as file:
        return file.read().strip()


def test_json_stylish():
    file1 = str(FIXTURES_PATH / "flat_file1.json")
    file2 = str(FIXTURES_PATH / "flat_file2.json")
    expected_output = read_file(FIXTURES_PATH / "expected_stylish_json.txt")

    diff = generate_diff(file1, file2, format_name='stylish')
    assert diff == expected_output


def test_json_plain():
    file1 = str(FIXTURES_PATH / "flat_file1.json")
    file2 = str(FIXTURES_PATH / "flat_file2.json")
    expected_output = read_file(FIXTURES_PATH / "expected_plain_json.txt")

    diff = generate_diff(file1, file2, format_name='plain')
    assert diff == expected_output


def test_json_json():
    file1 = str(FIXTURES_PATH / "flat_file1.json")
    file2 = str(FIXTURES_PATH / "flat_file2.json")
    expected_output = read_file(FIXTURES_PATH / "expected_json_json.json")

    diff = generate_diff(file1, file2, format_name='json')
    assert diff == expected_output

def test_yaml_stylish():
    file1 = str(FIXTURES_PATH / "file1.yml")
    file2 = str(FIXTURES_PATH / "file2.yml")
    expected_output = read_file(FIXTURES_PATH / "expected_stylish_yaml.txt")

    result = generate_diff(file1, file2, format_name="stylish")
    assert result == expected_output

def test_yaml_json():
    file1 = str(FIXTURES_PATH / "file1.yml")
    file2 = str(FIXTURES_PATH / "file2.yml")
    expected_output = read_file(FIXTURES_PATH / "expected_json_yaml.json")

    result = generate_diff(file1, file2, format_name="json")
    
    result_json = json.loads(result)
    expected_json = json.loads(expected_output)
    
    assert result_json == expected_json

def test_yaml_plain():
    file1 = str(FIXTURES_PATH / "file1.yml")
    file2 = str(FIXTURES_PATH / "file2.yml")
    expected_output = read_file(FIXTURES_PATH / "expected_plain_yaml.txt")

    result = generate_diff(file1, file2, format_name="plain")
    assert result == expected_output