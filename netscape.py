#!/usr/bin/python3

""" a simple hppt client | Author:janice.crandall@verizonwireless.com"""

import http.client

conn = http.client.HTTPConnection("localhost","9106")

conn.request('GET', '/')

res = conn.getresponse()

print(res.status, res.reason)

print(res.read())