import requests

BASE_URL = "http://127.0.0.1:8000/"

def ping_server():
    req = requests.get(BASE_URL)
    print(f"Ping Masterpiece Server: {req.json()}")

def start_new_game():
    req = requests.post(BASE_URL + "new_game")
    print(f"Start new game: {req.json()['value']}\r\n")

def fetch_characters():
    req = requests.get(BASE_URL + "user/characters")
    return req.json()

##############################

def post_item(endpoint, content: dict):
    req = requests.post(BASE_URL+f"{endpoint}", json=content)
    return req.json(), req.status_code