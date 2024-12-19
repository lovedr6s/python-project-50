from gendiff.formaters.json import get_json as json
from gendiff.formaters.plain import get_plain as plain
from gendiff.formaters.stylish import get_stylish as stylish


def select_formater(format_name):
    '''select formater for generate_diff function'''
    if format_name == 'stylish':
        return stylish
    elif format_name == 'plain':
        return plain
    elif format_name == 'json':
        return json
    else:
        raise Exception('wrong format!')
