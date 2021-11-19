with open("Day 1/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    count = 0
    for char in inp[0]:
        if char == "(":
            count += 1
        else:
            count -= 1
    print(count)
    return

def p2():
    count = 0
    pos = 0
    for char in inp[0]:
        if char == "(":
            count += 1
        else:
            count -= 1
        pos += 1
        if count == -1:
            print(pos)
            break
    return

p1()
p2()