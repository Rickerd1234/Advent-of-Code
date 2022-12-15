# Imports
from collections import deque
import math
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


def DijkstraFind(dist_map):
    width, height = len(inp[0]), len(inp)
    queue = deque(spot for spot in dist_map if spot[3] == 0)
    while queue:
        cx,cy,cv,cd = queue.popleft()

        if cv == "E":
            return cd

        for xo, yo in [(-1,0),(0,1),(1,0),(0,-1)]:
            tx, ty = xo + cx, yo + cy
            if tx in range(width) and ty in range(height):
                *_, tv, td = dist_map[tx + ty*width]
                if td > cd+1 and (ord(tv) <= ord(cv)+1) :
                    dist_map[tx + ty*width] = (tx,ty,tv,cd+1)
                    queue.append(dist_map[tx + ty*width])

# Part 1
def p1(inp):
    dist_map = [(x,y,val,math.inf) if val != "S" else (x,y,"a",0) for y,row in enumerate(inp) for x,val in enumerate(row)]
    print(DijkstraFind(dist_map))

# Part 2
def p2(inp, _):
    dist_map = [(x,y,val,math.inf) if val != "S" and val != "a" else (x,y,"a",0) for y,row in enumerate(inp) for x,val in enumerate(row)]
    print(DijkstraFind(dist_map))


# Run main functions
o1 = p1(inp)
p2(inp, o1)