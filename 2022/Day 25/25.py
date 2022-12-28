# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

factor_map = {
    "2":2,
    "1":1,
    "0":0,
    "-":-1,
    "=":-2
}

def s2i(num):
    return sum(factor_map[c] * (5**(len(num)-i-1)) for i, c in enumerate(num))

def reduceDigit(s, i, num):
    pre = s[:i]
    post = s[i+1:]
    cur = s
    for cv in factor_map.keys():
        nxt =  pre + cv + post
        if s2i(nxt) >= num:
            cur = nxt
        else:
            return cur
    return cur

def i2s(num):
    out = "2"
    while s2i(out) < num:
        out += "2"

    i = 0
    while s2i(out) > num:
        out = reduceDigit(out, i, num)
        i += 1

    return out

# Part 1
def p1(inp):
    print(i2s(sum(s2i(num) for num in inp)))

# Run main functions
p1(inp)