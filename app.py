import requests


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
                    "state": data["features"][zoneindex]["properties"]["state"]
                }
        else:
            print("Invalid statement.")


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
