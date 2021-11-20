with open("Day 18/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

neighbors = [(-1,-1), (-1,0), (-1, 1), (0,1), (1,1), (1,0), (1,-1), (0, -1)]

def iterate(grid):
    new = [[c for c in r] for r in grid]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            nc = 0
            for ox, oy in neighbors:
                if 0 <= ox + x < len(row) and 0 <= oy + y < len(grid):
                    if grid[oy + y][ox + x] == "#":
                        nc += 1
            if cell == "#" and not (2 <= nc <= 3):
                new[y][x] = "."
            elif cell == "." and nc == 3:
                new[y][x] = "#"
    return new

def pprint(grid):
    for row in grid:
        print("".join(row))

def p1():
    grid = inp.copy()
    for _ in range(100):
        grid = iterate(grid)
    print(sum([sum([1 for c in row if c == "#"]) for row in grid]))
    return

def iterate2(grid):
    new = [[c for c in r] for r in grid]
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if (x == 0 or x == len(row) -1) and (y == 0 or y == len(grid) -1):
                continue
            nc = 0
            for ox, oy in neighbors:
                if 0 <= ox + x < len(row) and 0 <= oy + y < len(grid):
                    if grid[oy + y][ox + x] == "#":
                        nc += 1
            if cell == "#" and not (2 <= nc <= 3):
                new[y][x] = "."
            elif cell == "." and nc == 3:
                new[y][x] = "#"
    return new

def p2(o1):
    grid = inp.copy()
    for _ in range(100):
        grid = iterate2(grid)
    print(sum([sum([1 for c in row if c == "#"]) for row in grid]))
    return

o1 = p1()
p2(o1)