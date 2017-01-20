import world
from player import Player

# could make a fun thing to have the game close (but save obviously) if your sanity get's below some amount
#def play():
#initialize the world

#do a menu thing that gives 3 options, save, load, newgame. Start the loop after they choose an option.


world.loadTiles()
player = Player()

while player.isAlive() and not player.victory:
    #finds the current room and does whatever it needs to the player
    room = world.tileExists(player.location[0],player.location[1])
    room.modifyPlayer(player)
    #DEBUG THE ROOM
    print("\nROOM DEBUG ", room)
    #incase the player dies:
    if player.isAlive() and not player.victory:
        isFirstTime = True
        if isFirstTime:
            print("""You wake up to a slightly humid but otherwise dark room.
The draft coming in from the North and East indicates a narrow passageway.\n""")
            ifFirstTime = False
        print("What do you do?\n")
        availableActions = room.availableActions()
        for i in availableActions:
            print(i)
        actionInput = input("\n[...]: ").split(' ')
        actionInput = actionInput[:3] #only takes the first 3 legit inputs
        print("DEBUG USER INPUT: ", actionInput)
        if actionInput[0] == "exit":
            quit()
        for i in availableActions:
            if actionInput[0] == i.hotkey: #if it matches the hotkey
                #sloppy way of checking the number of inputs.. might want to figure out how to use variable length or
                #how to pass a list of variable length into the **kwargs
                if actionInput[0] == "u" and len(actionInput) == 2:
                    player.doAction(i, item = actionInput[1])
                    break
                elif actionInput[0] == "uw" and len(actionInput) == 3:
                    player.doAction(i, item = actionInput[1], doorCheck = actionInput[2])
                    break
                elif actionInput[0] == 'u' or actionInput[0] == 'uw':
                    print("I don't understand you!") #idk why this doesn't print if the input is only 'uw'
                    break
                else:
                    player.doAction(i, **i.kwargs)
                    break


#if you died
if not player.victory and not player.isAlive():
    print("""\n
                    YOU DIED
                 .-.
               .'   `.
               :g g   :
               : o    `.
              :         ``.
             :             `.
            :  :         .   `.
            :   :          ` . `.
             `.. :            `. ``;
                `:;             `:'
                   :              `.
                    `.              `.     .
                      `'`'`'`---..,___`;.-'

                    """)
        
        
#at every location it should print out the possible paths.


#run play when the file is opened:

#if __name__ == "__main__":
    #play()