import httplib
import urllib
import json
import hashlib
import hmac
import csv
import time

ordersConn = httplib.HTTPSConnection("btc-e.com")


priceConn = httplib.HTTPSConnection("btc-e.com")


with open('test1.csv', 'wb') as f:
    writer = csv.writer(f, delimiter='|',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL)

    while True:
        ordersConn.request("GET", "/api/2/btc_usd/depth")
        response = ordersConn.getresponse()
        row = []
        row.append(int(round(time.time() * 1000)))

        priceConn.request("GET", "/api/2/btc_usd/ticker")
        priceResponse=priceConn.getresponse()
        jsonPriceResponse=json.load(priceResponse)
        row.append(jsonPriceResponse['ticker']['last'])

        # conn=httplib.HTTPConnection("https://btc-e.com/api/2/btc_usd/depth");

        # print response.status, response.reason
        json_response = json.load(response)
        # print json.load(response)
        # print json_response.keys()
        json_response['bids'].sort()
        json_response['asks'].sort()
        for pair in json_response['bids']:
            row.append(pair[0])
            row.append(pair[1])

        for pair in json_response['asks']:
            row.append(pair[0])
            row.append(pair[1])

        writer.writerow(row)
        time.sleep(1)
    # print json_response
    # print len(json_response['asks'])
