from gendiff.formatters.utils import normalize_stylish_value


def format_stylish(diff, depth=0):
    indent = ' ' * (depth * 4)
    lines = []

    for item in diff:
        key = item['key']
        match item['type']:
            case 'nested':
                children = format_stylish(item['children'], depth + 1)
                lines.append(f"{indent}  {key}: {{\n{children}\n{indent}  }}")
            case 'added':
                lines.append(f"{indent}  + {key}: {normalize_stylish_value(item['value'])}")
            case 'removed':
                lines.append(f"{indent}  - {key}: {normalize_stylish_value(item['value'])}")
            case 'updated':
                lines.append(f"{indent}  - {key}: {normalize_stylish_value(item['old_value'])}")
                lines.append(f"{indent}  + {key}: {normalize_stylish_value(item['new_value'])}")
            case 'unchanged':
                lines.append(f"{indent}    {key}: {normalize_stylish_value(item['value'])}")

    return '\n'.join(lines)
#

def stylish(diff):
    return '{\n' + format_stylish(diff) + '\n}'
