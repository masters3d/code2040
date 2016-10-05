import http.client
import json

conn = http.client.HTTPConnection("challenge.code2040.org")

payload = "{\"token\":\"MYCODE2040APIKEY\"}"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'cache-control': "no-cache"
   }

conn.request("POST", "/api/dating", payload, headers)

res = conn.getresponse()
data = res.read()

response = data.decode("utf-8")
print(response)

jsonResponse = json.loads(response)
datestamp = jsonResponse["datestamp"]
interval = jsonResponse["interval"]
print(datestamp)
print(interval)

import dateutil.parser
from datetime import datetime, timedelta

date = dateutil.parser.parse(datestamp)
print(date)
date = date + timedelta(seconds=interval)

dateString = date.isoformat()
dateString = dateString.replace("+00:00", "Z")
print(dateString)

payload = "\"token\" : \"MYCODE2040APIKEY\", \"datestamp\" : \"{}\"".format(dateString)
payload = "{" + payload + "}"

print(payload)

conn.request("POST", "/api/dating/validate", payload, headers)

res = conn.getresponse()
data = res.read()
response = data.decode("utf-8")

print(response)
