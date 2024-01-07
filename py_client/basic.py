import json
import requests

endpoint = "http://127.0.0.1:8000/api"

get_response = requests.get(endpoint, json={"title": "Abc123", "content": "Hello world", "price":"abc134"}) # HTTP Request
print(get_response.text)
print(get_response.headers)
# print(get_response.status_code)

# print(get_response.json())
# print(get_response.json()['message'])

