with open("Day 13/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

from itertools import permutations

def p1():
    data = []
    persons = []
    for opi in inp:
        fr, score_to = opi[:-1].split(" would ")
        score, to = score_to.split(" happiness units by sitting next to ")
        score = int(score[5:]) if score[:4] == "gain" else -int(score[5:])
        data.append((fr, to, score))

        if fr not in persons:
            persons.append(fr)
        if to not in persons:
            persons.append(to)
    
    n = len(persons)
    G = [["Empty" for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        G[i][i] = 0
    
    for f, t, s in data:
        fi, ti = persons.index(f), persons.index(t)
        G[fi][ti] = s

    max_hap = -10000000000
    for perm in permutations(range(len(G))):
        cycle = [G[perm[i-1]][perm[i]] for i in range(n)]
        rev_cycle = [G[perm[i]][perm[i-1]] for i in range(n)]
        happiness = sum(cycle) + sum(rev_cycle)
        if happiness > max_hap:
            max_hap = happiness

    print(max_hap)
    return

def p2(o1):
    data = []
    persons = []
    for opi in inp:
        fr, score_to = opi[:-1].split(" would ")
        score, to = score_to.split(" happiness units by sitting next to ")
        score = int(score[5:]) if score[:4] == "gain" else -int(score[5:])
        data.append((fr, to, score))

        if fr not in persons:
            persons.append(fr)
        if to not in persons:
            persons.append(to)
    
    n = len(persons)
    G = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    
    for i in range(n):
        G[i][i] = 0
    
    for f, t, s in data:
        fi, ti = persons.index(f), persons.index(t)
        G[fi][ti] = s

    max_hap = -10000000000
    for perm in permutations(range(len(G))):
        cycle = [G[perm[i-1]][perm[i]] for i in range(n)]
        rev_cycle = [G[perm[i]][perm[i-1]] for i in range(n)]
        happiness = sum(cycle) + sum(rev_cycle)
        if happiness > max_hap:
            max_hap = happiness

    print(max_hap)
    return

o1 = p1()
p2(o1)