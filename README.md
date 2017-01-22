# Introduction
'Dark Room' is a text-based adventure game built solely in Python. It was heavily modified from an online tutorial from:
http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/




## Commands:
+ n, s, e, w: Move in the cardinal directions.
+ pickup: Pickup an item.
+ use: Use an item.
+ usewith: Use an item with something.
+ h: Help.
+ q: Checks your current sanity.
+ save: Saves the current game and overrides the previous save.



## Features:
+ A menu system,
+ Multiple room types including a room with items, a locked door, and a room with a key,
+ Multiple items that can be both used and used with an object such as a key or trinket,
+ Sanity or Health meter that slowly drains as the player takes more and more time,
+ Multiple endings depending on the player's final sanity,
+ A save and load system that can save to a .txt file,
+ A method that asks and stores the player's name,
+ Various ASCII images for special rooms.



## Limitations:
+ Only one save file can be used at a time,
+ Rooms can contain at most one item,
+ Saving and loading will allow the user to pickup an item or visit a room 'for the first time' again,
+
