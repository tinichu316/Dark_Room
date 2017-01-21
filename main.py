import world, sys
from player import Player

# could make a fun thing to have the game close (but save obviously) if your sanity get's below some amount
#def play():
#initialize the world

#do a menu thing that gives 3 options, save, load, newgame. Start the loop after they choose an option.

introGreeting = """You wake up to a slightly humid but otherwise dark room.
The draft coming in from the North and East indicates a narrow passageway.
You move around and observe your exits.\n"""

menuText = """Welcome to Dark Room, a Python Adventure game.\n\n
type 'load' to load the previous file.
type 'newgame' to begin a new game (and erase the previous file).
Type 'exit' to quit the application.\n
"""

def menuLoop(): #could make the menu a room... nah
    while player.inMenu:
        print(menuText)
        actionInput = actionInput = input("\n[...]: ")
        if actionInput == "exit":
            sys.exit()
        if actionInput == "load":
            player.loadGame()
            play()
        if actionInput == "newgame":
            play()


def play():
    world.loadTiles()
    player.inMenu = False
    if player.location == [3,3]: #the starting location
        print(introGreeting)
    #ask the player for the name
    while player.isAlive() and not player.victory:
        #finds the current room and does whatever it needs to the player
        room = world.tileExists(player.location[0],player.location[1])
        room.modifyPlayer(player)
        #DEBUG THE ROOM
        print("\nROOM DEBUG ", room)
        #incase the player dies:
        if player.isAlive() and not player.victory:
            print(room.introText())
            print("What do you do?\n")
            availableActions = room.availableActions()
            for i in availableActions:
                print(i)
            actionInput = input("\n[...]: ").split(' ')
            actionInput = actionInput[:3] #only takes the first 3 legit inputs
            print("DEBUG USER INPUT: ", actionInput)
            #cheap debugging ways
            if actionInput[0] == "exit":
                sys.exit()
            if actionInput[0] == "save":
                player.saveGame()
            for i in availableActions:
                if actionInput[0] == i.hotkey:
                    #checks if the user uses a command that requires arguments
                    if actionInput[0] == "use":
                        if len(actionInput) == 1:
                            print("What are you using?")
                            break
                        elif len(actionInput) == 2:
                            player.doAction(i, item=actionInput[1])
                            break
                        else:
                            print("I don't understand that.")
                            break

                    elif actionInput[0] == "usewith":
                        if len(actionInput) == 1:
                            print("What are you using and with what?")
                            break
                        elif len(actionInput) == 2:
                            print("What do you want to use the %s with?" %actionInput[1])
                            break
                        elif len(actionInput) == 3:
                            player.doAction(i, item=actionInput[1], doorCheck=actionInput[2])
                            break
                        else:
                            print("I don't understand that.")
                            break

                    elif actionInput[0] == "pickup":
                        if len(actionInput) == 1:
                            print("What do you pickup?")
                            break
                        elif len(actionInput) == 2:
                            player.doAction(i, item=actionInput[1])
                            break
                        else:
                            print("I don't understand that.")
                            break

                    else:
                        player.doAction(i, **i.kwargs)
                        break

            else: #nonsense response
                print("That's not a valid command.")
                
    
    
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

if __name__ == "__main__":
    player = Player()        
    menuLoop()
    