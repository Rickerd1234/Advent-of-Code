with open("Day 11/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]
    
def flash(gr, x, y):
    inRange = lambda x: 0 <= x < len(gr)
    disps = [(xo, yo) for xo in (-1,0,1) for yo in (-1,0,1)]

    for xo, yo in disps:
        newx, newy = x+xo, y+yo
        if inRange(newx) and inRange(newy):
            gr[newy][newx] += 1

def stepGrid(grid):
    new_grid = [[c + 1 for c in r] for r in grid]
    tens = sum([[(x,y) for x,c in enumerate(row) if c==10] for (y, row) in enumerate(new_grid)] ,[])
    
    for (x,y) in tens:
        flash(new_grid, x,y)
        current_tens = sum([[(x,y) for x,c in enumerate(row) if c==10] for (y, row) in enumerate(new_grid)] ,[])
        tens += [ten for ten in current_tens if ten not in tens]
    return [[0 if c >= 10 else c for c in r] for r in new_grid], len(tens)

def printGrid(gr):
    for row in gr:
        print("".join([str(c) for c in row]))
    print()

def p1():
    grid = [[int(c) for c in r] for r in inp.copy()]

    flash_count = 0
    for _ in range(100):
        grid, flashes = stepGrid(grid)
        flash_count += flashes
    print(flash_count)
    return

def p2(o1):
    grid = [[int(c) for c in r] for r in inp.copy()]
    flashes = 0
    i = 0
    while flashes != 100:
        grid, flashes = stepGrid(grid)
        i += 1
    print(i)
    return

o1 = p1()
p2(o1)