# Imports
from collections import Counter
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

offsets = {
    "N" : (0,-1),
    "NE": (1,-1),
    "E":  (1,0),
    "SE": (1,1),
    "S":  (0,1),
    "SW": (-1,1),
    "W":  (-1,0),
    "NW": (-1,-1)
}
directions = [("N","NE","NW"), ("S", "SE", "SW"), ("W","NW","SW"), ("E","NE","SE")]
moves = ["N", "S", "W", "E"]


# Part 1 & 2
def p12(inp):
    elves = set([(x,y) for y, row in enumerate(inp) for x, spot in enumerate(row) if spot == "#"])

    for r in range(1500):
        proposals = {}
        new_elves = set()
        changed = False
        
        for (x,y) in elves:
            if not any((x+xo, y+yo) in elves for (xo,yo) in offsets.values()):
                new_elves.add((x,y))
                continue

            for i in range(4):
                d_i = (i+r) % 4
                if not any((x+offsets[d][0], y+offsets[d][1]) in elves for d in directions[d_i]):
                    xo, yo = offsets[moves[d_i]]
                    proposals[(x,y)] = (x+xo,y+yo)
                    break

            if (x,y) not in proposals:
                new_elves.add((x,y))

        prop_count = Counter(proposals.values())
        for elf, prop in proposals.items():            
            if prop_count[prop] == 1:
                new_elves.add(prop)
                changed = True
            else:
                new_elves.add(elf)
        
        elves = new_elves

        if r == 9:
            min_x, min_y = min(elves, key=lambda c: c[0])[0], min(elves, key=lambda c: c[1])[1]
            max_x, max_y = max(elves, key=lambda c: c[0])[0], max(elves, key=lambda c: c[1])[1]
            print((max_x-min_x+1)*(max_y-min_y+1) - len(elves))
        
        if not changed:
            print(r+1)
            break


# Run main functions
p12(inp)