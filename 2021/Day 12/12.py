with open("Day 12/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def findPaths(start, end, used, connections):
    paths = []
    possible = connections[start]
    for p in possible:
        if p.isupper() or p not in used:
            paths += [used.copy() + [p]]

    for path in paths:
        if path[-1] != end:
            new = findPaths(path[-1], end, path, connections)
            paths += [p for p in new if p not in paths]

    return [p for p in paths if p[-1] == end]


def findPaths2(start, end, used, connections, doubled):
    paths = []
    possible = connections[start]
    for p in possible:
        if p.isupper() or p not in used:
            paths += [(used.copy() + [p], doubled)]
        elif doubled == False and p != "start" and p != "end":
            paths += [(used.copy() + [p], True)]

    for path, double in paths:
        if path[-1] != end:
            new = findPaths2(path[-1], end, path, connections, double)
            paths += [(p, double) for p in new if p not in paths]

    return [p for p,d in paths if p[-1] == end]

def p1():
    conns = {}
    for conn in inp.copy():
        s,t = conn.split("-")
        if s in conns:
            conns[s] += [t]
        else:
            conns[s] = [t]
        if t in conns:
            conns[t] += [s]
        else:
            conns[t] = [s]
    
    print(len(findPaths("start", "end", ["start"], conns)))
    return conns

def p2(o1):
    conns = o1
    print(len(findPaths2("start", "end", ["start"], conns, False)))
    return

o1 = p1()
p2(o1)