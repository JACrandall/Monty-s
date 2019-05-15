#!/usr/bin/python3

"""Space-X API || author: janice.crandall@verizonwireless.com """
import requests
import pprint
import webbrowser

#access URL = https://api.spacexdata.com/v3/launches/latest
resp = requests.get('https://api.spacexdata.com/v3/launches/latest')
resp = resp.json()

#pprint.pprint(resp)
m_name = resp['mission_name']
m_date = resp['launch_date_local']

print("Name of the mission is: ", m_name)
print("Launch Date: ", m_date)

m_rock = resp["rocket"]["rocket_name"]
print(m_rock, '\n')

input('\n Press enter to access a videolink \n')

#m_link = 'https://en.wikipedia.org/wiki/SpaceX_CRS-17'

webbrowser.open(resp['links']['wikipedia'])

