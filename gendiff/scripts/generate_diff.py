import json
import yaml
from gendiff.scripts.diff_builder import build_diff
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_formatter


def parse_file(filepath):
    with open(filepath, 'r') as file:
        if filepath.endswith('.json'):
            return json.load(file)
        elif filepath.endswith(('.yml', '.yaml')):
            return yaml.safe_load(file)
        else:
            raise ValueError("Unsupported file format")


def generate_diff(file_path1, file_path2, format_name='stylish'):
    data1 = parse_file(file_path1)
    data2 = parse_file(file_path2)
    diff = build_diff(data1, data2)

    if format_name == 'stylish':
        return stylish(diff)
    elif format_name == 'plain':
        return plain(diff)
    elif format_name == "json":
        return json_format(diff)
    else:
        raise ValueError(f"Unsupported format: {format_name}")
