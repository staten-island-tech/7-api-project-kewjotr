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
            for alertfinder in data["features"]:
                return {
                    "event": data["features"]["properties"]["event"],
                    "office": data["features"]["properties"]["senderName"],
                    "category": data["features"]["properties"]["severity"],
                    "certainty": data["features"]["properties"]["certainty"],
                    "urgency": data["features"]["properties"]["urgency"]
                }

avail = ["Alerts", "Aviation", "Glossary", "Stations", "Offices", "Radar", "Points", "Products", "Zones"]
print("Available Categories""\n", avail)
category1 = ("View category""\n")
while (category1 != "end") or (category1 != "exit"):
    sort = input("Choose item to view")
    finish = extract(category1,sort)
    print(finish)
    category1 = ("View category""\n")
exit()
