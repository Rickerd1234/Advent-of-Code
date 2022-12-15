# Imports
from functools import cmp_to_key
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = file.read().split("\n\n")
    inp = [tuple(map(eval, packet.split("\n"))) for packet in inp]


def isOrdered(pack_a, pack_b):
    while pack_a and pack_b:
        val_a, *pack_a = pack_a
        val_b, *pack_b = pack_b
        if type(val_a) == type(val_b):
            if type(val_a) == int:
                if val_a == val_b:
                    continue
                else:
                    return val_a < val_b
            elif type(val_a) == list:
                result = isOrdered(val_a, val_b)
                if result is not None:
                    return result
        else:
            if type(val_a) == int: val_a = [val_a]
            elif type(val_b) == int: val_b = [val_b]
            result = isOrdered(val_a, val_b)
            if result is not None:
                return result
    if pack_a: return False
    elif pack_b: return True
    return None



# Part 1
def p1(inp):
    print(sum(i+1 if isOrdered(pack_a, pack_b) else 0 for i, (pack_a, pack_b) in enumerate(inp)))
    return inp

# Part 2
def p2(inp, o1):
    div1 = [[2]]
    div2 = [[6]]
    packets = [div1, div2]
    for pack_a, pack_b in inp:
        packets.append(pack_a)
        packets.append(pack_b)
    cmpFunc = lambda x,y: -1 if isOrdered(x,y) else 1
    packets.sort(key=cmp_to_key(cmpFunc))
    i1, i2 = packets.index(div1) + 1, packets.index(div2) + 1
    print(i1*i2)


# Run main functions
o1 = p1(inp)
p2(inp, o1)