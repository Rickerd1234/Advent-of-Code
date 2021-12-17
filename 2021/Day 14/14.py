with open("Day 14/inp.txt", "r") as file:
    start, rules = file.read().split("\n\n")
    rules = [line for line in rules.split("\n")]

from math import ceil

def step(poly, rd):
    new = ""
    if poly[1] == " ":
        return poly[0]

    for i in range(1, len(poly)):
        pair = poly[i-1:i+1]
        if pair in rd:
            new += pair[0] + rd[pair]
        else:
            new += pair[0]

    return new

def counter(poly, m = 1):
    c = {}
    for v in poly:
        if v in c:
            c[v] += m
        else:
            c[v] = m
    return c

def pairCounter(poly, m = 1):
    c = {}
    for i in range(1, len(poly)):
        v = poly[i-1:i+1]
        if v in c:
            c[v] += m
        else:
            c[v] = m
    return c

def smartStep(pcs, rd):
    new = {}

    for k,v in pcs.items():
        npc = pairCounter(step(k + " ", rd), v)
        new = combCounts(new, npc)
    
    return new

def combCounts(A, B):
    return {x: A.get(x, 0) + B.get(x, 0) for x in set(A).union(B)}


def p1():
    rd = {}
    for rule in rules:
        s, t = rule.split(" -> ")
        rd[s] = t

    poly = start
    for _ in range(10):
        poly = step(poly + " ", rd)
    counts = counter(poly)

    maxv = max(counts.values())
    minv = min(counts.values())
    print(maxv-minv)
    return rd

def p2(o1):
    poly = pairCounter(start)
    for _ in range(40):
        poly = smartStep(poly, o1)
        
    counts = {}
    for k,v in poly.items():
        for l in k:
            if l in counts:
                counts[l] += v
            else:
                counts[l] = v

    counts = {k: ceil(v/2) for k, v in counts.items()}

    maxv = max(counts.values())
    minv = min(counts.values())
    print(maxv-minv)
    return

o1 = p1()
p2(o1)