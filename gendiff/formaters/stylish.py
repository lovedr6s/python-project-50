ADDED = "  + "
REMOVED = "  - "
INDENT = "    "

def get_stylish(diff, level=0):
    result = ['{']
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value', None)

        if status == 'added':
            result.append(get_line(level, key, value, ADDED))
        elif status == 'unupdated':
            result.append(get_line(level, key, value, INDENT))
        elif status == 'deleted':
            result.append(get_line(level, key, value, REMOVED))
        elif status == 'changed':
            old_value = node['old_value']
            new_value = node['new_value']
            result.append(get_line(level, key, old_value, REMOVED))
            result.append(get_line(level, key, new_value, ADDED))
        elif status == 'nested':
            nested_value = get_stylish(value, level + 1)
            result.append(f'{INDENT * level}    {key}: {nested_value}')
    
    result.append(f'{INDENT * level}}}')
    return '\n'.join(result)


def get_line(level, key, value, sign):
    formatted_value = format_value(value, level + 1)
    return f'{INDENT * level}{sign}{key}: {formatted_value}'


def format_value(value, level):
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            formatted_val = format_value(val, level + 1)
            lines.append(f'{INDENT * (level + 1)}{key}: {formatted_val}')
        lines.append(f'{INDENT * level}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)