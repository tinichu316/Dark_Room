import items, random, math, world
import os.path as path #use lexists

fileName = "resources/save1.txt"

data = {"playerName" : "", "room" : [3,3], "inventory" : [0]*items.totalItemNo, "sanity" : 100} # default info

spookyQuotes = [
"Flee, screaming.",
"Give in, to your fear.",
"Hope is an illusion.",
"Caress your fear.",
"The mitochondria is the powerhouse of the cell.",
"I always lie.",
"Death... is close.",
"Who do the VooDoo?",
"Your sanity has decreased by 90 points.",
"Your courage will fail.",
"Honey, wake up! You're going to be late for school!",
"You are weak.",
"Your heart will explode.",
"No one will remember you.",
"Karen, Where's my report?",
"One eighteen and one quarter package chocolate cake mix.",
"Life was so much better back on Pig Beach.",
"Just who the hell do you think we are?",
"Apples. Oranges. Pears. Plums. Kumquats. Lemons. Limes. Avocado. Tomato. Banana. Papaya."
]

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
    
    print("Sanity: [" + health + "] (%s%%)        You%s\n" %(percent, responses[resp]))

class Player():
    # place commands here.
    def __init__(self):
        self.playerName = data['playerName']
        self.location = data['room']        
        self.inventory = data['inventory'] #store info in bits
        self.sanity = data['sanity']
        self.victory = False
        self.inMenu = True
        
    def isAlive(self):
        return self.sanity > 0

    def doAction(self, action, **kwargs):
        #finds the method 'action' in this class.
        actionMethod = getattr(self, action.method.__name__)
        #if found, it runs the method with any additional keywords.
        if actionMethod:
            if not kwargs: #if the dictionary is empty aka no extra parameters
                actionMethod(**kwargs)
            else:
                actionMethod(kwargs)

    def pickup(self, item):
        whichItem = item['item']
        currentRoom = world.tileExists(self.location[0], self.location[1])

        # Turns out the object memory index is different but as long as the strings are the same
        # aka they don't have the same name and description, we gucci.
        if whichItem == None:
            print("You pickup nothing.")
        #checks location and if the current room has the item. if so, it removes it.
        # limitations: room can only have one item or no items
        elif whichItem == "key" and str(currentRoom.item) == str(items.Key1()):
            if self.inventory[3] == 0: #the item is not already picked up
                self.inventory[3] = 1
                print("You picked up the key.\n\nYour sanity has slightly increased.\n")
                #gain sanity for checkpoint pickups.
                self.sanity += 3
                self.printSanity()
                currentRoom.item = None
            else:
                print("You already picked up the key!")
        elif whichItem == "key" and str(currentRoom.item) == str(items.Key2()): #good choice
            if self.inventory[4] == 0:
                self.inventory[4] = 1
                print("You picked up the key.\n\nYour sanity has slightly increased.\n")
                self.sanity += 3
                self.printSanity()
                currentRoom.item = None
            else:
                print("You already picked up the key!")
        elif whichItem == "trinket" and str(currentRoom.item) == str(items.Trinket()):
            if self.inventory[1] == 0:
                self.inventory[1] = 1
                print("You feel calmer after placing the trinket in your hand.\n")
                self.sanity += 5
                self.printSanity()
                currentRoom.item = None
            else:
                print("You already have the trinket!")
        else:
            print("There's no %s to pickup." %whichItem)
        
    def printInventory(self):
        print("You find in your pockets...")
        for i in range(len(self.inventory)):
            if self.inventory[i]: #if the item is there
                print(items.allItems[i])
        print("")

    def printSanity(self):
        displaySanity(self.sanity)

    def displaySpook(self):
        # print some spooky words
        luck = random.randrange(0, len(spookyQuotes), 1)
        print("*%s*" %spookyQuotes[luck])

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
        elif item == "trinket":
            index = 1
        # if it's a key, it will print invalid response
        elif item == "key":
            index = 3

        if index == 10:
            print("You don't have a %s.\n" %item)
        elif self.inventory[index]: #if the player has the item and types in a valid name
            items.allItems[index].useByPlayer(self)
            self.printSanity()
        else:
            print("You don't have a %s.\n" %item)

    def useItemTarget(self, item):
        target = self.location
        doorCheck = item['doorCheck']
        item = item['item']
        #target is the player's room [x,y]
        # doorCheck is what the player wants to use the item with (confusing, I know)
        targetRoom = world.tileExists(target[0],target[1])
        if item == "key" and doorCheck == "door":
            keyType = 0 #1 is key 1, 2 is both keys
            if self.inventory[4]:
                keyType = 2
            elif self.inventory[3]:
                keyType = 1
            else:
                print("You don't have a key!\n")

            if targetRoom.doorType == 0:
                print("There's no door here to unlock.\n")
            elif keyType == targetRoom.doorType or keyType == 2:
                targetRoom.unlock()
                self.sanity += 3
            else:
                print("That key doesn't fit here.\n")

        elif doorCheck == "door":
            print("I can't use %s on the door.\n" %item)
        elif item == "key":
            print("How can I use a key with a %s?\n" %doorCheck)
        else:
            print("I can't use a %s with a %s.\n" %(item, doorCheck))


    def callHelp(self):
        luck = random.randrange(10)
        if luck < 4:
            print("You call for help and instead hear a eerie moan.\nYour sanity drops as a result.")
            self.sanity -= 15
        elif luck < 8:
            print("You call for help, but no one answers.\nYour sanity dips as a result.")
            self.sanity -= 5
        else:
            print("You cry for help. \nThe sound of your own voice soothes you.\nYou gain some sanity.")
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
        print("Game saved.\n")

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
                