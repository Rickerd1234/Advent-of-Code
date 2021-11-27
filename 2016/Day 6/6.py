with open("Day 6/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    msgs = inp.copy()
    dics = [{} for _ in range(len(msgs[0]))]
    for msg in msgs:
        for i, c in enumerate(msg):
            if c in dics[i]:
                dics[i][c] += 1
            else:
                dics[i][c] = 0
    print("".join([[k for k,v in d.items() if v == max(d.values())][0] for d in dics]))
    return

def p2(o1):
    msgs = inp.copy()
    dics = [{} for _ in range(len(msgs[0]))]
    for msg in msgs:
        for i, c in enumerate(msg):
            if c in dics[i]:
                dics[i][c] += 1
            else:
                dics[i][c] = 0
    print("".join([[k for k,v in d.items() if v == min(d.values())][0] for d in dics]))
    return

o1 = p1()
p2(o1)