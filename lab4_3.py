#! python

#a script that loops 3 times asking for names, then prints them back.

#build an empty list

names = []

#a FOR loop that reads in 3 names from the user
for i in range(3):
    x = input("Please provide a name, any name: ")
    names.append(x)

#a FOR loop that prints out the 3 names for the user
#print("The names that you choose: ")
#for x in names:
#    print(x)

#change the formatting of the names printed out so that they are in the 'Title' case.
print("The names that you choose: ")
for x in names:
    print(x.lower().title())