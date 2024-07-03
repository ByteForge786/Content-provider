import urllib3
import json

# Disable InsecureRequestWarning if you're not verifying the SSL certificate
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

http = urllib3.PoolManager()
url = "your_url_here"

response = http.request('GET', url)

if response.status == 200:
    data = json.loads(response.data.decode('utf-8'))
    print(data)
else:
    print(f"Error: {response.status}")
