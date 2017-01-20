import os.path as path #use lexists
import player

# write objects and locations with capitals

#ITEM = (index)
KEY = 0
#LOCATION = (room number) (x,y coordinates. e.g. Dark Room would be (45)
DARK_ROOM = 0
HALLWAY = 1
FRONT_DOOR = 2

# save information as a text file
fileName = "saveGame.txt"

#default values:
#only updates when the file is saved.
data = player.data
#data = {"playerName" : "", "room" : [4,5], "inventory" : [], "sanity" : 100} #  store inventory in binary

def loadGameFile(fileName):
    if path.lexists(fileName):
        with open(fileName) as f:
            loadedFile = f.readlines()
        for x in loadedFile: #for each line in the save file
            if "playerName" in x:
                data["playerName"] = x[13:-2]
            if "room" in x:
                data["room"][0] = int(x[7])
                data["room"][1] = int(x[10])
            if "inventory" in x:
                for char in x:
                    if char.isdigit():
                        data["inventory"].append(int(char))
            if "sanity" in x:
                data["sanity"] = int(x[8:12])
    else:
        raise Exception("Save file not found!")

def saveGameFile(fileName):
    with open(fileName, "w") as f:
        f.write("playerName: '%s'\n" % data['playerName'])
        f.write("room: %s\n" % data['room'])
        f.write("inventory: %s\n" % data['inventory'])
        f.write("sanity: %i\n" % data['sanity'])
        
def inventoryContains(item):
    foo = True if data['inventory'][item] == 1 else False
    return foo

#get's the player's name
t1 = False
while not t1:
    data["playerName"] = input("What's your name? ")    
    resp = input("So your street name is: %s? (y/n) " %data["playerName"])
    if resp == "y":
        t1 = True




