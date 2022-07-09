# Imports
from math import ceil
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    i = int(inp[0])
    ring = ceil((i**(1/2) - 1) / 2)
    if i == 1:
        ring_size = 0
    else:
        ring_size = 2*ring - 1
    inner = (ring_size)**2
    ring_travel = min((i - inner - ring) % (ring_size+1), (inner - i - ring) % (ring_size+1))
    print(ring_travel + ring)
    return i

def neighborSum(grid, x,y):
    offset = (-1,0,1)
    s = 0
    for ox in offset:
        for oy in offset:
            s += grid[y+oy][x+ox]
    return s

# Part 2
def p2(inp, o1):
    s = 11
    c = s//2
    grid = [[0 for _ in range(s)] for _ in range(s)]

    grid[c][c] = 1
    x,y = c+1,c
    next_pos = (1,0)
    dir_map = {
            (1,0):(0,-1),
            (0,-1):(-1,0),
            (-1,0):(0,1),
            (0,1):(1,0),
        }
    i = 0
    while i < (s-2)**2 - 1:
        new_value = neighborSum(grid, x,y)
        if new_value > o1:
            print(new_value)
            break

        grid[y][x] = new_value
        nx,ny = dir_map[next_pos]
        x,y = x+nx,y+ny
        if grid[y][x] != 0:
            x,y = x-nx,y-ny
            nx,ny = next_pos
            x,y = x+nx,y+ny
        next_pos = (nx,ny)
        i += 1

    # for row in grid:
    #     print(*row, sep="\t")
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)