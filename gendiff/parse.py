import os
import json
import yaml


def parse_files(path):
    with open(path) as file:
        read_file = file.read()
        _, split_path = os.path.splitext(path)
        split_path = split_path.lower()
        if split_path in ['.yaml', '.yml']:
            return yaml.safe_load(read_file)
        elif split_path == '.json':
            return json.loads(read_file)
        else:
            raise Exception('Wong type of files')
