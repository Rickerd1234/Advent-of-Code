# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    insts = [int(i) for i in inp]
    p = 0
    i = 0
    while 0 <= p < len(insts):
        jump = insts[p]
        insts[p] = jump + 1
        p += jump
        i += 1
    print(i)
    return insts

# Part 2
def p2(inp, o1):
    insts = [int(i) for i in inp]
    p = 0
    i = 0
    while 0 <= p < len(insts):
        jump = insts[p]
        if jump >= 3:
            insts[p] = jump - 1
        else:
            insts[p] = jump + 1
        p += jump
        i += 1
    print(i)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)