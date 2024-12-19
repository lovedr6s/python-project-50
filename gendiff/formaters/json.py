import json


def get_json(diff):
    '''stylizes diff.'''
    return json.dumps(diff, indent=4)
