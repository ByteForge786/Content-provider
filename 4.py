import httpx
import json

url = "your_url_here"

# Disable SSL verification warnings
import warnings
warnings.filterwarnings("ignore", message="Unverified HTTPS request")

with httpx.Client(verify=False) as client:
    try:
        response = client.get(url)
        
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                print("JSON Data:")
                print(json.dumps(data, indent=2))
            except json.JSONDecodeError:
                print("Response is not JSON. Content:")
                print(response.text)
        elif response.status_code in (301, 302, 303, 307, 308):
            print(f"Redirect detected. Location: {response.headers.get('Location')}")
        else:
            print(f"Unexpected status code: {response.status_code}")
            print("Response content:")
            print(response.text)
    
    except httpx.RequestError as e:
        print(f"An error occurred while requesting {e.request.url!r}.")
        print(str(e))
