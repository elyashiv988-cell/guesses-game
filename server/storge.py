import json

def save_game(data):
    saved_data = stored_data()
    for user in saved_data:
        if user["username"]== data["username"]:
            saved_data.remove(user)
    saved_data.append(data)
    with open("db_saving_gams.json","w") as file:
        json.dump(saved_data, file, indent=4)

def stored_data():
    
    try:
        with open("db_saving_gams.json","r") as file:
            data = json.load(file)
            return data
        
    except FileNotFoundError:
        return []

def find_corrent_username(username):
    for user in stored_data():
        if username == user["username"]:
            return user
    return []

def default_saved_game():
    return {
        "target": None,
        "attempts": 0,
        "history": [],
        "isActive": False
    }

