def build_diff_tree(dict1, dict2):
    keys_old = set(dict1.keys())
    keys_new = set(dict2.keys())
    combined_keys = keys_old | keys_new
    diff_result = []

    for current_key in sorted(combined_keys):
        if current_key in keys_old and current_key in keys_new:
            if dict1[current_key] == dict2[current_key]:
                diff_result.append(
                    {
                        'key': current_key,
                        'value': dict1[current_key],
                        'status': 'unupdated',
                    },
                )
            elif isinstance(dict1[current_key], dict) and isinstance(dict2[current_key], dict):
                diff_result.append(
                    {
                        'key': current_key,
                        'status': 'nested',
                        'value': build_diff_tree(dict1[current_key], dict2[current_key]),
                    },
                )
            else:
                diff_result.append(
                    {
                        'key': current_key,
                        'status': 'changed',
                        'old_value': dict1[current_key],
                        'new_value': dict2[current_key],
                    },
                )
        elif current_key in keys_new:
            diff_result.append(
                {
                    'key': current_key,
                    'value': dict2[current_key],
                    'status': 'added',
                },
            )
        else:
            diff_result.append(
                {
                    'key': current_key,
                    'value': dict1[current_key],
                    'status': 'deleted',
                },
            )
    return diff_result
