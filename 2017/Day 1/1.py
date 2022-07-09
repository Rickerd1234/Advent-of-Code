# Imports
from sys import argv
from os.path import dirname

from numpy import half


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    vals = [int(i) for i in inp[0]]
    s = 0
    if vals[-1] == vals[0]:
        s += vals[0]
    for c,n in zip(vals, vals[1:]):
        if c==n:
            s += c
    print(s)
    return s

# Part 2
def p2(inp, o1):
    vals = [int(i) for i in inp[0]]
    s = 0
    halfway = len(vals)//2
    first, second = vals[:halfway], vals[halfway:]
    for a,b in zip(first,second):
        if a==b:
            s += 2*a
    print(s)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)