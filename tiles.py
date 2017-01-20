import items, actions, world


#non specific types of rooms (more than 1 exist)
class MapTile():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def introText(self):
        raise NotImplementedError() # we don't want to actually create anything called a maptile so we have to override these methods in any of our other classes
    
    def modifyPlayer(self, player):
        raise NotImplementedError()

    def adjacentMoves(self):
        # returns possible move actions
        #maybe add locked door blocking here?
        possibleMoves = []
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        if world.tileExists(self.x + 1, self.y):
            possibleMoves.append(actions.MoveEast())
        return possibleMoves

    def availableActions(self):
        moves = self.adjacentMoves(self)
        #list the possible extra moves. Doesn't list use but you can always try that.
        list = [actions.ViewInventory(),
                actions.CallHelp(),
                actions.ViewSanity()]
        moves.extend(list)
        return moves

    

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def pickup(self, player):
        index = items.allItems.index(self.item)
        player.inventory[index] = 1
        items.updateInventory()
        
        
    #idk if we need this next part...
    #def modifyPlayer(self, player):
    #    pass


#this type of room, like the two above it, need to be passed an x and y coordinate of a specific locked room
#player can enter this room but can't pass unless it's unlocked
class LockedRoom(MapTile):
    def __init__(self, x, y, isLocked, doorType):
        self.isLocked = isLocked
        self.doorType = doorType
        super().__init__(x, y)
        
    def unlock():
        #unlocks the door
        self.isLocked = False

#===============================================================================
#specific rooms 
class Dark_Room(MapTile):
    def introText(self): #triple quotes span multiple lines
        return """ 
        You wake up to a slightly humid but otherwise dark room. \n
        The draft coming in from the North and East indicates a narrow passageway.
        """
    
    def modifyPlayer(self, player):
        # Room does nothing
        pass    
    
    
class Hallway(MapTile):
    def introText(self): #triple quotes span multiple lines
        return """ 
        You walk into the passageway.
        """

    def modifyPlayer(self, player):
        pass
    
    
class Bad_Choice(MapTile):
    def introText(self):
        return """
        A sense of dread overcomes you as you enter this room.\n
        Your legs feel heavy and your head grows dizzier.\n
        Your take lumbering steps before you crash to the ground.\n
        .\n
        ..\n
        ...\n
        You awake covered in slime and cockroaches.\n
        Your sanity has taken a large hit.
        """
    
    def modifyPlayer(self, player):
        player.sanity -= 40
        #displaySanity()
        
        
class Front_Door(MapTile):
    def introText(self):
        return """
        You made it out! Congratulations!
        """
    
    def modifyPlayer(self, player):
        player.victory = True
        
class Choice_Room(MapTile):
    def introText(self):
        return """
        You enter a room split into North and South directions.\n
        You have a feeling you will need to go into one room,\n
        but you also sense that the other room will lead to harm.
        """
    
    def modifyPlayer(self, player):
        pass
    
class Loot_Dirty(MapTile):
    def introText(self):
        return """
        As you enter, a strong scent of cinnamon and pumpkin spice hits you.\n
        You see a gorgeous looking lattee and you can't help but devour it.\n
        You feel better after that.
        """
    def modifyPlayer(self, player):
        player.sanity += 20
        #displaySanity()

    
    
    
    
class Locked_Door2(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, True, 2)
    def introText(self):
        if self.isLocked:
            return """
            A locked door stands in your way. This one has a gold handle.
            """
        else:
            return """
            A once locked door with a gold handle decorates the room.
            """
    
    def modifyPlayer(self, player):
        #block the player if they try to go north
        pass

class Locked_Door1(LockedRoom):
    def __init__(self, x, y):
        super().__init__(x, y, True, 1)
    def introText(self):
        if self.isLocked:
            return """
            A locked door stands in your way. This one has a brass handle.
            """
        else:
            return """
            A once locked door with a brass handle decorates the room.
            """
    
    def modifyPlayer(self, player):
        #block the player if they try to go south
        pass
    
    
    
    

class Bad_Room(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Key1())
    def introText(self):
        return """
        It smells like death and decay in here.\n
        You quickly turn around to leave when you spot something shiny.\n
        It appears to be a key.
        """
    #can use Bad_Room.pickup(player) to pickup the key1
      
    
class Lootway(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Trinket())
    def introText(self):
        return """
        At the end of this hallway you spot a small item.\n
        Upon closer inspection, it appears to be a trinket.
        """
    #can use Lootway.pickup(player)
    
class Good_Choice(LootRoom):
    def __init__(self, x, y):
        super().__init__(x, y, items.Key2())
    def introText(self):
        return """
        You appear unharmed.\n
        You notice in the corner a small golden key.
        """
    #can use Good_Choice.pickup(player)
