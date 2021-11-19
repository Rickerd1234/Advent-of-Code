with open("Day 2/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

dims = [tuple(map(lambda x: int(x), dim.split("x"))) for dim in inp]

def area(l,w,h):
    return min([l * w, w * h, l * h]) + 2 * (l * w + l * h + w * h)

def ribbon(l,w,h):
    return l * w * h + 2 * (l+w+h - max([l,w,h]))

def p1():
    print(sum([area(l,w,h) for l,w,h in dims]))
    return

def p2():
    print(sum([ribbon(l,w,h) for l,w,h in dims]))
    return

p1()
p2()