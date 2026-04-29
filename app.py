import json
import requests

def extract(sort,item):
    file = requests.get(f"https://www.pokeapi.co/api/v2/{sort.lower()}/{item.lower()}")
    data = file.json()
    return {
        "name": data["name"],
        "id": data["id"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }
take = input()
out = extract("pokemon",take)
print(out)