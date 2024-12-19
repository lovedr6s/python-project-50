def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return value


def normalize_stylish_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"{value}"
    return value 


def normalize_value_json(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return value


def normalize_diff(diff):
    result = []
    for item in diff:
        normalized_item = {
            "key": item["key"],
            "type": item["type"],
            "value": normalize_value_json(item.get("value")),
            "old_value": normalize_value_json(item.get("old_value")),
            "new_value": normalize_value_json(item.get("new_value"))
        }
        if "children" in item:
            normalized_item["children"] = normalize_diff(item["children"])
        result.append(normalized_item)
    return result
