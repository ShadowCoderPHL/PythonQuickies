import requests
import json


for x  in range(1, 150):
    url = "https://yourcompanyhere.api-us1.com//api/3/fields/"+ str(x)
    
    
    headers = {
        "Accept": "application/json",
        "api-token": "YOUR_API_KEY_HERE"
    }
    
    
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    
    try:
        print("\"" + data['field']['title'].replace(" ", "_").replace("/", "_").lower() + "\" => \"" + data['field']['id'] + "\",")
    except KeyError:
        print(x)
    