with open("Day 9/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def findLows(g):
    lows = []
    for y, r in enumerate(g):
        for x, c in enumerate(r):
            is_low = True
            inRangeX = lambda x: 0 <= x < len(r)
            if inRangeX(x+1) and not g[y][x+1] > c:
                is_low = False
            if inRangeX(x-1) and not g[y][x-1] > c:
                is_low = False

            inRangeY = lambda y: 0 <= y < len(g)
            if inRangeY(y+1) and not g[y+1][x] > c:
                is_low = False
            if inRangeY(y-1) and not g[y-1][x] > c:
                is_low = False

            if is_low:
                lows.append((x,y,c))
    return lows

def p1():
    grid = [[int(c) for c in row] for row in inp]
    lows = findLows(grid)
    risk_levels = [l[2] + 1 for l in lows]
    print(sum(risk_levels))
    return grid, lows

def getBasin(grid, low):
    checked = []
    basin = [low]
    inRangeX = lambda x: 0 <= x < len(grid[0])
    inRangeY = lambda y: 0 <= y < len(grid)
    for x,y,z in basin:
        if (x,y,z) in checked:
            continue

        if inRangeX(x+1) and grid[y][x+1] > z and grid[y][x+1] != 9:
            basin.append((x+1,y,grid[y][x+1]))
        if inRangeX(x-1) and grid[y][x-1] > z and grid[y][x-1] != 9:
            basin.append((x-1,y,grid[y][x-1]))

        if inRangeY(y+1) and grid[y+1][x] > z and grid[y+1][x] != 9:
            basin.append((x,y+1,grid[y+1][x]))
        if inRangeY(y-1) and grid[y-1][x] > z and grid[y-1][x] != 9:
            basin.append((x,y-1,grid[y-1][x]))

    return list(set(basin))

def p2(o1):
    grid, lows = o1
    basins = [getBasin(grid, low) for low in lows]
    basins.sort(reverse=True, key=len)
    p = 1
    for b in basins[:3]:
        p *= len(b)
    print(p)
    return

o1 = p1()
p2(o1)