import pytest
from gendiff import generate_diff

file1 = 'tests/fixtures/nested_file1.yml'
file2 = 'tests/fixtures/nested_file2.yml'
file3 = 'tests/fixtures/flat_file1.json'
file4 = 'tests/fixtures/flat_file2.json'
file5 = 'tests/fixtures/file3.yml'
file6 = 'tests/fixtures/file4.yml'
file7 = 'tests/fixtures/file1.json'
file8 = 'tests/fixtures/file2.json'

nested_yml_stylish = 'tests/fixtures/nested_yml_result.txt'
nested_yml_plain = 'tests/fixtures/nested_yml_result_plain.txt'
nested_yml_json = 'tests/fixtures/nested_yml_result_json.txt'
flat_json_stylish = 'tests/fixtures/result_flat.txt'
flat_yaml_plain = 'tests/fixtures/flat_json_result.txt'


@pytest.mark.parametrize(
    "filepath1, filepath2, formater, diff", 
        [
        (file1, file2, 'stylish', nested_yml_stylish), 
        (file1, file2, 'plain', nested_yml_plain),
        (file7, file8, 'json', nested_yml_json),
        (file3, file4, 'stylish', flat_json_stylish),
        (file5, file6, 'plain', flat_yaml_plain),
        (file3, file4, 'plain', flat_yaml_plain),
        ]
    )
def test_generate_diff(filepath1, filepath2, formater, diff):
    '''tests function generate_diff with different files.'''
    result = generate_diff(filepath1, filepath2, formater)
    for lines in open(diff):
        list_of_lines = []
        if lines in diff:
            merge_lines = list_of_lines.append(lines)
            expected_result = ' '.join(merge_lines)
            assert result == expected_result



