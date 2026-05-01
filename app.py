import requests
import tkinter as tk

def extract(category,specific):
    if specific == True:
        response = requests.get(f"https://api.weather.gov/{category}/{specific}")
    else:
        response = requests.get(f"https://api.weather.gov/{category}")
        
    data = response.json