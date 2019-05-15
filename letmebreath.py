#!/usr/bin/python3

""" look up air quality | Author:janice.crandall@verizonwireless.com"""

LOOKUPAPI = r"http://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-05-14&distance=25&API_KEY=AA3508D1-F495-41D8-956F-1348DFF70023"

import requests

def main():
    r = requests.get(LOOKUPAPI)
    evenlist = (r.json())[0::2]
    for day in evenlist:
        print(day['DateForecast'])
        print(day['ReportingArea'], day['StateCode'], sep=', ')
        print("Today's air quality is: ",day['Category']['Name'])
        print(day['Discussion'])
        input("--- Press Enter to Continue ---")

main() 


