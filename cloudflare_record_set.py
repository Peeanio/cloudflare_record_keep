import requests
import os
import json
import socket
import time

record = os.environ["RECORD"]
comment = os.environ["COMMENT"]
zone = os.environ["ZONE"]
email = os.environ["EMAIL"]
key = os.environ["KEY"]
record_id = os.environ["RECORD_ID"]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("1.1.1.1", 80))
ip_addr = s.getsockname()[0]
s.close()

url = f"https://api.cloudflare.com/client/v4/zones/{zone}/dns_records/{record_id}"

request_data = {"content": ip_addr,
        "name": record,
        "ttl": 3600,
        "type": "A",
	"proxied": False
}

request_headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {key}"
}
while True:
    r = requests.patch(url, data=json.dumps(request_data), headers=request_headers)

    print(r.content)
    
    time.sleep(6000)
