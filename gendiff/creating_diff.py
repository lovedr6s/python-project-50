from gendiff.base_diff import diff
from gendiff.formaters import select_formater
from gendiff.parse import parse_files


def generate_diff(dict1, dict2, format_name='stylish'):
    '''generates a diff with two prepared files and the selected format.'''
    file1 = parse_files(dict1)
    file2 = parse_files(dict2)
    dif = diff(file1, file2)
    formater = select_formater(format_name)
    return formater(dif)
