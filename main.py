import requests
import base64

# Define API URL and credentials
token_url = 'https://accounts.spotify.com/api/token'
client_id = "fbb110ab30ad4948864988c4aac9772f"
client_secret = "e6e0e157c46a426fbbdd351d11599237"

# Encode credentials in base64
message = f"{client_id}:{client_secret}"
messagebase64 = base64.b64encode(message.encode()).decode()

# Define headers and data
token_header = {
    "Authorization": f"Basic {messagebase64}",
    "Content-Type": "application/x-www-form-urlencoded"
}
data = {
    "grant_type": "client_credentials"
}

# Make the POST request
r = requests.post(token_url, data=data, headers=token_header)
token = r.json()

# Print the access token
print(token)