import requests
# import json

BASE_URL = "http://localhost:5000/"

response = requests.get(BASE_URL + "login")

print(response.json())