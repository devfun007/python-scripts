import requests
import json


def firewall(id):
    url = "https://n163.meraki.com/api/v0/networks/" + id + "/l3FirewallRules/"

    payload = "{\n\t\"rules\": [\n\t    {\n        \"comment\": \"Deny to corporate\",\n        \"policy\": \"deny\",\n        \"protocol\": \"any\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"192.168.1.0/24\",\n        \"destPort\": \"Any\",\n        \"destCidr\": \"172.16.0.0/12\",\n        \"syslogEnabled\": false\n    },\n    {\n        \"comment\": \"Deny to corporate\",\n        \"policy\": \"deny\",\n        \"protocol\": \"any\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"192.168.1.0/24\",\n        \"destPort\": \"Any\",\n        \"destCidr\": \"10.0.0.0/8\",\n        \"syslogEnabled\": false\n    },\n    {\n        \"comment\": \"http\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"80\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"https\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"443\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"http-alt\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"8080\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"NTP\",\n        \"policy\": \"allow\",\n        \"protocol\": \"udp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"123\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"DNS\",\n        \"policy\": \"allow\",\n        \"protocol\": \"udp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"53\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Meraki cloud communication\",\n        \"policy\": \"allow\",\n        \"protocol\": \"udp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"7351\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"VPN Registry\",\n        \"policy\": \"allow\",\n        \"protocol\": \"udp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"9350\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Backup Controller\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"993,7734,7752\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Backup Controller 2\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"60000-61000\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"RentCafe CRM\",\n        \"policy\": \"allow\",\n        \"protocol\": \"tcp\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"8024\",\n        \"destCidr\": \"104.156.164.124/32\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Block CnC\",\n        \"policy\": \"deny\",\n        \"protocol\": \"any\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"Any\",\n        \"destCidr\": \"212.114.52.210/32\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Block CnC\",\n        \"policy\": \"deny\",\n        \"protocol\": \"any\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"Any\",\n        \"destCidr\": \"45.147.229.0/24\",\n        \"syslogEnabled\": true\n    },\n    {\n        \"comment\": \"Deny Catch All\",\n        \"policy\": \"deny\",\n        \"protocol\": \"any\",\n        \"srcPort\": \"Any\",\n        \"srcCidr\": \"Any\",\n        \"destPort\": \"Any\",\n        \"destCidr\": \"Any\",\n        \"syslogEnabled\": true\n    }\n\t]\n}"
    headers = {
        'X-Cisco-Meraki-API-Key': "",
    'Content-Type': "application/json",
    'User-Agent': "PostmanRuntime/7.20.1",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "b0a76270-28b3-4401-a0ca-dcf6b1c77467,9e14025d-89a2-4212-b189-9334e4f9a2f7",
    'Host': "",
    'Accept-Encoding': "gzip, deflate",
    'Content-Length': "536",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

    response = requests.request("PUT", url, data=payload, headers=headers)

    print(response.text)

fh = open("networkids.txt", "r")

filecontent = fh.read()

data = json.loads(filecontent)

for item in data:
    print (item["id"])
    firewall(item["id"])