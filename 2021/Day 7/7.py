with open("Day 7/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def optMove(locs):
    ls = locs.copy()
    opt = sum(ls)
    p = 0
    for _ in range(min(ls), max(ls)):
        p += 1
        new = sum([abs(l - p) for l in locs])

        if new < opt:
            opt = new
    return opt

def optMove2(locs):
    sumOfInc = lambda n: int((1 + n) * (n / 2))

    ls = locs.copy()
    opt = sum([sumOfInc(l) for l in locs])
    p = 0

    for _ in range(min(ls), max(ls)):
        p += 1
        new = sum([sumOfInc(abs(l - p)) for l in locs])
        if new < opt:
            opt = new
    return opt

def p1():
    locs = [int(l) for l in inp[0].split(",")]
    print(optMove(locs))
    return locs

def p2(o1):
    locs = o1
    print(optMove2(locs))
    return

o1 = p1()
p2(o1)