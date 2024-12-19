def diff(d1, d2):
    keys1 = set(d1.keys())
    keys2 = set(d2.keys())
    all_keys = keys1 | keys2
    result = []
    for key in sorted(all_keys):
        if key in keys1 and key in keys2:
            if d1[key] == d2[key]:
                result.append(
                    {
                        'key': key,
                        'value': d1[key],
                        'status': 'unupdated',
                    },
                )
            elif isinstance(d1[key], dict) and isinstance(d2[key], dict):
                result.append(
                    {
                        'key': key,
                        'status': 'nested',
                        'value': diff(d1[key], d2[key]),
                    },
                )
            else:
                result.append(
                    {
                        'key': key,
                        'status': 'changed',
                        'old_value': d1[key],
                        'new_value': d2[key],
                    },
                )
        elif key in keys2:
            result.append(
                {
                    'key': key,
                    'value': d2[key],
                    'status': 'added',
                },
            )
        else:
            result.append(
                {
                    'key': key,
                    'value': d1[key],
                    'status': 'deleted',
                },
            )
    return result
