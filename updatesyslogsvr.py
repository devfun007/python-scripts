import requests
import json


def changesyslog(id):
    url = "https://api.meraki.com/api/v0/networks/" + id + "/syslogServers"

    payload = payload = "{\n    \"servers\": [\n        {\n            \"host\": \\",\n            \"port\": 514,\n            \"roles\": [\n               \"URLs\",\n                \"Security events\"\n            ]\n        }\n    ]\n}"
    headers = {
        'X-Cisco-Meraki-API-Key': "1b1390aad1f5db8ce70ef7bfbf6f85ec9e8df72d",
        'Content-Type': "application/json",
       'cache-control': "no-cache",
        'Postman-Token': "8bf74032-a79d-4b38-abfb-ca4b1741bfd5"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print(response.text)

fh = open("networkids.txt", "r")

filecontent = fh.read()

data = json.loads(filecontent)

for item in data:
    print (item["id"])
    changesyslog(item["id"])