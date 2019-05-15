#! python

import time
import random

#function that will roll the dice
def roll_dice(name):
    #random.randint will generate the random dice rolls, arguments(1,7) specified 1 through 6
    dice_one = random.randint(1,7)
    dice_two = random.randint(1,7)
    dice_total = dice_one + dice_two
    #print out the results
    print('\n' + name +' rolled a ' +str(dice_one) + ' and '+ str(dice_two) + ' for a total of '+str(dice_total) + '.')

#a simple game of dice, using a function to calculate the dice rolls

#loop that will stop when the player enters 'exit'
while True:
    answer = input('\nWould you like to play dice? Type exit to exit, and anything else to play: ')
    #check to see if the player entered 'exit'
    if answer.lower()=='exit':
        break
    print('\nThe dice will be rolled for the computer, then you, highest total wins!')
    
    #time.sleep() specified for how many seconds you would like to pause the script
    time.sleep(2)

    #call the roll_dice function and store the returned total in variables
    comp_total = roll_dice('Computer')
    time.sleep(2)
    player_total = roll_dice('User')
    time.sleep(2)

    #determine who wins with an If-Else loop
    if comp_total >= player_total:
        print('\nThe computer wins!')
    else:
        print('\nYou Win!  Congratulations!!!')

