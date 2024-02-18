import requests
from bs4 import BeautifulSoup
# Set up API endpoint and parameters
endpoint = 'https://api.discord.com/users'
params = {
 'limit': 100, # number of users to create
 'token': '', # token for authenticating with Discord API
}
headers = {'Authorization': 'Bot ' + params['token']}
payload = {}
# Create users one by one
for i in range(params['limit']):
 name = f"User{i+1}"
 email = f"user{i+1}@example.com"
 password = f"password_{i+1}"
 payload[f"{name}_username"] = name
 payload[f"{name}_email"] = email
 payload[f"{name}_password"] = password
 response = requests.post(endpoint, headers=headers, data=payload)
 if response.status_code == 201:
  print(f"Created user '{name}'!")
 else:
  print(f"Failed to create user '{name}'.")