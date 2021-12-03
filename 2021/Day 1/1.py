with open("Day 1/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    ms = [int(m) for m in inp]
    c = 0
    prev = ms[0]
    for m in ms[1:]:
        if m > prev:
            c += 1
        prev = m
    print(c)
    return ms

def p2(o1):
    ms = o1
    c = 0
    for i, m in enumerate(ms[3:]):
        if m > ms[i]:
            c += 1
    print(c)
    return

o1 = p1()
p2(o1)