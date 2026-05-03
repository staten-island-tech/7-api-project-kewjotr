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
                "postal": data["address"]["postalCode"],
                "address": data["address"]["streetAddress"]
            }
        elif category == "alerts":
            if specific == "active":
                for activealerts in data["features"]:
                    return {
                        "event": data["features"][activealerts]["properties"]["event"],
                        "office": data["features"][activealerts]["properties"]["senderName"],
                        "category": data["features"][activealerts]["properties"]["severity"],
                        "certainty": data["features"][activealerts]["properties"]["certainty"],
                        "urgency": data["features"][activealerts]["properties"]["urgency"]
                    }
            elif specific == "types":
                return data["eventTypes"]
            else:
                return "Invalid statement."
        elif (category == "aviation") and (specific == "sigmets"):
            for aircraft in data["features"]:
                return {
                    "aircrafts": data["features"][aircraftindex]["properties"]["sequence"]
                }
        elif category == "stations":
            return {
                "name": data["properties"]["name"],
                "elevation": data["properties"]["elevation"]["value"],
                "timezone": data["properties"]["timeZone"]
            }
        elif category == "radar":
            if specific == "servers":
                for radarserversindex in data["@graph"]["ping"]["targets"]["radar"]:
                    return data["@graph"]["ping"]["targets"]["radar"][radarserversindex]
            elif specific == "stations":
                for radarstationsindex in data["features"]:
                    return {
                        "id": data["features"][radarstationsindex]["properties"]["id"],
                        "name": data["features"][radarstationsindex]["properties"]["name"],
                        "type": data["features"][radarstationsindex]["properties"]["stationType"]
                    }
            else:
                return "Invalid Statement."
        elif category == "products":
            if specific == "locations":
                for key in data["locations"]:
                    if data["locations"][key] == null:
                        del data["locations"][key]
                    else:
                        return data["locations"][key]
            elif specific == "types":
                for producttypes in data["@graph"]:
                    return {
                        "code": data["@graph"][producttypes]["productCode"],
                        "name": data["@graph"][producttypes]["productName"]
                    }
            else:
                return "Invalid Statement."
        else:
            return "Invalid Statement."
    else:
        if category == "glossary":
            for glossaryindex in data["glossary"]:
                return {
                    "term": data["glossary"][glossaryindex]["term"],
                    "definition": data["glossary"][glossaryindex]["definition"]
                }
        elif category == "alerts":
            for expiredalerts in data["features"]:
                return {
                    "event": data["features"][expiredalerts]["properties"]["event"],
                    "office": data["features"][expiredalerts]["properties"]["senderName"],
                    "category": data["features"][expiredalerts]["properties"]["severity"],
                    "certainty": data["features"][expiredalerts]["properties"]["certainty"],
                    "urgency": data["features"][expiredalerts]["properties"]["urgency"]
                }
        elif category == "stations":
            for stationsindex in data["features"]:
                return {
                    "station": data["features"][stationsindex]["properties"]["stationIdentifier"],
                    "name": data["features"][stationsindex]["properties"]["name"],
                    "provider": data["features"][stationsindex]["properties"]["provider"]
                }
        elif category == "products":
            for productsindex in data["@graph"]:
                return {
                    "ID": data["@graph"][productsindex]["wmoCollectiveId"],
                    "Office": data["@graph"][productsindex]["issuingOffice"],
                    "Code": data["@graph"][productsindex]["productCode"]
                }
        elif category == "zones":
            for zoneindex in data["features"]:
                return {
                    "id": data["features"][zoneindex]["properties"]["id"],
                    "county": data["features"][zoneindex]["properties"]["name"],
                    "state": data["features"][zoneindex]["properties"]["state"],
                    "type": data["features"][zoneindex]["properties"]["types"]
                }
        else:
            return "Invalid statement."


list = ["Alerts", "Aviation", "Glossary", "Stations", "Offices", "Radar", "Products", "Zones"]
print("Available Categories:""\n", list)

category1 = ("View category""\n")
while (category1 != "end") or (category1 != "exit"):
    sort = input("Choose item to view")
    if category1 in list:
        finish = extract(category1,sort)
        print(finish)
        category1 = ("View category""\n")
    else:
        print("Invalid statement. Please try again.")
        category1 = ("View category""\n")
exit()
