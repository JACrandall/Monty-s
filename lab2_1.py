#! python

# A script which searches a string for a word, then slices out a portion of the string

message = 'Well, hey there, are you doing good?'

#Find the index of the work 'are'
are_index = message.find('are')

#Slice out the desired portion then print it out
new_message = message[are_index:]

print('\n' + message)
print('\n' + new_message)