# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    vals = [[int(v) for v in row.split("\t")] for row in inp]
    diffs = [max(row) - min(row) for row in vals]
    print(sum(diffs))
    return vals

# Part 2
def p2(inp, o1):
    s = 0
    for row in o1:
        for v in row:
            for w in row:
                if v % w == 0 and v != w:
                    s += v // w
    print(s)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)