import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Why are you gay",
    "price": 32.99
}
get_response = requests.post(endpoint, json=data)
print(get_response.json())