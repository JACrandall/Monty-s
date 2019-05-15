#!/usr/bin/python3

def showInstructions():
    print('''
    RPG Game
    --------
    Commands:
        go [direction]
        get [item] 
        type exit to leave the game
    ''')

def showStatus():
    print('------------------------------')
    print('You are in the', currentRoom)
    print('Inventory:', inventory)
    if "item" in rooms[currentRoom]:
        print('You see a', rooms[currentRoom]['item'])
    print('------------------------------')

inventory=[]

rooms={'Hall':{'south':'Kitchen', 'east':'Dining Room','item':'key'},\
    'Kitchen':{'north':'Hall','item':'monster'},'Dining Room':{'west':'Hall','item':'cookie'},\
        'Garden':{'north':'Dining Room'}}

currentRoom='Hall'

showInstructions()

while True:
    showStatus()
    move=''
    while move=='':
        move = input('> ')
    move=move.lower().split()

    if move[0]=='go':
        if move[1] in rooms[currentRoom]:
            currentRoom=rooms[currentRoom][move[1]]
        else:
            print("You cannot go that way")
    if move[0]=='get':
        if 'item' in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
            inventory +=[move[1]]
            print('You just picked up', move[1])
            del rooms[currentRoom]['item']
        else:
            print('Cannot get',move[1])
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']\
        and 'cookie' in inventory:
        print('You throw the cookie at the monster! He suddenly seems preoccupied...')
        del rooms[currentRoom]['item']
        inventory.remove('cookie')
    if 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
        print('A monster has got you.... GAME OVER!')
        break

    if currentRoom == 'Garden' and 'key' in inventory:
        print("You used the key to open the door in the garden and escape the creepy monster house")
        print("You win!")
        break

print('Thanks for playing!')
    
            
