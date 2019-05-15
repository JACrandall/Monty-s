#! python

import os

#a script that will create a directory, create a file in that directory, then delete both

#create a new directory
os.makedirs('c:\\python_files\\example_files')

#create a new file in the example_files directory
filename = 'c:\\python_files\\example_files\\tester.txt'
file_object = open(filename, 'w')
file_object.close()

#challenge portion, open file in read mode
with open(filename, 'r+') as file_object
    file_object.write('Gardening\n')
    print(file_object.read())

#delete the new file
os.unlink(filename)

#delete the new directory
os.rmdir('C:\\python_files\\example_files')

