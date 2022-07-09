# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    out = sum([len(pp.split(" ")) == len(set(pp.split(" "))) for pp in inp])
    print(out)
    return inp

# Part 2
def p2(inp, o1):
    spps = [["".join(sorted(pw)) for pw in pp.split(" ")] for pp in inp]
    out = sum([len(pp) == len(set(pp)) for pp in spps])
    print(out)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)