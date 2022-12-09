# Imports
import math
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    visible_grid = [[False for _ in row] for row in inp]
    height, width = len(inp), len(inp[0])
    y_ranges = [(0,height,1),(height-1,-1,-1)]
    x_ranges = [(0,width,1),(width-1,-1,-1)]

    # Check vertical perspectives
    for yr in y_ranges:
        for x in range(*x_ranges[0]):
            max = -1
            for y in range(*yr):
                tree = int(inp[y][x])
                # Track the max spotted height and update this tree on the grid
                if tree > max:
                    visible_grid[y][x] = True
                    max = tree

    # Check horizontal perspectives
    for xr in x_ranges:
        for y in range(*y_ranges[0]):
            max = -1
            for x in range(*xr):
                tree = int(inp[y][x])
                # Track the max spotted height and update this tree on the grid
                if tree > max:
                    visible_grid[y][x] = True
                    max = tree

    print(sum(sum(vis for vis in row) for row in visible_grid))

# Part 2
def p2(inp, _):
    max = 0
    height, width = len(inp), len(inp[0])
    for y in range(height):
        for x in range(width):
            tree_height = int(inp[y][x])
            dirs = []

            # Compute Scenic Score
            for offset in [(0,1),(0,-1),(1,0),(-1,0)]:
                xo, yo = x, y
                current = 0

                # Completely scan one direction
                while xo + offset[0] in range(width) and yo + offset[1] in range(height):
                    # Update position and count
                    xo += offset[0]
                    yo += offset[1]
                    current += 1
                    # We spot the blocking tree, so stop going this direction
                    if int(inp[yo][xo]) >= tree_height:
                        break
                dirs.append(current)

            score = math.prod(dirs)

            # Compare to max
            if score > max:
                max = score

    print(max)


# Run main functions
o1 = p1(inp)
p2(inp, o1)