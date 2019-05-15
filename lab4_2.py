#! python

#a simple loop that asks the user when to exit

#a counter to keep count of how many times the loop has run

ctr = 1

#continuous loop that exists when a condition is met
while True:
    #gather user input, if'exit' then exit the loop, otherwise keep looping.
    user_input = input("Useless loop iteration # "+str(ctr)+", type exist if you wish to exit: ")
    if user_input.lower() == "exit":
        print("Exiting the useless loop!")
        break
    else:
        ctr +=1
        if ctr > 5:
            break

 #Challenge - make it so that the loop will only run a maximum of 5 times.       