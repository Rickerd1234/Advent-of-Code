# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    return inp

# Part 2
def p2(inp, o1):
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)