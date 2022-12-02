# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line for line in file.read().split("\n\n")]


# Part 1
def p1(elves):
    calories = [sum(int(cal) for cal in elf.split("\n")) for elf in elves]
    print(max(calories))
    return calories

# Part 2
def p2(inp, calories):
    print(sum(sorted(calories, reverse=True)[0:3]))


# Run main functions
o1 = p1(inp)
p2(inp, o1)