# Imports
from sys import argv
from os.path import dirname
import sympy as sym


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n").split(": ") for line in file]

op_dict = {
    "+": lambda x,y: x+y,
    "-": lambda x,y: x-y,
    "*": lambda x,y: x*y,
    "/": lambda x,y: x/y
}

def solveSystem(monkeys, unknown):
    while len(unknown) > 0:
        for monkey in list(unknown):
            left, op, right = monkeys[monkey]
            if left in unknown or right in unknown:
                continue
        
            monkeys[monkey] = op(monkeys[left], monkeys[right])
            unknown.remove(monkey)
    return monkeys

# Part 1
def p1(inp):
    monkeys = {}
    unknown = set()
    for (monkey, job) in inp:
        if job.isnumeric():
            monkeys[monkey] = int(job)
            continue

        left, op, right = job.split(" ")
        monkeys[monkey] = (left, op_dict[op], right)
        unknown.add(monkey)
    
    pt2 = monkeys.copy(), unknown.copy()
    
    print(int(solveSystem(monkeys, unknown)["root"]))

    return pt2

# Part 2
def p2(_, o1):
    monkeys, unknown = o1

    old_root = monkeys["root"]
    monkeys["root"] = (old_root[0], lambda x,y: x-y, old_root[2])
    monkeys["humn"] = sym.symbols('humn')
    
    print(int(round(sym.solve(solveSystem(monkeys, unknown)["root"])[0], 0)))


# Run main functions
o1 = p1(inp)
p2(inp, o1)