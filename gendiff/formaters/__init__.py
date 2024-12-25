from gendiff.formaters.json import get_json as json
from gendiff.formaters.plain import get_plain as plain
from gendiff.formaters.stylish import get_stylish as stylish


def select_formatter(format_name):
    formatters = {
        'stylish': stylish,
        'plain': plain,
        'json': json,
    }
    if format_name not in formatters:
        raise ValueError(f"Unsupported format: {format_name}")
    return formatters[format_name]


def apply_formatter(content, format_name):
    formatter = select_formatter(format_name)
    return formatter(content)
