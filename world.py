_world = {}
startingPosition = (0, 0)

#have the player move based on cardinal directions.

def loadTiles():
    with open("resources/map.txt", 'r') as f:
        rows = f.readlines()
    #makes the first row into an array split by tab characters then finds the length of that
    print(rows[0].split("#"))
    xMax = len(rows[0].split("#")) 
    
    for y in range(len(rows)):
        cols = rows[y].split("#") #array along a row 
        print(cols)
        for x in range(xMax):
            tileName = cols[x].replace('\n','')
            #if tileName == "DarkRoom":
                #global startingPosition = (x, y)
            #getattr goes into the tiles.py file and finds a file with the name equal to that on the txt file
            _world[(x,y)] = None if tileName == '' else getattr(__import__("tiles"), tileName)(x, y)
            
def tile_exists(x, y):
    return _world.get((x, y))