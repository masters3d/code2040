import http.client
import json

conn = http.client.HTTPConnection("challenge.code2040.org")

payload = "{\"token\":\"MYCODE2040APIKEY\"}"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'cache-control': "no-cache"
   }

conn.request("POST", "/api/prefix", payload, headers)

res = conn.getresponse()
data = res.read()

response = data.decode("utf-8")
#print(response)

jsonResponse = json.loads(response)
prefix = jsonResponse["prefix"]
arrayP = jsonResponse["array"]
print(prefix)
#print(arrayP)

arrayToReturn = []

for each in arrayP:
	if not each.startswith(prefix):
		arrayToReturn.append(each)



payload = "\"token\" : \"MYCODE2040APIKEY\", \"array\" : {}".format(arrayToReturn)
payload = "{" + payload + "}"

payload = payload.replace("'", "\"")

print(payload)

conn.request("POST", "/api/prefix/validate", payload, headers)

res = conn.getresponse()
data = res.read()
response = data.decode("utf-8")

print(response)
