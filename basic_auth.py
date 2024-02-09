import requests

url = "https://postman-echo.com/basic-auth"
header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
username = "postman"
password = "password"

response = requests.get(url, auth=(username, password))

print("Status Code:", response.status_code)

if response.status_code == 200:
    print("Response JSON:", response.json())
else:
    print("Error:", response.text)