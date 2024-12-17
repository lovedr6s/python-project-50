def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return 'null'
    return value


def format_plain(diff, path=""):
    lines = []

    for item in diff:
        property_path = f"{path}.{item['key']}" if path else item['key']

        if item['type'] == 'added':
            lines.append(
                f"Property '{property_path}' was added with value: "
                f"{format_value(item['value'])}"
            )
        elif item['type'] == 'removed':
            lines.append(
                f"Property '{property_path}' was removed"
            )
        elif item['type'] == 'updated':
            lines.append(
                f"Property '{property_path}' was updated. "
                f"From {format_value(item['old_value'])} "
                f"to {format_value(item['new_value'])}"
            )
        elif item['type'] == 'nested':
            lines.append(
                format_plain(item['children'], property_path)
            )

    return '\n'.join(lines)


def plain(diff):
    return format_plain(diff)
