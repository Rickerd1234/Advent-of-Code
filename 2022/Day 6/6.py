# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = file.read().strip("\n")


def findMarker(string, length):
    rolling_window = list(string[:length])
    for i, c in enumerate(string[length:], length):
        if len(set(rolling_window)) == length:
            return i

        rolling_window[i % length] = c


# Part 1
def p1(inp):
    print(findMarker(inp, 4))

# Part 2
def p2(inp, _):
    print(findMarker(inp, 14))


# Run main functions
o1 = p1(inp)
p2(inp, o1)