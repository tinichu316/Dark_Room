import player


class Action():
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    #when you call the class it prints out what that action is
    def __str__(self):
        return "%s: %s." %(self.hotkey, self.name)


class MoveNorth(Action):
    def __init__(self):
        super().__init__(method = player.move_north,
                         name = "Go North",
                         hotkey = "n",
                         )
class MoveSouth(Action):
    def __init__(self):
        super().__init__(method = player.move_south,
                         name = "Move South",
                         hotkey = "s",
                         )
class MoveEast(Action):
    def __init__(self):
        super().__init__(method = player.move_east,
                         name = "Walk East",
                         hotkey = "e",
                        )
class MoveWest(Action):
    def __init__(self):
        super().__init__(method = player.move_west,
                         name = "Travel West",
                         hotkey = "w",
                        )

class ViewInventory(Action):
    #prints the player's inventory
    def __init__(self):
        super().__init__(method = player.printInventory,
                         name = "View Inventory",
                         hotkey = "i"
                         )

class ViewSanity(Action):
    def __init__(self):
        super().__init__(method = player.printSanity,
                         name = "Check Sanity",
                         hotkey = "q"
                         )

class CallHelp(Action):
    def __init__(self):
        super().__init__(method = player.callHelp,
                         name = "Call for Help",
                         hotkey = "h"
                         )

class UseItem(Action):
    def __init__(self):
        super().__init__(method = player.useItem,
                         name = "Use an item",
                         hotkey = "u",
                         item = item
                         ) #this action will have to passed an arg

class UseItemTarget(Action):
    def __init__(self):
        super().__init__(method = player.useItemTarget,
                         name = "Use an item with something",
                         hotkey = "uw",
                         item = item,
                         target = target
                         ) #this action will have to passed an arg