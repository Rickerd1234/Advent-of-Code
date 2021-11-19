from itertools import permutations


with open("Day 9/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    data = []
    ulocs = []
    for route in inp:
        locs, dist = route.split(" = ")
        locs = locs.split(" to ")
        data.append((locs, int(dist)))

        if locs[0] not in ulocs:
            ulocs.append(locs[0])
        if locs[1] not in ulocs:
            ulocs.append(locs[1])
    
    n = len(ulocs)
    G = [[1000000 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        G[i][i] = 0
    
    for (a, b), d in data:
        ai, bi = ulocs.index(a), ulocs.index(b)
        G[ai][bi] = d
        G[bi][ai] = d

    shortest = 10000000000
    for perm in permutations(range(8)):
        cycle = [G[perm[i-1]][perm[i]] for i in range(n)]
        path = sum(cycle) - max(cycle)
        if path < shortest:
            shortest = path

    print(shortest)
    return G

def p2(o1):
    n = len(o1)
    longest = 0
    for perm in permutations(range(8)):
        cycle = [o1[perm[i-1]][perm[i]] for i in range(n)]
        path = sum(cycle) - min(cycle)
        if path > longest:
            longest = path
    print(longest)
    return

o1 = p1()
p2(o1)