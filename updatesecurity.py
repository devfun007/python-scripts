import requests
import json

def update(id):
    url = "https://api.meraki.com/api/v0/networks/" + id + "/security/malwareSettings"

    payload = "{\r\n  \"mode\": \"enabled\",\r\n  \"allowedUrls\": [\r\n    {\r\n      \"url\":",\r\n      \"comment\": \"\"\r\n    },\r\n    {\r\n      \"url\": \"\",\r\n      \"comment\": \"\"\r\n    },\r\n    {\r\n      \"url\": \"",\r\n      \"comment\": \"\"\r\n    }\r\n  ]\r\n}"
    headers = {
        'X-Cisco-Meraki-API-Key': "enter api key",
        'Content-Type': "application/json"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print(response.text)

fh = open("networkids.txt", "r")

filecontent = fh.read()

data = json.loads(filecontent)

for item in data:
    print (item["id"])
    update(item["id"])