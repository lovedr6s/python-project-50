
def get_plain(diff, path=''):
    result = []
    for node in diff:
        name = f'{path}{node["key"]}'
        if node['status'] == 'added':
            result.append(f"Property '{name}' was added with value: {select_type(node['value'])}")  # noqa: E501
        elif node['status'] == 'deleted':
            result.append(f"Property '{name}' was removed")
        elif node['status'] == 'changed':
            result.append(f"Property '{name}' was updated. From {select_type(node['old_value'])} to {select_type(node['new_value'])}")  # noqa: E501
        elif node['status'] == 'nested':
            result.append(f'{get_plain(node["value"], path=name + ".")}')
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
