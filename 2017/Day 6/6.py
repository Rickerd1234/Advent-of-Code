# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def distribute(blocks):
    max_block = max(blocks)
    index = blocks.index(max_block)
    block_count = len(blocks)
    all = max_block // block_count
    rest = max_block % block_count
    blocks[index] = 0
    for i in range(index+1,block_count):
        if rest > 0:
            blocks[i] += all + 1
            rest -= 1
        else:
            blocks[i] += all
    for i in range(index+1):
        if rest > 0:
            blocks[i] += all + 1
            rest -= 1
        else:
            blocks[i] += all

# Part 1
def p1(inp):
    blocks = [int(i) for i in inp[0].split("\t")]
    known = [str(blocks)]
    i = 0
    while True:
        distribute(blocks)
        i += 1
        new = str(blocks)
        if new in known:
            break
        known.append(new)
    print(i)
    return known, new

# Part 2
def p2(inp, o1):
    known, new = o1
    ind = known.index(new)
    print(len(known) - ind)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)