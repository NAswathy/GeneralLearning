import requests

# Define the API endpoint URL
url = "http://127.0.0.1:5000/api/v1/create"

# Define the data to be sent in the POST request
data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com"
}

# Send a POST request to the API endpoint with the data
response = requests.post(url, json=data)

# Check the response status code
if response.status_code == 200:
    print("Data processed successfully")
else:
    print("Failed to process data")
