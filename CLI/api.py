import requests

# Define the API endpoint and message payload
url = "http://127.0.0.1:8000/api"
payload = {"msg": "What is your name"}

# Send the HTTP POST request
response = requests.post(url, json=payload)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the response data (bot's answer)
    data = response.json()
    bot_answer = data["res"]
    print("Bot's answer:", bot_answer)
else:
    print("Error:", response.status_code)
