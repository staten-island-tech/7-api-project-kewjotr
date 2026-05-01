import requests
import tkinter as tk

def extract(category,specific):
    if specific:
        response = requests.get(f"https://api.weather.gov/{category}/{specific}")
    else:
        response = requests.get(f"https://api.weather.gov/{category}")
        
    data = response.json
    if specific:
        if category == "offices":
            return {
                "id": data["id"],
                "name": data["name"],
                "telephone": data["telephone"],
                "postal": data["postalCode"],
                "address": data["streetAddress"]
            }