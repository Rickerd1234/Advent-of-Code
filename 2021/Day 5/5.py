with open("Day 5/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    lines = inp.copy()

    points = {}
    for line in lines:
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
 
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                p = (x1, y)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
            continue

        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                p = (x, y1)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
            continue

    print(sum([1 for p in points.values() if p > 1]))
    return

def p2(o1):
    lines = inp.copy()

    points = {}
    for line in lines:
        start, end = line.split(" -> ")
        x1, y1 = start.split(",")
        x2, y2 = end.split(",")
 
        x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    

        if x1 == x2:
            if y1 > y2:
                y1, y2 = y2, y1
            for y in range(y1, y2 + 1):
                p = (x1, y)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
            continue

        if y1 == y2:
            if x1 > x2:
                x1, x2 = x2, x1
            for x in range(x1, x2 + 1):
                p = (x, y1)
                if p in points:
                    points[p] += 1
                else:
                    points[p] = 1
            continue

        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for i, x in enumerate(range(x1, x2 + 1)):
            if y1 < y2:
                y = y1 + i
            else:
                y = y1 - i
            p = (x, y)
            if p in points:
                points[p] += 1
            else:
                points[p] = 1

    print(sum([1 for p in points.values() if p > 1]))
    return

o1 = p1()
p2(o1)