import json
import requests

URL = "http://127.0.0.1:8000/predict"

with open("backend/samples/premium_customer.json") as file:
    payload = json.load(file)

response = requests.post(URL, json=payload)

print(response.status_code)
print(response.json())