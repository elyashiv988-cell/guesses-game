import requests
from creds import create_username, create_password

base_url = "http://127.0.0.1:8000"

def signin(username, password):

    response = requests.post(f"{base_url}/api/login", json={"username": username, "password": password})
    return response.status_code, response.json()

def start_game(usrename: str, resume: bool):
    response = requests.get(f"{base_url}/api/game/start", params= {"username": usrename, "resume": resume})
    return response.status_code, response.json()



def geussing_app(username, guess):

    
    response = requests.post(f"{base_url}/api/game/guess", params={"guess": guess, "username": username})
    return response.status_code, response.json()


def exit_game(username, save):

    response = requests.post(f"{base_url}/api/game/exit", params={"username": username, "save": save})
    return response.status_code, response.json()