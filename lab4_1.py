#! python

#import randon module
import random

#a script that takes a number from the user and checks if it is from 1 to 10

#take a number from the user and convert a number from a string to an integer
num = int(input('Please guess a number between 1 and 10: '))

#if-elif-else statement to check if the number is between 1 and 10
if num < 1:
    print("Your number is less than 1. Follow directions!")
elif num > 10:
    print("Your number is greater than 10. Follow directions!")
else:
    guess = random.randint(1,11)
    if num == guess:
        print("The number " + str(num) + " is between 1 and 10 and it was a correct guess.  Good job! You are a good guesser!")
    else:
      print("The number " + str(num) + " is between 1 and 10 but it was not a correct guess!") 

    

#Challenge
#Make this a quick guessing game! Tell user to guess a number between 1 and 10, then tell them
#if they guessed correctly.  Still check the validity of the number being
#between 1 and 10 but then add a block that also checks to see if the user
#guessed correctly.
