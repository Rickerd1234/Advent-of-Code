with open("Day 20/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def score(v):
    return sum(factors(v)) * 10

def p1():
    t = int(inp[0])
    i = 1
    while score(i) <= t:
        i += 1
    print(i)
    return

def score2(v):
    facs = [f for f in factors(v) if f * 50 >= v]
    return sum(facs) * 11

def p2(o1):
    t = int(inp[0])
    i = 1
    while score2(i) <= t:
        i += 1
    print(i)
    return

o1 = p1()
p2(o1)