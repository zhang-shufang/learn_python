from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_dict = json.loads(contents)
        return user_dict
    else:
        return None

def get_new_user_info(path, info={
        'name': '',
        'age': '',
        'sex': ''}):
    """Prompt for a new user info."""
    user_dict = {}
    for key in info.keys():
        user_dict[key] = input(f"Please enter your {key}: ")
    contents = json.dumps(user_dict)
    path.write_text(contents)
    return user_dict

def greet_user():
    """Greet the user by name."""
    path = Path('user_dict2.json')
    user_dict = get_stored_user_info(path)
    if user_dict:
        print(f"Welcome back, {user_dict['name']}!")
    else:
        user_dict = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_dict['name']}!")

greet_user()