from gendiff.base_diff import build_diff_tree
from gendiff.formaters import apply_formatter
from gendiff.parse import get_content


def generate_diff(file_path1, file_path2, format_name='stylish'):
    parsed_data1 = get_content(file_path1)
    parsed_data2 = get_content(file_path2)
    dif = build_diff_tree(parsed_data1, parsed_data2)
    return apply_formatter(dif, format_name)
