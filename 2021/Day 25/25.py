with open("Day 25/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def stepGrid(grid):
    moved = False
    w,h = len(grid[0]), len(grid)
    getNewPos = lambda p, s: p % s
    movers = []
    for y,row in enumerate(grid):
        for x,pos in enumerate(row):
            if pos == ">":
                np = getNewPos(x + 1, w)
                if grid[y][np] == ".":
                    movers.append((x,y, np, pos))
    
    if len(movers) > 0: moved = True

    for x,y,n,t in movers:
        if t == ">":
            grid[y][x], grid[y][n] = grid[y][n], grid[y][x]

    movers = []
    for y,row in enumerate(grid):
        for x,pos in enumerate(row):
            if pos == "v":
                np = getNewPos(y + 1, h)
                if grid[np][x] == ".":
                    movers.append((x,y, np, pos))

    if len(movers) > 0: moved = True

    for x,y,n,t in movers:
        if t == "v":
            grid[y][x], grid[n][x] = grid[n][x], grid[y][x]

    return moved

def showGrid(grid):
    for row in grid:
        print("".join(row))
    print()

def p1():
    grid = [[c for c in line] for line in inp]
    i = 1
    while True:
        moved = stepGrid(grid)
        if moved:
            i += 1
        else:
            break
    print(i)
    return

def p2(o1):
    return

o1 = p1()
p2(o1)