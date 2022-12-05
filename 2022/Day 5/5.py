# Imports
import copy
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = file.read().split("\n\n")


# Part 1
def p1(inp):
    crates, moves = inp
    stacks = {}
    for line in reversed(crates.split("\n")):
        for i, v in enumerate(line):
            if v.isnumeric():
                stacks[int(v)] = []

            elif v.isalpha():
                ind = len(range(0,i,4))
                stacks[ind].append(v)
    stacks_copy = copy.deepcopy(stacks)

    for move in moves.split("\n"):
        move, target = move.split(" to ")
        count, source = move[5:].split(" from ")
        count, source, target = map(int, (count, source, target))
        
        while count:
            moved = stacks[source].pop()
            stacks[target].append(moved)
            count -= 1

    print("".join([v[-1] for v in stacks.values()]))
    return stacks_copy, moves

# Part 2
def p2(inp, o1):
    stacks, moves = o1
    for move in moves.split("\n"):
        move, target = move.split(" to ")
        count, source = move[5:].split(" from ")
        count, source, target = map(int, (count, source, target))
        
        moved = stacks[source][-count:]
        stacks[source] = stacks[source][:-count]
        stacks[target] += moved

    print("".join([v[-1] for v in stacks.values()]))
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)