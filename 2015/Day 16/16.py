with open("Day 16/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

known = '''children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1'''

def score(pot, known):
    s = 0
    for k, v in pot.items():
        if known[k] == v:
            s += 1
    return s

def p1():
    known_dict = {}
    for line in known.split("\n"):
        k, v = line.split(": ")
        known_dict[k] = int(v)

    aunt_info = {}
    for aunt in inp:
        id, info = aunt.split(": ", 1)
        id = int(id[4:])
        data = info.split(", ")
        aunt_info[id] = {}
        for kv in data:
            key, value = kv.split(": ")
            aunt_info[id][key] = int(value)
    
    best = (-1, -1)
    for k,v in aunt_info.items():
        scr = score(v, known_dict)
        if scr > best[1]:
            best = (k, scr)

    print(best[0])
    return known_dict, aunt_info

def score2(p, c):
    s = 0
    for k, v in p.items():
        if k in ["cats", "trees"]:
            if c[k] < v:
                s += 1
        elif k in ["pomeranians", "goldfish"]:
            if c[k] > v:
                s += 1
        else:
            if c[k] == v:
                s += 1
    return s

def p2(o1):
    kn_dic, aunt_dict = o1

    best = (-1, -1)
    for k,v in aunt_dict.items():
        scr = score2(v, kn_dic)
        if scr > best[1]:
            best = (k, scr)
    
    print(best[0])
    return

o1 = p1()
p2(o1)