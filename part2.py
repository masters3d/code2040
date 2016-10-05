import http.client

conn = http.client.HTTPConnection("challenge.code2040.org")

payload = "{\"token\":\"MYCODE2040APIKEY\"}"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'cache-control': "no-cache"
   }

conn.request("POST", "/api/reverse", payload, headers)

res = conn.getresponse()
data = res.read()

stringToReverse = data.decode("utf-8")
stringToSend = stringToReverse[::-1]

print(stringToReverse)
print(stringToSend)

payload = "\"token\" : \"MYCODE2040APIKEY\", \"string\" : \"{}\"".format(stringToSend)
payload = "{" + payload + "}"

conn.request("POST", "/api/reverse/validate", payload, headers)

res = conn.getresponse()
data = res.read()
response = data.decode("utf-8")

print(response)
