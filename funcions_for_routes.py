import json, os
def try_to_load_json(JSON, error_mes): #because when showed picture which does not have a record in the db return False
    """Try to load JSON, Except - return error message."""
    true_json = {}
    try: true_json = json.loads(JSON)
    except TypeError: true_json = {"text": error_mes}
    return true_json

def find_current_dir():
    """Found where is script running."""
    return os.path.dirname(os.path.abspath(__file__))

def return_dir_of_pictures():
    """Returns directory of pictures."""
    return os.path.join(find_current_dir(), 'static', 'pic')