import copy as cp

with open("Day 8/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def shiftScreen(screen, row, a, b):
    new = cp.deepcopy(screen)
    cs = len(screen)
    rs = len(screen[0])
    if row:
        for i, c in enumerate(screen[a]):
            new[a][(i + b) % rs] = c

    else:
        for i, r in enumerate(screen):
            new[(i + b) % cs][a] = r[a]
    return new

def p1():
    insts = inp.copy()
    screen = [["." for _ in range(50)] for _ in range(6)]
    for inst in insts:
        if inst[:4] == "rect":
            _, AxB = inst.rsplit(" ", 1)
            a, b = AxB.split("x")
            for x in range(int(a)):
                for y in range(int(b)):
                    screen[y][x] = "#"

        elif inst[:6] == "rotate":
            _, AbyB = inst.rsplit("=")
            a, b = AbyB.split(" by ")
            if "x=" in inst:
                screen = shiftScreen(screen, False, int(a), int(b))
            else:
                screen = shiftScreen(screen, True, int(a), int(b))

    print(sum([sum([1 for c in r if c == "#"]) for r in screen]))
    return screen

def show(screen):
    for row in screen:
        print("".join(row))

def p2(o1):
    screen = o1
    show(screen)
    return

o1 = p1()
p2(o1)