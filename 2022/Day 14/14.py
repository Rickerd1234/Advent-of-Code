# Imports
import math
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    walls = set()
    lowest = -math.inf
    for line in inp:
        segments = list(map(lambda coord: map(int, coord.split(",")), line.split(" -> ")))
        x, y = segments[0]
        for nx,ny in segments[1:]:
            sx = 1 if nx > x else -1
            sy = 1 if ny > y else -1
            for px in range(x,nx+sx,sx):
                for py in range(y,ny+sy,sy):
                    walls.add((px,py))
                    lowest = max(lowest, py)
            x,y = nx,ny

    start_pos = (500,0)
    sand = set()
    x,y = start_pos
    while True:
        sdown = (x,y+1)
        sleft = (x-1,y+1)
        sright = (x+1,y+1)
        if sdown not in walls and sdown not in sand:
            x,y = sdown
        elif sleft not in walls and sleft not in sand:
            x,y = sleft
        elif sright not in walls and sright not in sand:
            x,y = sright
        else:
            # Source is blocked
            if (x,y) == start_pos:
                break
            sand.add((x,y))
            x,y = start_pos

        # This sand will fall infinitely
        if y > lowest:
            break

    print(len(sand))
    return walls, lowest

# Part 2
def p2(_, o1):
    walls, lowest = o1

    start_pos = (500,0)
    sand = set()
    x,y = start_pos
    while True:
        sdown = (x,y+1)
        sleft = (x-1,y+1)
        sright = (x+1,y+1)
        reached_bottom = sdown[1] == lowest + 2
        if sdown not in walls and sdown not in sand and not reached_bottom:
            x,y = sdown
        elif sleft not in walls and sleft not in sand and not reached_bottom:
            x,y = sleft
        elif sright not in walls and sright not in sand and not reached_bottom:
            x,y = sright
        else:
            sand.add((x,y))
            # Source is blocked
            if (x,y) == start_pos:
                break
            x,y = start_pos

    print(len(sand))
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)