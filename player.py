import items

data = {"playerName" : "", "room" : [4,5], "inventory" : [1], "sanity" : 100} #  store inventory in binary

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
            
                
    
                