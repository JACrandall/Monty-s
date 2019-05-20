#!/usr/bin/python3

"""Price tracker & comparison shop tool ||
pull in upc and prices using Walmart API || 
author: janice.crandall@verizonwireless.com """

import requests
import sqlite3
import time


#define Walmart's API
WUPC = 'http://api.walmartlabs.com/v1/items?'
APIKEY = 'apikey=d7hjdvye4sky5cdwmmmtf3bf'

def upclookup(whatupc):
    
    resp = requests.get(WUPC+APIKEY+whatupc)

    if resp.status_code==200:
        return resp.json()
    else:
        return False

def trackmeplease(trackt, trackp):
    conn = sqlite3.connect('price.db')
    try:
        conn.execute('''CREATE TABLE PRICE
        (TIME VARCHAR2 PRIMARY KEY NOT NULL,
        PRICE REAL  NOT NULL);''')
    except:
        pass
    conn.execute ("INSERT INTO PRICE (TIME,PRICE) VALUES (?,?)", (trackt, trackp))
    conn.commit()
    cursor = conn.execute("SELECT time, price from PRICE")
    for row in cursor:
        print("TIME = ", row[0])
        print("PRICE = ", row[1])
        print()

    print('Database operation complete')
    conn.close()    
    


def main():
    whatupc = input("What is the UPC you wish to look up? ")
    whatupc = '&upc=' + whatupc
    mylookup =  upclookup(whatupc)
    if mylookup:
        #print (mylookup)
        m_upc = mylookup['items'][0]['upc']
        m_name = mylookup['items'][0]['name']
        m_price = mylookup['items'][0]['salePrice']
        m_desc = mylookup['items'][0]['shortDescription']
   
        print("The UPC Code for the item is: ", m_upc, '\n')
        print("The item name is: ", m_name, '\n')
        print("The sales price is: ", m_price, '\n')
        print("Short Description: ", m_desc, '\n')
        trackmeplease(time.ctime(), m_price)
        
    else:
        print("Something went wrong with your lookup. Sorry... (Buy something else)")
main()





