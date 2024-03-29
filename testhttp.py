import requests

url = "https://jsonplaceholder.typicode.com/posts/"

payload = {"id":[1,2,3],"userId":1}

response = requests.get(url, params=payload)

response_json = response.json()

#status = response.status_code
for i in response_json:
    print(i, "\n")

print(response_json)


new_data = {
    "userID": 1,
    "id": 1,
    "title": "Making a POST request",
    "body": "This is the data we created."
}

# The API endpoint to communicate with
url_post = "https://jsonplaceholder.typicode.com/posts"

# A POST request to tthe API
post_response = requests.post(url_post, json=new_data)

# Print the response
post_response_json = post_response.json()
print(post_response_json)