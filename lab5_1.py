#! python

#please create a color.txt file in c:\phython_files\ and put 5 colors, each on their own line

#create a file object, then use readlines() to store the file contents
filename='C:\\python_files\\colors.txt'
with open(filename) as file_object:
    colors = file_object.readlines()

#use a FOR loop to print out the colors to the prompt
for x in colors:
    print(x)    
