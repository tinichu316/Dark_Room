#store needed commands here
# examine/x
# take/grab
# go/g
# use ___ with ___
# help (calls for help)
# commands
# look/l (describes the surroundings)
# inventory/i (gives a list of the items in the inventory)
# save
# load
# sanity
# quit (saves then quits)

import math

def displaySanity(percent):
    bar = ["-"]*20
    responses = {0: " are about to die.", 1: "r heart is beating like crazy.", 2: " begin to see hallucinations.", 3: " feel increasingly dizzy.", 4: " have a slight headache.", 5: " feel just fine."}
    if percent <= 100:
        resp = math.ceil((percent-10)/20)        
        for i in range(math.ceil(percent/5)):
            bar[i] = "|"
        
    else:
        resp = 5        
        bar = ["|"]*20
    health = "".join(bar)
    
    print("Sanity: [" + health + "] (%s%%)        You%s" %(percent, responses[resp]))



