with open("Day 8/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


def esclen(code):
    it = iter(code)
    c = -2
    for char in it:
        if char == "\\":
            char = next(it)
            if char == "\\" or char == "\"":
                pass
            elif char == "x":
                next(it)
                next(it)
        c += 1
    return c

def p1():
    print(sum([len(code) - esclen(code) for code in inp]))
    return

def esclen2(code):
    it = iter(code)
    c = 4
    for char in it:
        if char == "\\":
            char = next(it)
            c += 2
            if char == "\\" or char == "\"":
                c += 1
                pass
            elif char == "x":
                c += 2
                next(it)
                next(it)
        c += 1
    return c

def p2():
    print(sum([esclen2(code) - len(code) for code in inp]))
    return

p1()
p2()