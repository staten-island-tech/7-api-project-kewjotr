import json

def extract(athlete):
    file = requests.get(f"https://www.strava.com/api/v3/{athlete.lower()}")
    data = file.json()
    return