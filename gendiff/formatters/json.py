import json
from gendiff.formatters.utils import normalize_diff


def json_format(diff):
    normalized_diff = normalize_diff(diff)
    return json.dumps(normalized_diff, indent=4)