import pytest
from gendiff import generate_diff

FIXTURE_PATH = "tests/fixtures/"


@pytest.mark.parametrize(
    "filepath1, filepath2, formater, diff", 
    [
        ('nested_file1.yml', 'nested_file2.yml', 'stylish', 'nested_yml_result.txt'),
        ('nested_file1.yml', 'nested_file2.yml', 'plain', 'nested_yml_result_plain.txt'),
        ('file1.json', 'file2.json', 'json', 'nested_yml_result_json.txt'),
        ('flat_file1.json', 'flat_file2.json', 'stylish', 'result_flat.txt'),
        ('file3.yml', 'file4.yml', 'plain', 'flat_json_result.txt'),
        ('flat_file1.json', 'flat_file2.json', 'plain', 'flat_json_result.txt'),
    ]
)


def test_generate_diff(filepath1, filepath2, formater, diff):
    # Добавляем BASE_PATH к каждому файлу
    filepath1 = f"{FIXTURE_PATH}/{filepath1}"
    filepath2 = f"{FIXTURE_PATH}/{filepath2}"
    diff = f"{FIXTURE_PATH}/{diff}"
    
    result = generate_diff(filepath1, filepath2, formater)
    
    with open(diff, 'r') as file:
        expected_result = file.read()
    assert result.strip() == expected_result.strip()