#!/usr/bin/python3
"""Openstack json parsing
author: janice.crandall@verizonwireless.com
learning about json and python
"""
 
import json
 
def main():
    """runtime code"""
    with open(r'openstackresponse01.json', 'r') as openjson:
        print(openjson.read())
        openjson.seek(0)  #to move pointer in file back up to the top of file
        decodedopenjson = json.load(openjson)
        #print(decodedopenjson)
        print(decodedopenjson['server']['imageRef'])
 
main()