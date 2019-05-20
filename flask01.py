#!/usr/bin/python3

import csv
import json

from flask import Flask

app = Flask(__name__)



@app.route("/")
def vzw():
    return "Welcome to API Automation!"

@app.route("/hello/<name>")
def hello_name(name):
    return "Hello {}".format(name)

@app.route("/v1/csvwithout/<filename>")
#@app.route("/v1/csvwithout/")

def my_csv_parse_wo():
    big_list = []
    if ".csv" not in filename:
        filename = filename = ".csv"
    with open(filename) as csv_to_parse:
        csvreader = csv.reader(csv_to_parse)
        for row in csvreader:
            little_list = []
            little_list.append(row[1])
            little_list.append(row[3])
            big_list.append(little_list)
        return json.dumps(big_list)

@app.route("/v1/csvwith/")
def my_csv_parse_with():
    big_list = []
    with open('mycsvwith.csv') as csv_to_parse:
        csvreader = csv.DictReader(csv_to_parse)
        for row in csvreader:
            little_list = []
            little_list.append(row['ip'])
            little_list.append(row['port'])
            big_list.append(little_list)
        return json.dumps(big_list)

if __name__ == "__main__":
    app.run(port=9103)



