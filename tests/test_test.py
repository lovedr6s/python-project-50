import pytest
from gendiff import generate_diff

BASE_PATH = "tests/fixtures/"


@pytest.mark.parametrize(
    "filepath1, filepath2, formater, diff", 
    [
        (
            f'{BASE_PATH}nested_file1.yml',
            f'{BASE_PATH}nested_file2.yml',
            'stylish',
            f'{BASE_PATH}nested_yml_result.txt'
        ),
        (
            f'{BASE_PATH}nested_file1.yml',
            f'{BASE_PATH}nested_file2.yml',
            'plain',
            f'{BASE_PATH}nested_yml_result_plain.txt'
        ),
        (
            f'{BASE_PATH}file1.json',
            f'{BASE_PATH}file2.json',
            'json',
            f'{BASE_PATH}nested_yml_result_json.txt'
        ),
        (
            f'{BASE_PATH}flat_file1.json',
            f'{BASE_PATH}flat_file2.json',
            'stylish',
            f'{BASE_PATH}result_flat.txt'
        ),
        (
            f'{BASE_PATH}file3.yml',
            f'{BASE_PATH}file4.yml',
            'plain',
            f'{BASE_PATH}flat_json_result.txt'
        ),
        (
            f'{BASE_PATH}flat_file1.json',
            f'{BASE_PATH}flat_file2.json',
            'plain',
            f'{BASE_PATH}flat_json_result.txt'
        ),
    ]
)
def test_generate_diff(filepath1, filepath2, formater, diff):
    result = generate_diff(filepath1, filepath2, formater)
    with open(diff, 'r') as file:
        expected_result = file.read()
    print("Result:")
    print(result)
    print("Expected:")
    print(expected_result)
    assert result.strip() == expected_result.strip()
