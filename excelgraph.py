#/usr/bin/python3
import datetime # this is from timestamping
import matplotlib.pyplot as plt #this is from graphing
import pandas as pd # this is for data conversion to data framing
from pandas import ExcelWriter
from pandas import ExcelFile

def main():
    #creates a pandas dataframe of a sheet from an excel book
    mdf = pd.read_excel('lastday.xlsx', sheet_name='Sheet1')
    xaxisyears = mdf["years"]
    xaxisyears =list(xaxisyears.values)
    xaxisyears = map(str, xaxisyears)
    xaxisyears = list(xaxisyears)
    
    yaxisminout = mdf["mins"]
    yaxisminout = list(yaxisminout.values)
    print(yaxisminout)
    """
    now =datetime.datetime.now() # produces a timestamp of NOW
    xaxisyears = ["2016","2017","2018","2019"]
    yaxisminout = [100,2200,34,55]
    plt.ylabel("Downtime in Mins")
    plt.xlabel("Year")
    plt.title("Downtime in Minutes per Year")

    plt.plot(xaxisyears, yaxisminout)
    plt.savefig(now.strftime("%Y-%m-%d-outage.png"))
    """
main()

