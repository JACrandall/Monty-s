#! python
#This code is a test from the beginner Python class
#The purpose of this code is to read data from a file, calculate BMI
#and then write the output to a file

#create a list to store input from the input file where weight is on line 1
#and height in inches is on line 2
file = open('C:\\python scripts\\bmifile.txt', 'r')
varis = file.readlines()

#read list into variables for calculation 
x=int(varis[0][:-1])
y=int(varis[1][:-1])

#make metric conversion

kilos = x / 2.2046
meters = y / 39.370

#calculate BMI
BMI = int(kilos / (meters * meters))

#print BMI to output file called bmi.txt
f= open('bmi.txt','w')
f.write(str(BMI)+'\n')
