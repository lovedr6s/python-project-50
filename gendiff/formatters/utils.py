def normalize_value(value):
    if isinstance(value, bool):
        return str(value).lower()  # True -> "true", False -> "false"
    if value is None:
        return 'null'  # None -> "null"
    if isinstance(value, dict):  # Для [complex value]
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return value

def normalize_value_json(value):
    """Приводит значения к JSON-совместимому формату."""
    if isinstance(value, bool):
        return str(value).lower()
    return value

def normalize_diff(diff):
    """Рекурсивно нормализует diff."""
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