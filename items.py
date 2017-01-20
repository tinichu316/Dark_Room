playerName = "PLACEHOLDER" #until i can figure out how to import without importing before the player enters their name

allItems = [] #holds all the items.. only adds them the first time they are called though
#does not add items if you just call the item with the appropriate parameter.. works if you print the item though.
totalItemNo = 2

class Item():
    #base class for all items
    #index is the index in the save file
    def __init__(self, index, name, description, sanity): 
        self.index = index
        self.name = name
        self.description = description
        self.sanity = sanity

    def __addToList__(self):
        #adds the item to the masterlist
        i = 0
        while i < totalItemNo: #number of items that we have
            if len(allItems) == self.index: #adds the items by their index in order
                #add to the list
                allItems.append(self)
            i += 1
    
    def __str__(self):
        return "%s." %(self.name)
    
    def useByPlayer(self, player):
        return "You can't do that."
    


class IntroNote(Item):
    def __init__(self, playerName):
        self.playerName = playerName
        self.sanityAmt = -5
        self.isFirstTime = True
        super().__init__(index = 0,
                         name = "A crumpled note",
                         description = "It reads: I've been waiting for you, %s." %self.playerName,
                         sanity = self.sanityAmt)
        
    def useByPlayer(self, player):
        if isFirstTime:
            player.sanity += self.sanityAmt
            isFirstTime = False
    
    
class Trinket(Item):
    def __init__(self):
        #in the parent (super) to initialize the item with these arguments
        self.sanityAmt = 20
        super().__init__(index = 1,
                         name = "Trinket", 
                         description = "A sentimental token that reminds you of home.",
                         sanity = self.sanityAmt)
        
    def useByPlayer(self, player):
        if isFirstTime:
            player.sanity += self.sanityAmt
            isFirstTime = False
        


#for items in this script, initialize them
#just have to put all the items here:
#It's ugly but it works
items = [IntroNote(playerName), Trinket()] 
for obj in items:
    obj.__addToList__()
    


