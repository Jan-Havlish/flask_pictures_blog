import json


def try_to_load_json(JSON,
                     error_mes):  # because when showed picture which does not have a record in the db return False
    """Try to load JSON, Except - return error message."""
    true_json = {}
    try:
        true_json = json.loads(JSON)
    except TypeError:
        true_json = {"text": error_mes}
    return true_json
