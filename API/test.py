
import requests
import json
url = "http://127.0.0.1:5000/"
payload = json.dumps([
    {
        "data": "hi i'm bisht"
    }
])
headers = {
    'Content-Type': 'application/json'
}
resposnse = requests.request("POST", url, data=payload, headers=headers)
print(resposnse.text)
