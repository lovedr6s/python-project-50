from gendiff.base_diff import diff
from gendiff.formaters import apply_formatter
from gendiff.parse import parse_file


def generate_diff(dict1, dict2, format_name='stylish'):
    file1 = parse_file(dict1)
    file2 = parse_file(dict2)
    dif = diff(file1, file2)
    return apply_formatter(dif, format_name)
