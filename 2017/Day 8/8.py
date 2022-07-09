# Imports
from sys import argv
from os.path import dirname
from collections import defaultdict


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    registers = defaultdict(int)
    op_dict = {
        "dec": lambda a,b: a-b,
        "inc": lambda a,b: a+b
    }
    cond_dict = {
        ">=": lambda a,b: a>=b,
        "<=": lambda a,b: a<=b,
        "==": lambda a,b: a==b,
        "!=": lambda a,b: a!=b,
        "<": lambda a,b: a<b,
        ">": lambda a,b: a>b
    }
    for line in inp:
        inst, cond = line.split(" if ")
        reg, op, val = inst.split(" ")
        cond_reg, cond_op, cond_val = cond.split(" ")

        if cond_dict[cond_op](registers[cond_reg], int(cond_val)):
            registers[reg] = op_dict[op](registers[reg], int(val))
    print(registers[max(registers, key=registers.get)] )
    return op_dict, cond_dict

# Part 2
def p2(inp, o1):
    registers = defaultdict(int)
    op_dict, cond_dict = o1
    max_reg = 0
    for line in inp:
        inst, cond = line.split(" if ")
        reg, op, val = inst.split(" ")
        cond_reg, cond_op, cond_val = cond.split(" ")

        if cond_dict[cond_op](registers[cond_reg], int(cond_val)):
            registers[reg] = op_dict[op](registers[reg], int(val))
            curr_max = registers[max(registers, key=registers.get)]
            if curr_max > max_reg:
                max_reg = curr_max
    print(max_reg)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1) 