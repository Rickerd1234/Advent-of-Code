# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    value = 1
    cycle = 0
    interesting = 0
    for instr in inp:
        if instr == "noop":
            queue = [0]
        elif instr.startswith("addx"):
            queue = [0, int(instr.split(" ")[1])]

        for inc in queue:
            cycle += 1
            value += inc

            if cycle % 40 == 19:
                interesting += value * (cycle+1)

    print(interesting)

# Part 2
def p2(inp, _):
    value = 1
    cycle = 0
    screen = ""
    for instr in inp:
        if instr == "noop":
            queue = [0]
        elif instr.startswith("addx"):
            queue = [0, int(instr.split(" ")[1])]

        for inc in queue:
            if (abs(value - cycle)) <= 1:
                screen += "██"
            else:
                screen += "  "

            cycle += 1
            value += inc
            if cycle > 39:
                cycle = 0
                screen += "\n"

    print(screen)


# Run main functions
o1 = p1(inp)
p2(inp, o1)