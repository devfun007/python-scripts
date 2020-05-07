import requests
import json


def changehub(id):
    url = "https://api.meraki.com/api/v0/networks/" + id + "/siteToSiteVpn"

    payload = payload = "{\n\"mode\":\"spoke\",\n\"hubs\":[{\n  \"hubId\":\"networkid\",\n  \"useDefaultRoute\":false\n  },\n  {\n    \"hubId\":\"networkid\",\"useDefaultRoute\":false\n  }]\n}"
    headers = {
    'X-Cisco-Meraki-API-Key': "enter api key",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "162",
    'Referer': "https://api.meraki.com/api/v0/networks/" + id + "/siteToSiteVpn",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print(response.text)

fh = open("networdids.txt", "r")

filecontent = fh.read()

data = json.loads(filecontent)

for item in data:
    print (item["id"])
    changehub(item["id"])