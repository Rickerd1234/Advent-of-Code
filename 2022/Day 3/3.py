# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def getCommonPrio(strings):
    common = set(strings[0]).intersection(*strings[1:])
    rucksack_prio = ord(common.pop()) - ord("A")
    if rucksack_prio > 26:
        return rucksack_prio - 31
    else:
        return rucksack_prio + 27


# Part 1
def p1(inp):
    prio = 0
    for rucksack in inp:
        size = len(rucksack)
        p1, p2 = rucksack[:size//2], rucksack[size//2:]
        prio += getCommonPrio((p1, p2))
    print(prio)

# Part 2
def p2(inp, _):
    prio = 0
    for i in range(0, len(inp), 3):
        prio += getCommonPrio(inp[i:i+3])
    print(prio)


# Run main functions
o1 = p1(inp)
p2(inp, o1)