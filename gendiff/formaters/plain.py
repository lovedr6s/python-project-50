
def get_plain(diff, path=''):
    result = []
    for node in diff:
        name = f'{path}{node["key"]}'
        if node['status'] == 'added':
            value = select_type(node['value'])
            result.append(f"Property '{name}' was added with value: {value}")
        elif node['status'] == 'deleted':
            result.append(f"Property '{name}' was removed")
        elif node['status'] == 'changed':
            old_value = select_type(node['old_value'])
            new_value = select_type(node['new_value'])
            result.append(
                f"Property '{name}' was updated. From {old_value} "
                f"to {new_value}"
                )
        elif node['status'] == 'nested':
            nested_result = get_plain(node["value"], path=name + ".")
            result.append(nested_result)
    final_result = '\n'.join(result)
    return final_result


def select_type(node):
    if isinstance(node, str):
        return f"'{node}'"
    elif isinstance(node, dict) or isinstance(node, list):
        return "[complex value]"
    elif isinstance(node, bool):
        return str(node).lower()
    elif node is None:
        return 'null'
    else:
        return node
