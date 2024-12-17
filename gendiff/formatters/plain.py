from gendiff.formatters.utils import normalize_value

def plain(diff):
    def format_plain(diff, path=""):
        lines = []

        for item in diff:
            property_path = f"{path}.{item['key']}" if path else item['key']

            if item['type'] == 'added':
                lines.append(
                    f"Property '{property_path}' was added with value: "
                    f"{normalize_value(item['value'])}"
                )
            elif item['type'] == 'removed':
                lines.append(f"Property '{property_path}' was removed")
            elif item['type'] == 'updated':
                lines.append(
                    f"Property '{property_path}' was updated. "
                    f"From {normalize_value(item['old_value'])} "
                    f"to {normalize_value(item['new_value'])}"
                )
            elif item['type'] == 'nested':
                lines.append(format_plain(item['children'], property_path))

        return '\n'.join(lines)

    return format_plain(diff)
