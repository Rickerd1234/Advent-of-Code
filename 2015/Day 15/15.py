with open("Day 15/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def score(v, data):
    out = 1
    for i in range(4):
        score_ings = [v[j] * ing[1][i] for j, ing in enumerate(data)]
        temp = max(0, sum(score_ings))
        out *= temp
    return out

def p1():
    data = []
    for ing in inp:
        n, info = ing.split(": ")
        vals = info.split(", ")
        scores = [int(val.split(" ")[1]) for val in vals]
        data += [(n, scores)]

    v = [17, 19, 38, 26]

    print(score(v, data))

    return

def calories(v, data):
    cals = [c * data[i][1][4] for i, c in enumerate(v)]
    return sum(cals)


def p2(o1):
    data = []
    for ing in inp:
        n, info = ing.split(": ")
        vals = info.split(", ")
        scores = [int(val.split(" ")[1]) for val in vals]
        data += [(n, scores)]

    v = [46, 14, 30, 10]

    # print(calories(v, data))
    print(score(v, data))

    return

o1 = p1()
p2(o1)