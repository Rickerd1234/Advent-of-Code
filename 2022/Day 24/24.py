# Imports
from collections import deque
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]
    hor_blizzard_set = set()
    ver_blizzard_set = set()
    width, height = len(inp[0])-2, len(inp)-2
    for y, row in enumerate(inp):
        y -= 1
        for x, spot in enumerate(row): 
            x -= 1
            if spot == "<":
                for i in range(width):
                    nx = (x-i) % width
                    i %= width
                    hor_blizzard_set.add((nx,y,i))
            elif spot == ">":
                for i in range(width):
                    nx = (x+i) % width
                    i %= width
                    hor_blizzard_set.add((nx,y,i))

            elif spot == "^":
                for i in range(height):
                    ny = (y-i) % height
                    i %= height
                    ver_blizzard_set.add((x,ny,i))
            
            elif spot == "v":
                for i in range(height):
                    ny = (y+i) % height
                    i %= height
                    ver_blizzard_set.add((x,ny,i))
    inp = width, height, hor_blizzard_set, ver_blizzard_set
    

# Part 1 & 2
def p12(inp):
    width, height, hor_blizzard_set, ver_blizzard_set = inp
    
    targets = [(width-1, height), (0,-1), (width-1, height)]
    max_t_i = 0

    visited = set()
    queue = deque([(0,-1,0,0)])
    found_pt1 = False
    while queue:
        x,y,t,t_i = queue.popleft()
        if t_i < max_t_i: continue

        for xo,yo in [(1,0),(0,1),(0,-1),(-1,0),(0,0)]:
            nx, ny = x+xo, y+yo
            if (nx,ny) == targets[t_i]:
                if not found_pt1:
                    found_pt1 = True
                    print(t+1)
                if t_i == len(targets) - 1:
                    print(t+1)
                    return
                max_t_i = max(max_t_i, t_i+1)
                visited.add((nx,ny,t+1,t_i+1))
                queue.append((nx,ny,t+1,t_i+1))
            if 0 <= nx < width and 0 <= ny < height or (nx,ny) in {(0,-1), (width-1, height)}:
                if (nx, ny, (t+1)%height) in ver_blizzard_set or (nx, ny, (t+1)%width) in hor_blizzard_set or (nx, ny, t+1, t_i) in visited:
                    continue
                visited.add((nx, ny, t+1, t_i))
                queue.append((nx, ny, t+1, t_i))


# Run main functions
p12(inp)