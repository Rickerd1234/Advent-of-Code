with open("Day 19/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    split_index = inp.index("")
    repl, start = inp[:split_index], inp[split_index + 1]
    repl_dict = {}
    for r in repl:
        i, o = r.split(" => ")
        if i in repl_dict:
            repl_dict[i] = repl_dict[i] + [o]
        else:
            repl_dict[i] = [o]
    
    results = []
    for i, c in enumerate(start):
        if c in repl_dict:
            for o in repl_dict[c]:
                results.append(start[:i] + o + start[i+1:])

        if i < len(start) - 1:
            pair = c + start[i+1]
            if pair in repl_dict:
                for o in repl_dict[pair]:
                    results.append(start[:i] + o + start[i+2:])
    print(len(set(results)))
    return start, repl_dict

def p2(o1):
    med, repl = o1
    rev_repl = {}
    for k,vs in repl.items():
        for v in vs:
            if v in rev_repl:
                print("ERROR")
            else:
                rev_repl[v] = k

    c = 0
    while med != "e":
        for o, i in rev_repl.items():
            new = med.replace(o, i, 1)
            if new != med:
                med = new
                c += 1
    print(c)
    return

o1 = p1()
p2(o1)