#!/usr/bin/python3

"""in the endgame || author: janice.crandall@verizonwireless.com """

import requests
import argparse
import time
import hashlib

#see pg 61 of the book / this is a public variable
XAVIER = 'http://gateway.marvel.com/v1/public'

#create a hashing function
def hashbuild(cur_time,priv_key,pub_key):
    return hashlib.md5((cur_time+priv_key+pub_key).encode('utf-8')).hexdigest()

#make the character call
def marvelcharcall(cur_time,hashy,pub_key,look_me_up):
    marvel_url = XAVIER+'/characters'
    marvel_url += "?name="+look_me_up+"&ts="+cur_time+"&apikey="+pub_key+'&hash='+hashy
    hulk = requests.get(marvel_url)
    return hulk.json()

def main():
    #harvest public key
    with open('marvelpub.txt') as pubkeyfile:
        beast = pubkeyfile.read().rstrip('\n')

    #harvest private key
    with open ('marvelpri.txt') as privkeyfile:
        storm = privkeyfile.read().rstrip('\n')

    #create an string of an integer for the timestamp
    cur_time=str(int(time.time()))
    
    #Ask user for Marvel Character to look up
    charlook = input("What character are we looking up? ")
    #build the hashkey to pass to the API
    hashy = hashbuild(cur_time,storm,beast)

    print(marvelcharcall(cur_time, hashy, beast, charlook))

main()


    
