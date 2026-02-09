with open("Day 11/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def isLegal(overview):
    for floor in overview:
        chips = [c[0].split("-")[0] for c in floor if c[1] == "microchip"]
        gens = [g[0] for g in floor if g[1] == "generator"]
        unsafe = [c for c in chips if c not in gens]
        if len(unsafe) > 0 and len(gens) > 0:
            return False
    return True

def p1():
    floors = inp.copy()
    overview = [[] for _ in floors]
    for f, floor in enumerate(floors):
        _, items = floor.split(" contains ")
        if items == "nothing relevant":
            continue
        else:
            if " and " in items:
                rest, last = items.split(" and ")
                stuff = rest.split(", ") + [last]
                stuff = [tuple(s[2:].split(" ")) for s in stuff]
                for s in stuff:
                    overview[f].append(s)
    
    return

def p2(o1):
    return

o1 = p1()
p2(o1)