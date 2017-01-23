# does not add items if you just call the item with the appropriate parameter.. works if you print the item though.
totalItemNo = 5
playerName = "PLACEHOLDER"

class Item():
    # base class for all items
    # index is the index in the save file
    def __init__(self, index, name, description):
        self.index = index
        self.name = name
        self.description = description

    def __str__(self):
        return "%s. %s" %(self.name, self.description)

    #general case. if the item can be used, define it specifically.
    def useByPlayer(self, player):
        return "You can't do that."
    
#===============================================================================    

    
class Key1(Item):
    def __init__(self):
        self.keyType = 1
        super().__init__(index = 3,
                         name = "A rusty brass key",
                         description = "It looks almost rusted away."
                         )
        
    def useByPlayerTarget(self, target): #target will be the room that we are in
        if self.keyType == target.doorType and target.isLocked:
            target.unlock()
            return "Door unlocked!"
        else:
            return "You can't use that here!"

    def useByPlayer(self, player):
        print("Use the key with what? Use 'usewith [item] [target]'\n")


class Key2(Item):
    def __init__(self):
        self.keyType = 2
        super().__init__(index = 4,
                         name = "A rusty golden key",
                         description = "An old key that's almost rusted away."
                         )
        
    def useByPlayerTarget(self, target): #target will be the room that we are in
        if self.keyType == target.doorType and target.isLocked:
            target.unlock()
            return "Door unlocked!"
        else:
            return "You can't use that here!"

    def useByPlayer(self, player):
        print("Use the key with what? Use 'usewith [item] [target]'\n")


    


class IntroNote(Item):
    def __init__(self, playerName):
        self.playerName = playerName
        self.sanityAmt = -10
        self.isFirstTime = True
        super().__init__(index = 0,
                         name = "A crumpled note",
                         description = "It reads: Dear %s..." %self.playerName,
                         )
        
    def useByPlayer(self, player):
        if self.isFirstTime:
            player.sanity += self.sanityAmt
            self.isFirstTime = False
            print("""You touch the note and a chill goes up your spine.
It reads:

 █     █░ ▄▄▄       ██ ▄█▀▓█████     █    ██  ██▓███
▓█░ █ ░█░▒████▄     ██▄█▒ ▓█   ▀     ██  ▓██▒▓██░  ██▒
▒█░ █ ░█ ▒██  ▀█▄  ▓███▄░ ▒███      ▓██  ▒██░▓██░ ██▓▒
░█░ █ ░█ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ▓▓█  ░██░▒██▄█▓▒ ▒
░░██▒██▓  ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒▒█████▓ ▒██▒ ░  ░
░ ▓░▒ ▒   ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ▒ ░ ░    ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░░▒░ ░ ░ ░▒ ░
  ░   ░    ░   ▒   ░ ░░ ░    ░       ░░░ ░ ░ ░░
    ░          ░  ░░  ░      ░  ░      ░

Your sanity has decreased.""")
        else:
            print("""The note reads:

 █     █░ ▄▄▄       ██ ▄█▀▓█████     █    ██  ██▓███
▓█░ █ ░█░▒████▄     ██▄█▒ ▓█   ▀     ██  ▓██▒▓██░  ██▒
▒█░ █ ░█ ▒██  ▀█▄  ▓███▄░ ▒███      ▓██  ▒██░▓██░ ██▓▒
░█░ █ ░█ ░██▄▄▄▄██ ▓██ █▄ ▒▓█  ▄    ▓▓█  ░██░▒██▄█▓▒ ▒
░░██▒██▓  ▓█   ▓██▒▒██▒ █▄░▒████▒   ▒▒█████▓ ▒██▒ ░  ░
░ ▓░▒ ▒   ▒▒   ▓▒█░▒ ▒▒ ▓▒░░ ▒░ ░   ░▒▓▒ ▒ ▒ ▒▓▒░ ░  ░
  ▒ ░ ░    ▒   ▒▒ ░░ ░▒ ▒░ ░ ░  ░   ░░▒░ ░ ░ ░▒ ░
  ░   ░    ░   ▒   ░ ░░ ░    ░       ░░░ ░ ░ ░░
    ░          ░  ░░  ░      ░  ░      ░
            """)

            #weird.. prints out 'None' after..
    
    
class Trinket(Item):
    def __init__(self):
        #in the parent (super) to initialize the item with these arguments
        self.sanityAmt = 20
        self.isFirstTime = True
        super().__init__(index = 1,
                         name = "A Trinket",
                         description = "A sentimental token that reminds you of home."
                         )
        
    def useByPlayer(self, player):
        if self.isFirstTime:
            player.sanity += self.sanityAmt
            self.isFirstTime = False
            print("You place the trinket around your neck and feel better protected. \nYour sanity has increased slightly.\n")



#literally just here for convenience sake. remove if possible. Makes the allItems array 5 elements long
class DumbPotato(Item):
    def __init__(self):
        super().__init__(index = 2,
                         name = "A dumb Potato",
                         description = "How did you even get this?"
                         )


#ADD NEW ITEMS HERE:
#================================================================================================
allItems = [IntroNote(playerName), Trinket(), DumbPotato(), Key1(), Key2()]

