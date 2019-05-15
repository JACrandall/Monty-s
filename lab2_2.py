#! python

# a script that pulls in numberical data from the user and prints out the sun

#gather numbers from the user and convert the numbers to integers with typecasting
first_num = int(input('n\Please provide a number from 1 to 9: '))
second_num = int(input ('n\Please input a number that is from 1 to 9: '))

#convert the numbers to integers with typecasting
#first_num = int(first_num)
#second_num = int(second_num)

#check to make sure input numbers are within range
if first_num < 1 or first_num > 9:
    print("We are done with you. You can't follow directions. "+str(first_num)+" ??")
    exit()

if second_num < 1 or second_num > 9:
    print("We are done with you. You can't follow directions. "+str(second_num)+" ??")
    exit()

#do math, print out the result.
sum_of_nums = first_num + second_num
print('The sum of your numbers is: '+str(sum_of_nums))

#challenge
print('\n' + 'The sum of '+str(first_num)+' and '+ str(second_num)+' is: ' + str(sum_of_nums))