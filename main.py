import world, sys, items, random
from player import Player

# could make a fun thing to have the game close (but save obviously) if your sanity get's below some amount

#check if saving and loading means people can exploit room.isFirstTime

#do a menu thing that gives 3 options, save, load, newgame. Start the loop after they choose an option.

#how much sanity the player loses per game loop:
sanityTick = -1

endings = [
"Your mind is nearly gone.",
"You begin to remember your past.",
"You have a heavy headache but are otherwise fine.",
"You remain unscathed. You are unstoppable!"
]

victoryScreen = """You stumble against the wooden door.
You reach to turn the handle as the voices get nearer.\n

                            .-''''-
                           F   .-'
                          F   J
                         I    I
                          L   `.
                           L    `-._,
                            `-.__.-'            @@
                                               @@@
                       @                      @@@@
              _____   @@                 .---@@@@@-...__
          .--'     `-@@@          .--..-'    @@@@@@     ''`---....
 _____.----.        @@@`.._____ .'          @@@@@@@
                    @@@       /       -.    @@@@@@@ _.---
                    @@@     .(              @@@@@@@
                     @      : `--...        @@@@@@
                     @       `.     ``.     @@@@@@
                               :       :.    @@@@@
                             .'          )    @@@
                           .'            /    @@
                        _.'              |   .@@
                      ,:'               |     '
                    .'                 <
                   '                   |
                  /                    |
                 '                     .

You feel the outside wind, the pale moonlight hitting your skin.
        """

introGreeting = """

                    ==={[o]|[o]|[o]|[o]|[o]}===

You wake up to a slightly humid but otherwise dark room.
The draft coming in from the North and East indicates a narrow passageway.
You move around and observe your exits.\n"""

menuText = """
         _____           _
        |  _  \         | |
        | | | |__ _ _ __| | __
        | | | / _` | '__| |/ /
        | |/ / (_| | |  |   <
        |___/ \__,_|_|  |_|\_\\

        ______
        | ___ \\
        | |_/ /___   ___  _ __ ___
        |    // _ \ / _ \| '_ ` _ \\
        | |\ \ (_) | (_) | | | | | |
        \_| \_\___/ \___/|_| |_| |_|

         a Python Adventure game.
             By William Wang\n\n
type 'load' to load the previous file.
type 'newgame' to begin a new game (and erase the previous file).
Type 'exit' to quit the application.
"""

def menuLoop(): #could make the menu a room... nah
    while player.inMenu:
        print(menuText)
        actionInput = input("\n[...]: ").lower()
        if actionInput == "exit":
            sys.exit()
        if actionInput == "load":
            player.loadGame()
            play()
        if actionInput == "newgame":
            play()


def spookItUp(sanity):
    luck = random.randrange(0,100)
    if luck > sanity:
        player.displaySpook()

def getPlayerName():
    t1 = False
    while not t1:
        print("\nWhat's your name?")
        playerName = input("\n[...]: ")
        resp = input("\nIs %s what you want to be known as? (y/n) " % playerName)
        if resp == "y":
            return playerName

def score(sanity):
    #selects a certain ending to return based on the player's sanity. 0 = worst.
    ending = sanity//(100//len(endings))
    return endings[ending-1]



def play():
    world.loadTiles()
    #ask the player for the name
    pN = getPlayerName()
    items.playerName = player.playerName = pN
    #sets the intro note name to the player's name
    items.allItems[0] = items.IntroNote(pN)

    player.inMenu = False
    if player.location == [3,3]: #the starting location
        print(introGreeting)

    while player.isAlive() and not player.victory:
        #finds the current room and does whatever it needs to the player
        room = world.tileExists(player.location[0],player.location[1])
        room.modifyPlayer(player)
        #DEBUG THE ROOM
        #print("\nROOM DEBUG ", room,"\n")
        #incase the player dies:
        if player.isAlive() and not player.victory:
            print(room.introText())
            print("What do you do?\n")
            availableActions = room.availableActions()
            for i in availableActions:
                print(i)

            player.sanity += sanityTick
            spookItUp(player.sanity)

            actionInput = (input("\n[%s]: " %player.playerName).lower()).split(' ')
            actionInput = actionInput[:3] #only takes the first 3 legit inputs
            print("==========================================================================================\n")
            if actionInput[0] == "exit":
                sys.exit()
            for i in availableActions:
                if actionInput[0] == "save":
                    player.saveGame()
                    break
                elif actionInput[0] == i.hotkey:
                    #checks if the user uses a command that requires arguments
                    if actionInput[0] == "use":
                        if len(actionInput) == 1:
                            print("What are you using? Type 'use [item]'")
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
                            print("What do you pickup? Type 'pickup [item]'")
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
                print("Invalid command.\n")
                
    #if you win
    if player.isAlive() and player.victory:
        print(victoryScreen)
        print("You have escaped with %s%% sanity." %player.sanity)
        print(score(player.sanity))

    #if you died
    if not player.victory and not player.isAlive():
        print("""\n
                        YOU DIED
                 .-.
               .'   `.
               :x x   :
               : -     `.
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
    