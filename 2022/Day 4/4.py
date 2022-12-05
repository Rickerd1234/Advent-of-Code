# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    c = 0
    for pair in inp:
        e1, e2 = (list(map(int, e.split("-"))) for e in pair.split(","))

        if (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e1[0] <= e2[0] and e1[1] >= e2[1]):
            c += 1
    print(c)
    return inp

# Part 2
def p2(inp, _):
    c = 0
    for pair in inp:
        e1, e2 = (list(map(int, e.split("-"))) for e in pair.split(","))
        e1, e2 = set(range(e1[0], e1[1]+1)), set(range(e2[0], e2[1]+1))

        if e1 & e2:
            c += 1
    print(c)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)