def get_stylish(diff, level=0):
    result = ['{']
    for node in diff:
        key = node['key']
        status = node['status']
        value = node.get('value', None)

        if status == 'added':
            result.append(get_line(level, key, value, '  + '))
        elif status == 'unupdated':
            result.append(get_line(level, key, value, '    '))
        elif status == 'deleted':
            result.append(get_line(level, key, value, '  - '))
        elif status == 'changed':
            old_value = node['old_value']
            new_value = node['new_value']
            result.append(get_line(level, key, old_value, '  - '))
            result.append(get_line(level, key, new_value, '  + '))
        elif status == 'nested':
            nested_value = get_stylish(value, level + 1)
            result.append(f'{"    " * level}    {key}: {nested_value}')
    
    result.append(f'{"    " * level}}}')
    return '\n'.join(result)


def get_line(level, key, value, sign):
    formatted_value = format_value(value, level + 1)
    return f'{"    " * level}{sign}{key}: {formatted_value}'


def format_value(value, level):
    if isinstance(value, dict):
        lines = ['{']
        for key, val in value.items():
            formatted_val = format_value(val, level + 1)
            lines.append(f'{"    " * (level)}{key}: {formatted_val}')
        lines.append(f'{"    " * (level - 1)}}}')
        return '\n'.join(lines)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)