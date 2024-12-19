def get_stylish(diff, level=0):
    result = []
    for node in diff:
        if node['status'] == 'added':
            result.append(get_lines(level, node, '  + ', inner))
        elif node['status'] == 'unupdated':
            result.append(get_lines(level, node, '    ', inner))
        elif node['status'] == 'deleted':
            result.append(get_lines(level, node, '  - ', inner))
        elif node['status'] == 'changed':
            node['value'] = node['old_value']
            result.append(get_lines(level, node, '  - ', inner))
            node['value'] = node['new_value']
            result.append(get_lines(level, node, '  + ', inner))
        else:
            result.append(get_lines(level + 1, node, '', get_stylish))
    result.append(f'{"    " * level}{"}"}')
    level -= 1
    final_result = '\n'.join(result)
    return f'{"{"}\n{final_result}'


def get_lines(level, string, sign, func):
    line = ''
    line += f'{"    " * level + sign}{string["key"]}: '
    line += f'{func(string["value"], level)}'
    return line


def inner(node, level):
    container = ''
    if isinstance(node, list):
        new_node = get_stylish(node, level + 1)
        return str(new_node)
    if isinstance(node, dict):
        level += 1
        for key, value in node.items():
            new_value = inner(value, level)
            container += f'\n    {"    " * level}{key}: {new_value}'
        return '{' + container + '\n' + '    ' * level + '}'
    if isinstance(node, bool):
        return str(node).lower()
    if node is None:
        node = 'null'
        return node
    else:
        return node
