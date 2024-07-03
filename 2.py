 import httpx
import json

url = "your_url_here"

# Using a context manager to ensure the client is properly closed
with httpx.Client(verify=False) as client:
    response = client.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Error: {response.status_code}")
