import json

def extract(sort,item):
    file = requests.get(f"https://www.strava.com/api/v3/{sort.lower()}/{item.lower()}")
    data = file.json()
    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [t["type"]["name"] for t in data["types"]]
    }