playerName = "PLACEHOLDER" # until i can figure out how to import without importing before the player enters their name


# does not add items if you just call the item with the appropriate parameter.. works if you print the item though.
totalItemNo = 5

class Item():
    # base class for all items
    # index is the index in the save file
    def __init__(self, index, name, description, sanity): 
        self.index = index
        self.name = name
        self.description = description
        self.sanity = sanity

    # def __addToList__(self):
    #     # adds the item to the masterlist
    #     for i in range(totalItemNo + 1): # number of items that we have
    #         if len(allItems) == self.index:  # adds the items by their index in order
    #             # add to the list
    #             allItems.append(self)
    
    def __str__(self):
        return "%s: %s" %(self.name, self.description)

    #general case. if the item can be used, define it specifically.
    def useByPlayer(self, player):
        return "You can't do that."
    
#===============================================================================    

    
class Key1(Item):
    def __init__(self):
        self.keyType = 1
        super().__init__(index = 3,
                         name = "A rusty brass key",
                         description = "It looks almost rusted away.",
                         sanity = 5)
        
    def useByPlayerTarget(self, player, target): #target will be the room that we are in
        if self.keyType == target.doorType and target.isLocked:
            target.unlock()
            return "Door unlocked!"
        else:
            return "You can't use that here!"

    def useByPlayer(self, player):
        print("Use the key with what? Use 'uw [item] [target]'")


class Key2(Item):
    def __init__(self):
        self.keyType = 2
        super().__init__(index = 4,
                         name = "A rusty golden key",
                         description = "An old key that's almost rusted away.", 
                         sanity = 10)
        
    def useByPlayerTarget(self, player, target): #target will be the room that we are in
        if self.keyType == target.doorType and target.isLocked:
            target.unlock()
            return "Door unlocked!"
        else:
            return "You can't use that here!"

    def useByPlayer(self, player):
        print("Use the key with what? Use 'uw [item] [target]'")


    


class IntroNote(Item):
    def __init__(self, playerName):
        self.playerName = playerName
        self.sanityAmt = -10
        self.isFirstTime = True
        super().__init__(index = 0,
                         name = "A crumpled note",
                         description = "It reads: I've been waiting for you, %s." %self.playerName,
                         sanity = self.sanityAmt)
        
    def useByPlayer(self, player):
        if self.isFirstTime:
            player.sanity += self.sanityAmt
            self.isFirstTime = False
            print("You touch the note and a chill goes up your spine. \nYour sanity has decreased.")
    
    
class Trinket(Item):
    def __init__(self):
        #in the parent (super) to initialize the item with these arguments
        self.sanityAmt = 20
        self.isFirstTime = True
        super().__init__(index = 1,
                         name = "Trinket", 
                         description = "A sentimental token that reminds you of home.",
                         sanity = self.sanityAmt)
        
    def useByPlayer(self, player):
        if self.isFirstTime:
            player.sanity += self.sanityAmt
            self.isFirstTime = False



#literally just here for convenience sake. remove if possible. Makes the allItems array 5 elements long
class DumbPotato(Item):
    def __init__(self):
        super().__init__(index = 2,
                         name = "A dumb Potato",
                         description = "How did you even get this?",
                         sanity = 1000)
        


# def updateInventory():
#     #for items in this script, initialize them
#     #just have to put all the items here:
#     #It's ugly but it works
#     items = [IntroNote(playerName), Trinket(), DumbPotato(), Key1(), Key2()]
#     for obj in items:
#         obj.__addToList__()
        
allItems = [IntroNote(playerName), Trinket(), DumbPotato(), Key1(), Key2()]  # holds all the items.. only adds them the first time they are called though

