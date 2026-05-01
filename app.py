import requests
import tkinter as tk

def extract(category,specific):
    if specific:
        response = requests.get(f"https://api.weather.gov/{category}/{specific}")
    else:
        response = requests.get(f"https://api.weather.gov/{category}")
        
    data = response.json
    if specific:
        if (category == "offices"):
            return {
                "id": data["id"],
                "name": data["name"],
                "telephone": data["telephone"],
                "postal": data["postalCode"],
                "address": data["streetAddress"]
            }
        elif (category == "alerts") and (specific == "active"):
            return

print("Available Categories""\n""Alerts, Aviation, Glossary, Stations, Offices, Radar, Points, Products, Zones")
category1 = ("View category""\n")
while category1 != "end":
    sort = input("Choose item to view")
    finish = extract(category1,sort)
    print(finish)
    
exit()