with open("Day 17/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def splits(remainder, used, unused):
    if remainder == 0:
        return 1

    count = 0
    for i, c in enumerate(unused):
        if c > remainder:
            break
        temp = unused[:i].copy()
        count += splits(remainder - c, used + [c], temp)
    return count

def p1():
    unused = []
    for c in inp:
        unused.append(int(c))
    unused.sort()

    print(splits(150, [], unused))

    return unused

def splits2(remainder, used, unused):
    if remainder == 0:
        return [used]

    conts = []
    for i, c in enumerate(unused):
        if c > remainder:
            break
        temp = unused[:i].copy()
        conts += splits2(remainder - c, used + [c], temp)
    return conts

def p2(o1):
    setsizes = [len(sol) for sol in splits2(150, [], o1)]
    smallest = min(setsizes)
    print(len([1 for s in setsizes if s == smallest]))
    return

o1 = p1()
p2(o1)