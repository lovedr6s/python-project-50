import json

import yaml


def parse_content(data, file_format):
    file_format = file_format.lower()
    match file_format:
        case 'yaml' | 'yml':
            return yaml.safe_load(data)
        case 'json':
            return json.loads(data)
        case _:
            raise ValueError(f"Unsupported format: {file_format}")
