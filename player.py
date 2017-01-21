import items, random, math, world
import os.path as path #use lexists

fileName = "resources/save1.txt"

data = {"playerName" : "", "room" : [3,3], "inventory" : [0]*items.totalItemNo, "sanity" : 100} # default info

def displaySanity(percent):
    bar = ["-"]*20
    responses = {
                -1: " are dead.",
                0: " are about to die.",
                1: "r heart is beating like crazy.",
                2: " begin to see hallucinations.",
                3: " feel increasingly dizzy.",
                4: " have a slight headache.",
                5: " feel just fine."}
    if percent <= 100:
        resp = math.ceil((percent-10)/20)        
        for i in range(math.ceil(percent/5)):
            bar[i] = "|"
        
    else:
        resp = 5        
        bar = ["|"]*20
    health = "".join(bar)
    
    print("\nSanity: [" + health + "] (%s%%)        You%s" %(percent, responses[resp]))

class Player():
    # place commands here.
    def __init__(self):
        self.playerName = data['playerName']
        self.location = data['room']        
        self.inventory = data['inventory'] #store info in bits
        self.sanity = data['sanity']
        self.victory = False
        self.inMenu = True
        #gives the player the starting note
        self.inventory[0] = 1
        
    def isAlive(self):
        return self.sanity > 0

    def doAction(self, action, **kwargs):
        #finds the method 'action' in this class.
        actionMethod = getattr(self, action.method.__name__)
        #if found, it runs the method with any additional keywords.
        print("DEBUG KEYWORDS", kwargs)
        if actionMethod:
            if not kwargs: #if the dictionary is empty aka no extra parameters
                actionMethod(**kwargs)
            else:
                actionMethod(kwargs)

    def pickup(self, item):
        item = item['item']
        if item == None:
            print("You pickup nothing.")
        #checks location..
        elif item == "key" and self.location == [4,1]: #Bad Room
            if self.inventory[3] == 0: #the item is not there
                self.inventory[3] = 1
                print("You picked up the key.")
            else:
                print("You already picked up the key!")
        elif item == "key" and self.location == [2,6]: #good choice
            if self.inventory[4] == 0:  # the item is not there
                self.inventory[4] = 1
                print("You picked up the key.")                
            else:
                print("You already picked up the key!")
        elif item == "trinket" and self.location == [6,3]:
            if self.inventory[1] == 0:  # the item is not there
                self.inventory[1] = 1
                print("You feel calmer after placing the trinket in your hand.")
                self.sanity += 20
            else:
                print("You already have the trinket!")
        else:
            print("There's no %s to pickup." %item)
        
    def printInventory(self):
        print("You find in your pockets...")
        for i in range(len(self.inventory)):
            if self.inventory[i]: #if the item is there
                print(items.allItems[i])

    def printSanity(self):
        displaySanity(self.sanity)

    #movement commands
    def move(self, dx, dy):
        self.location[0] += dx
        self.location[1] += dy
    def move_north(self):
        self.move(0,-1)
    def move_south(self):
        self.move(0, 1)
    def move_east(self):
        self.move(1, 0)
    def move_west(self):
        self.move(-1, 0)

    def useItem(self, item): #item is a str
        item = item['item']
        index = 10
        if item == "note":
            index = 0
        if item == "trinket":
            index = 1
        if item == "key":
            index = 2 #the potato
        if len(self.inventory) >= index and self.inventory[index]: #if the player has the item
            print(items.allItems[index].useByPlayer(self))
        else:
            print("There is no such %s." %item)

    def useItemTarget(self, item):
        target = self.location
        doorCheck = item['doorCheck']
        item = item['item']
        #target is the player's room [x,y]
        # doorCheck is what the player wants to use the item with (confusing, I know)
        targetRoom = world.tileExists(target[0],target[1])
        if item == "key" and doorCheck == "door":
            keyType = 0 #1 is key 1, 2 is both keys
            if len(self.inventory) == 4 and self.inventory[3] and self.inventory[4]:
                keyType = 2
            elif len(self.inventory) == 3 and self.inventory[3]:
                keyType = 1
            else:
                print("You don't have a key!")

            if targetRoom.doorType == 0:
                print("There's no door here to unlock.")
            elif keyType == targetRoom.doorType or keyType == 2:
                targetRoom.unlock()
            else:
                print("That key doesn't fit here.")

        elif doorCheck == "door":
            print("I can't use %s on the door." %item)
        elif item == "key":
            print("How can I use a key with a %s?" %doorCheck)
        else:
            print("I can't use a %s with a %s." %(item, doorCheck))


    def callHelp(self):
        luck = random.randrange(10)
        if luck < 4:
            print("\nYou call for help and instead hear a eerie moan.\nYour sanity drops as a result.")
            self.sanity -= 15
        elif luck < 8:
            print("\nYou call for help, but no one answers.\nYour sanity dips as a result.")
            self.sanity -= 5
        else:
            print("\nYou cry for help. \nThe sound of your own voice soothes you.\nYou gain some sanity.")
            self.sanity += 10
        displaySanity(self.sanity)

    def saveGame(self):
        if not path.lexists(fileName):
            print("DEBUG FILE DOESNT EXIST")
            open(fileName, 'a')
        with open(fileName, "w") as f:
            f.write("playerName: '%s'\n" % self.playerName)
            f.write("room: %s\n" % self.location)
            f.write("inventory: %s\n" % self.inventory)
            f.write("sanity: %i\n" % self.sanity)
        print("Game saved.")

    def loadGame(self):
        if path.lexists(fileName):
            with open(fileName) as f:
                loadedFile = f.readlines()
            for x in loadedFile:  # for each line in the save file
                if "playerName" in x:
                    self.playerName = x[13:-2]
                if "room" in x:
                    self.location[0] = int(x[7])
                    self.location[1] = int(x[10])
                if "inventory" in x:
                    counter = 0
                    for char in x:
                        if char.isdigit():
                            self.inventory[counter] = int(char)
                            counter += 1
                if "sanity" in x:
                    self.sanity = int(x[8:12])
        else:
            raise Exception("Save file not found!")
                