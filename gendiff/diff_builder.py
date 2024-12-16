def build_diff(data1, data2):
    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data2:
            diff.append({'key': key, 'type': 'removed', 'value': data1[key]})
        elif key not in data1:
            diff.append({'key': key, 'type': 'added', 'value': data2[key]})
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            diff.append({
                        'key': key,
                        'type': 'nested',
                        'children': build_diff(data1[key], data2[key])
                        })
        elif data1[key] == data2[key]:
            diff.append({'key': key, 'type': 'unchanged', 'value': data1[key]})
        else:
            diff.append({
                        'key': key,
                        'type': 'updated',
                        'old_value': data1[key],
                        'new_value': data2[key]
                        })
    return diff
