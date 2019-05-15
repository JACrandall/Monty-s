#!/usr/bin/python3

"""in the endgame || author: janice.crandall@verizonwireless.com """

import requests
import pprint

#define my api key (read in from a file)
with open("nasakey.txt") as keyfile:
    mykey=keyfile.read()
#add in a start_date = START_DATE where start_date in format YYYY-MM-DD
#sdte=input("Enter the start date of the query (YYYY-MM-DD): ")
sdte='2019-05-10'

#also add in end_date=END_DATE where end_date in format YYYY-MM-DD
#edte=input("Enter the end date of the query (YYYY-MM-DD): ")
edte='2019-05-12'

#lookup nasa api
#GET https://api.nasa.gov/neo/rest/v1/feed?start_date=START_DATE&end_date=END_DATE&api_key=API_KEY
bigrocks = requests.get(r"https://api.nasa.gov/neo/rest/v1/feed?start_date="+sdte+"&end_date="+edte+"&api_key="+mykey)
#dump initial data to screen
#pprint.pprint(bigrocks.json())
bigrocks=bigrocks.json()

for rock in bigrocks["near_earth_objects"].values():
    for srock in rock:
        print("Rock Name: ",srock['name'],"\n", "ID: ", srock['id'])
        c_a_d = (srock['close_approach_data'][0])
        print(c_a_d,"\n")
        