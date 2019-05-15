#! python

#a script that builds a list, and then prints it out

#build a small list of trees, print the list
trees = ['cedar', 'hickory', 'oak']
print('\nList of trees: '+str(trees))

#add new trees to the list
trees.append('pecan')
trees.append('willow')
print('\nWe added new trees: '+str(trees))

#create a new list containing only the newly added trees
new_trees = trees[-2:]
print('\nSpecifically, we added: '+str(new_trees))

#final print statement
print('\nFinal list of trees: '+str(trees))

#Challenge 1
#insert a tree into the front of the list, and then print the new list.
trees.insert(0,'pine')
print('\nFinal list of trees: '+str(trees))

#Challenge 2
#pop the last tree in the list, then use a variable to hold that and print out what you popped off.
last_tree = trees.pop()
print('\nFinal tree: '+str(last_tree))
