with open("Day 2/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    moves = inp.copy()
    hor = 0
    dep = 0
    for move in moves:
        dir, n = move.split(" ")

        if dir == "forward":
            hor += int(n)
        elif dir == "up":
            dep -= int(n)
        elif dir == "down":
            dep += int(n)
    print(hor * dep)
    return moves

def p2(o1):
    moves = o1
    hor = 0
    dep = 0
    aim = 0
    for move in moves:
        dir, n = move.split(" ")

        if dir == "forward":
            hor += int(n)
            dep += int(n) * aim
        elif dir == "up":
            aim -= int(n)
        elif dir == "down":
            aim += int(n)
    print(hor * dep)
    return

o1 = p1()
p2(o1)