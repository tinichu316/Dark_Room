import items


#non specific types of rooms (more than 1 exist)
class MapTile: #no parantheses since we aren't going to be subclassing
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def introText(self):
        raise NotImplementedError() # we don't want to actually create anything called a maptile so we have to override these methods in any of our other classes
    
    def modifyPlayer(self, player):
        raise NotImplementedError()
    

class LootRoom(MapTile):
    def __init__(self, x, y, item):
        self.item = item
        super().__init__(x, y)
        
    def addLoot(self, player):
        index = items.allItems.index(self.item)
        player.inventory[index] = 1
        
    #def modifyPlayer(self, player):
    #    pass
        


#specific rooms 
class Dark_Room(MapTile):
    def introText(self): #triple quotes span multiple lines
        return """ 
        You wake up to a slightly humid but otherwise dark room. \n
        The draft coming in from your front and your right indicates a narrow passageway.
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
        player.sanity -= 30
        
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
        You enter a room split into left and right directions.\n
        You have a feeling you will need to go into one room,\n
        but you also sense that the other room will lead to harm.
        """
    
    def modifyPlayer(self, player):
        pass
    