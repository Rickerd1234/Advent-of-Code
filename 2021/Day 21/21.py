from collections import Counter
from typing import DefaultDict
from itertools import permutations
from functools import cache

with open("Day 21/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def throw(player, die):
    for _ in range(3):
        player += die
        die += 1
        if die > 100:
            die = 1
    return player, die

def score(player):
    return player % 10 if player % 10 > 0 else 10

def p1():
    p0, p1 = [int(s.rsplit(" ",1)[1]) for s in inp]
    s0, s1 = 0, 0
    die = 1
    dc = 0
    target = 1000
    while s1 < target:
        p0, die = throw(p0 % 10, die)
        dc += 3
        s0 += score(p0)
        if s0 >= target:
            break

        p1, die = throw(p1 % 10, die)
        dc += 3
        s1 += score(p1)

    if s0 < s1:
        print(s0 * dc)
    else:
        print(s1 * dc)
    return

@cache
def playDirac(p0, p1, s0, s1, turn, scs, lim = 21):
    if s0 >= lim: return 1, 0
    elif s1 >= lim: return 0, 1

    wins_zero = 0 
    wins_one = 0
    if turn == 0:
        for throw, count in scs:
            zw, ow = playDirac((p0 + throw) % 10, p1, s0 + score(p0 + throw), s1, 1, scs, lim = lim)
            wins_zero += zw * count
            wins_one += ow * count
    else:
        for throw, count in scs:
            zw, ow = playDirac(p0, (p1 + throw) % 10, s0, s1 + score(p1 + throw), 0, scs, lim = lim)
            wins_zero += zw * count
            wins_one += ow * count
    return wins_zero, wins_one

def p2(o1):
    p0, p1 = [int(s.rsplit(" ",1)[1]) for s in inp]

    perms = set(permutations([1,1,1, 2,2,2, 3,3,3], 3))

    sim_counts = tuple((k,v) for (k,v) in Counter([sum(perm) for perm in perms]).items())
    w0, w1 = playDirac(p0,p1, 0,0, 0, sim_counts, lim = 21)

    if w0 > w1:
        print(w0)
    else:
        print(w1)
    return

o1 = p1()
p2(o1)