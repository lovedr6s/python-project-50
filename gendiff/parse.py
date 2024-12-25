import json
import os

import yaml


def parse_content(data, file_format):
    file_format = file_format.lower()
    if file_format in ['yaml', 'yml']:
        return yaml.safe_load(data)
    elif file_format == 'json':
        return json.loads(data)
    else:
        raise Exception(f"Unsupported format: {file_format}")


def get_content(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
    _, file_extension = os.path.splitext(file_path)
    file_extension = file_extension.lower()[1:]
    return parse_content(file_content, file_extension)
