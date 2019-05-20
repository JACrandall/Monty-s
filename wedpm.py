#!/usr/bin/python3

"""Game of Thrones API || author: janice.crandall@verizonwireless.com """
import requests
#import pprint

#ask user what book they want to query
booknum = input("Which book are you searching on (1-5)? ")

#build our finished URL (API)
bookurl = str("https://www.anapioficeandfire.com/api/books/" + booknum)

resp = requests.get(bookurl)
resp = resp.json()

#pprint.pprint(resp.json())
#tell user the Name of that book

print("That book is: ",  resp['name'])
book_name = (str(resp['name'])).replace(" ","")
f= open(book_name+'.txt','w')
#pprint.pprint(resp)

#list the name of the characters in that book
#this requires access the URLs returned in our first lookup
#for loops stop automatically when it gets to the end of the list
for t_url in resp["characters"]:
    #print(t_url,"\n\n")
    char_resp = requests.get(t_url)
    char_resp = char_resp.json()
    t_char = char_resp['name']
    #print(t_char)
    f.write(str(t_char)+'\n')

#looping throught each URL and grabbing the names returned by each