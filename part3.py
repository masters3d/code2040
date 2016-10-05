import http.client
import json

conn = http.client.HTTPConnection("challenge.code2040.org")

payload = "{\"token\":\"MYCODE2040APIKEY\"}"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'cache-control': "no-cache"
   }

conn.request("POST", "/api/haystack", payload, headers)

res = conn.getresponse()
data = res.read()

response = data.decode("utf-8")
#print(response)

jsonResponse = json.loads(response)
needle = jsonResponse["needle"]
haystack = jsonResponse["haystack"]
print(needle)
print(haystack)

indexOfNeedle = haystack.index(needle)

payload = "\"token\" : \"MYCODE2040APIKEY\", \"needle\" : {}".format(indexOfNeedle)
payload = "{" + payload + "}"

conn.request("POST", "/api/haystack/validate", payload, headers)

res = conn.getresponse()
data = res.read()
response = data.decode("utf-8")

print(response)
