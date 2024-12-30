import os

from gendiff.base_diff import build_diff_tree
from gendiff.formaters import apply_formatter
from gendiff.parse import parse_content


def generate_diff(file_path1, file_path2, format_name='stylish'):
    parsed_data1 = get_content(file_path1)
    parsed_data2 = get_content(file_path2)
    dif = build_diff_tree(parsed_data1, parsed_data2)
    return apply_formatter(dif, format_name)


def get_file_extention(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension.lower()[1:]


def get_content(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    return parse_content(file_content, get_file_extention(file_path))
