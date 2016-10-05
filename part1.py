import http.client

conn = http.client.HTTPConnection("challenge.code2040.org")

payload = "{\"token\" : \"MYCODE2040APIKEY\", \"github\" : \"https://github.com/masters3d/code2040\"}"

headers = {
    'content-type': "application/json",
    'accept': "application/json",
    'cache-control': "no-cache"
    }

conn.request("POST", "/api/register/", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))