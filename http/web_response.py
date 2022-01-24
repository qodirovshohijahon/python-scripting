#!/usr/bin/env python

import http.client
import pprint

con = http.client.HTTPSConnection("api.fda.gov")
con.request('GET', '/drug/label.json?limit=10')

res = con.getresponse()

print("Status: {}".format(res.status))

headers_list = res.getheaders()
print("Headers: {}".format(headers_list))

con.close()