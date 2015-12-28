import httplib
import urllib
import json
import hashlib
import hmac


conn = httplib.HTTPSConnection("btc-e.com")
conn.request("GET", "/api/2/btc_usd/depth")
response = conn.getresponse()
# conn=httplib.HTTPConnection("https://btc-e.com/api/2/btc_usd/depth");

print response.status, response.reason
json_response=json.load(response)
# print json.load(response)
print json_response.keys()
print json_response
print len(json_response['asks'])