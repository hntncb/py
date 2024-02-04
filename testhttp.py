import requests

url = "https://google.com"

response = requests.get(url)

#response_json = response.json()

status = response.status_code

print(status)