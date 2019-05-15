#!/usr/bin/python3
ctr=0
#open the log file
with open("imblog.log") as jclog: #read mode if the default
    for logline in jclog:
    #look for source ip address
        if "source address" in logline:
            ctr = ctr + 1  #or ctr += 1
            #print ips that are source ips to screen
            #print(logline)
            #print(logline.split(' ')[-1], end="") #the end="" eliminates the double spacing between IP addresses
            #write source ips to an output file
            with open ("imblog.out","a") as jcout:
                #print(logline.split(' ')[-1], end="",file=jout)
                jcout.write(logline.split(' ')[-1])
#display total number of source ips to screen
print("The number of source IP addresses in the file is: ", ctr)
with open("imblog.out") as jcout:
    print(set(jcout.readlines()))