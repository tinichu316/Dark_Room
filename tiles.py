import items, actions, world


#non specific types of rooms (more than 1 exist)
class MapTile():
    def __init__(self, x, y):
        #default stuff for every tile
        self.x = x
        self.y = y
        self.doorType = 0
        self.isFirstTime = True
        self.item = None
        
    def introText(self):
        raise NotImplementedError() # we don't want to actually create anything called a maptile so we have to override these methods in any of our other classes
    
    def modifyPlayer(self, player):
        raise NotImplementedError()

    def adjacentMoves(self):
        # returns possible move actions and prints it to the user
        #maybe add locked door blocking here?
        possibleMoves = []
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x - 1, self.y):
            possibleMoves.append(actions.MoveWest())
        if world.tileExists(self.x, self.y - 1):
            possibleMoves.append(actions.MoveNorth())
        if world.tileExists(self.x, self.y + 1):
            possibleMoves.append(actions.MoveSouth())
        return possibleMoves

    def availableActions(self):
        moves = self.adjacentMoves()
        #list the possible extra moves aside from movement
        list = [actions.ViewInventory(),
                actions.CallHelp(),
                actions.ViewSanity(),
                actions.UseItem(None),
                actions.UseItemTarget(None, None),
                actions.PickupItem(None)]
        moves.extend(list)
        return moves

    

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def pickup(self, player):
        index = items.allItems.index(self.item)
        player.inventory[index] = 1

    def modifyPlayer(self, player):
        pass


#this type of room, like the two above it, need to be passed an x and y coordinate of a specific locked room
#player can enter this room but can't pass unless it's unlocked
class LockedRoom(MapTile):
    def __init__(self, x, y, isLocked, doorType):
        self.isLocked = isLocked
        self.doorType = doorType
        super().__init__(x, y)
        
    def unlock(self):
        #unlocks the door
        self.isLocked = False
        print("Click! The door unlocks!\n")

    def modifyPlayer(self, player):
        pass


#===============================================================================
#specific rooms 
class Dark_Room(MapTile):
    def introText(self): #triple quotes span multiple lines
            return "The dark room smells like dust and mildew.\n"
    
    def modifyPlayer(self, player):
        # Room does nothing
        if self.isFirstTime:
            player.inventory[0] = 1
            self.isFirstTime = False
    
    
class Hallway(MapTile):
    def introText(self): #triple quotes span multiple lines
        return "You walk into the passageway.\n"

    def modifyPlayer(self, player):
        pass
    
    
class Bad_Choice(MapTile):
    def introText(self):
        if self.isFirstTime:
            self.isFirstTime = False
            return """
A sense of dread overcomes you as you enter this room.
Your legs feel heavy and your head grows dizzier.
Your take lumbering steps before you crash to the ground.
    ___________________________________________
   |\\'-._(   /                                 |
   | \  .'-._\                            ,   ,|
   |-.\\'    .-;                         .'\`-' |
   |   \  .' (                       _.'   \   |
   |.--.\\'   _)                   ;-;       \._|
   |    ` _\(_)/_                  \ `'-,_,-'\ |
   |______ /(O)\  _________________/____)_`-._\|


You awake covered in spiderwebs.
Your sanity has taken a large hit.
    """
        else:
            return """
Terrible memories haunt you here. You feel worse.\n
            """
    
    def modifyPlayer(self, player):
        if self.isFirstTime:
            player.sanity -= 40
            player.printSanity()
        else:
            player.sanity -= 10
            player.printSanity()
        
        
class Front_Door(MapTile):
    def introText(self): # can add different endings depending on sanity
        return """
        YOU WIN
        """
    
    def modifyPlayer(self, player):
        player.victory = True
        
class Choice_Room(MapTile):
    def introText(self):
        #let's place a riddle or puzzle here that will hint at the rooms
        return """You enter a room split into North and South directions.
A message scrawled on the wall reads:
'One of these doors will lead to doom so be careful and pick the right room.
If the magnetic field lines around the Earth point from North to South,\nwhich way would a compass point?'
"""
    
    def modifyPlayer(self, player):
        pass
    
class Loot_Dirty(MapTile):
    def introText(self):
        if self.isFirstTime:
            self.isFirstTime = False
            return """
As you enter, a strong scent of cinnamon and pumpkin spice hits you.
            ( (
             ) )
          ........
          |      |]
          \      /
           `----'
You see a gorgeous looking latte and you can't help but devour it.
You feel better after that.
        """
        else:
            return """Without the latte the room looks less appealing.
            """
    def modifyPlayer(self, player):
        if self.isFirstTime:
            player.sanity += 10
            player.printSanity()
    
    
    
    
class Locked_Door2(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, True, 2)
        self.doorType = 2

    def introText(self):
        if self.isLocked:
            return """A locked door stands to the North. This one has a gold handle.\n
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __ @|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
            """
        else:
            return "A now open door with a gold handle decorates the room.\nA passage opens to the North.\n"

    def adjacentMoves(self):
        possibleMoves = []
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x - 1, self.y):
            possibleMoves.append(actions.MoveWest())
        if world.tileExists(self.x, self.y - 1) and not self.isLocked:
            possibleMoves.append(actions.MoveNorth())
        if world.tileExists(self.x, self.y + 1):
            possibleMoves.append(actions.MoveSouth())
        return possibleMoves

    def availableActions(self):
        moves = self.adjacentMoves()
        list = [actions.ViewInventory(),
                actions.CallHelp(),
                actions.ViewSanity(),
                actions.UseItem(None),
                actions.UseItemTarget(None, None),
                actions.PickupItem(None)]
        moves.extend(list)
        return moves



class Locked_Door1(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, True, 1)
        self.doorType = 1

    def introText(self):
        if self.isLocked:
            return """A locked door stands to the South. This one has a brass handle.\n
            __________
           |  __  __  |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |  __  __ O|
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |  ||  | |
           | |__||__| |
           |__________|
            """
        else:
            return "A now open door with a brass handle decorates the room.\nA passage opens to the South.\n"

    def adjacentMoves(self):
        possibleMoves = []
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x - 1, self.y):
            possibleMoves.append(actions.MoveWest())
        if world.tileExists(self.x, self.y - 1):
            possibleMoves.append(actions.MoveNorth())
        if world.tileExists(self.x, self.y + 1) and not self.isLocked:
            possibleMoves.append(actions.MoveSouth())
        return possibleMoves

    def availableActions(self):
        moves = self.adjacentMoves()
        list = [actions.ViewInventory(),
                actions.CallHelp(),
                actions.ViewSanity(),
                actions.UseItem(None),
                actions.UseItemTarget(None, None),
                actions.PickupItem(None)]
        moves.extend(list)
        return moves

    

class Bad_Room(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Key1())
        self.item = items.Key1() #somehow room has no self.item
    def introText(self):
        if self.item:
            return """It smells like death and decay in here.
Your head grows foggier the longer you stay.\n
You quickly turn around to leave when you spot something shiny.
           __
          /O \_____
          \__/-="="`

It appears to be a key made of brass.
            """
        else:
            return"""It smells like death and decay in here.
Your head grows foggier the longer you stay.\n
There's nothing left in this room.
            """
    def modifyPlayer(self, player):
        player.sanity -= 10

    
class Lootway(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Trinket())
        self.item = items.Trinket()
    def introText(self):
        if self.item:
            return """At the end of this hallway you spot a small item.
Upon closer inspection, it appears to be a trinket.
            """
        else:
            return"""You stand in an empty hallway.
            """

class Good_Choice(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Key2())
        self.item = items.Key2()
    def introText(self):
        if self.item:
            return """You appear unharmed.\n
           __
          /@ \_____
          \__/-="="`

You notice in the corner a small key made of gold.
        """
        else:
            return"""
Without the golden key, the room looks wholly empty.
            """
