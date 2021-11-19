with open("Day 6/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def execute(instruction, lights):
    instr, start, _, end = instruction.rsplit(" ", 3)
    sx, sy = map(int, start.split(","))
    ex, ey = map(int, end.split(","))

    if instr == "turn on":
        func = lambda x: 1
    elif instr == "turn off":
        func = lambda x: 0
    else:
        func = lambda x: 1 - x

    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            lights[y][x] = func(lights[y][x])

def p1():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in inp:
        execute(instruction, lights)
    print(sum(list(map(sum, lights))))
    return


def execute2(instruction, lights):
    instr, start, _, end = instruction.rsplit(" ", 3)
    sx, sy = map(int, start.split(","))
    ex, ey = map(int, end.split(","))

    if instr == "turn on":
        func = lambda x: x + 1
    elif instr == "turn off":
        func = lambda x: x - 1 if x - 1 >= 0 else 0
    else:
        func = lambda x: x + 2

    for x in range(sx, ex+1):
        for y in range(sy, ey+1):
            lights[y][x] = func(lights[y][x])

def p2():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in inp:
        execute2(instruction, lights)
    print(sum(list(map(sum, lights))))
    return

p1()
p2()