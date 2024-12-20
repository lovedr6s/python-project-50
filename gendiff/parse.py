import json
import os

import yaml


def parse(content, format):
    format = format.lower()
    if format in ['yaml', 'yml']:
        return yaml.safe_load(content)
    elif format == 'json':
        return json.loads(content)
    else:
        raise Exception(f"Unsupported format: {format}")


def parse_file(path):
    with open(path, 'r') as file:
        content = file.read()
    
    _, extension = os.path.splitext(path)
    extension = extension.lower()[1:]
    return parse(content, extension)