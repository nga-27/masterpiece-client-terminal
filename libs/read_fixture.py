import os
import json

def read_fixture():
    if not os.path.exists("fixture.json"):
        print("ERROR: No fixture found!")
        return {}
    
    data = {}
    with open("fixture.json", 'r') as fixture:
        data = json.load(fixture)
        fixture.close()
    return data