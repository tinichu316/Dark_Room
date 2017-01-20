import items
import random
import math

data = {"playerName" : "", "room" : [4,5], "inventory" : [1], "sanity" : 100} #  store inventory in binary

def displaySanity(percent):
    bar = ["-"]*20
    responses = {0: " are about to die.", 
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
    
    print("Sanity: [" + health + "] (%s%%)        You%s" %(percent, responses[resp]))

class Player():
    # place commands here.
    def __init__(self):
        self.playerName = data['playerName']
        self.location = data['room']        
        self.inventory = data['inventory'] #store info in bits
        self.sanity = data['sanity']
        self.victory = False
        
    def isAlive(self):
        return self.sanity > 0
        
        
    def printInventory(self):
        for i in range(len(self.inventory)):
            if self.inventory[i]: #if the item is there
                print(items.allItems[i])
                
    def useItem(self, item):
        index = items.allItems.index(item)
        if self.inventory[index]: #if the player has the item
            print(items.allItems[index].useByPlayer())
        else:
            print("There is no such item %s." %item)
            
    def callHelp(self):
        luck = random.randrange(10)
        if luck < 4:
            print("You call for help and instead hear a eerie moan.\nYour sanity drops as a result.")
            self.sanity -= 15
        elif luck < 8:
            print("You call for help, but no one answers.\nYour sanity dips as a result.")
            self.sanity -= 5
        else:
            print("You cry for help. The sound of your own voice soothes you.\nYou gain some sanity")
            self.sanity += 10
        displaySanity(self.sanity)
            
    
                
    
                