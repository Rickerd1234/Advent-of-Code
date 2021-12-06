with open("Day 6/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def passDay(td):
    new_td = {6:0, 8:0}
    for t, c in td.items():
        if t == 0:
            new_td[8] += c
            new_td[6] += c
        else:
            if t-1 in new_td:
                new_td[t-1] += c
            else:
                new_td[t-1] = c
    return new_td

def p1():
    timers = [int(t) for t in inp[0].split(",")]
    td = {}
    for t in timers:
        if t in td:
            td[t] += 1
        else:
            td[t] = 1
    
    for _ in range(80):
        td = passDay(td)
    print(sum(td.values()))
    return timers

def p2(o1):
    timers = o1
    td = {}
    for t in timers:
        if t in td:
            td[t] += 1
        else:
            td[t] = 1

    for _ in range(256):
        td = passDay(td)
    print(sum(td.values()))
    return

o1 = p1()
p2(o1)