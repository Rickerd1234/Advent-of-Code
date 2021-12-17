with open("Day 15/inp.txt", "r") as file:
    costs = [[int(c) for c in line.strip("\n")] for line in file]

# Just some optimization stuff
import heapq

INF = 100000000

def dijkstra(costs, source):
    s = len(costs)
    inRange = lambda x: 0 <= x < s
    offsets = [(-1,0), (1,0), (0,-1), (0,1)]

    costGrid = [[INF for _ in range(s)] for _ in range(s)]
    costGrid[source[1]][source[0]] = 0
    queue = [(0, source)]

    while queue:
        c, (x,y) = heapq.heappop(queue)
        for xo, yo in offsets:
            X, Y = x+xo, y+yo
            if inRange(X) and inRange(Y):
                newCost = c + costs[Y][X]
                if costGrid[Y][X] > newCost:
                    costGrid[Y][X] = newCost
                    heapq.heappush(queue, (newCost, (X, Y)))
    return costGrid

def p1():
    s = len(costs)
    costGrid = dijkstra(costs, (0,0))

    print(costGrid[s-1][s-1])
    return

def getNewVal(grid, x, y):
    s = len(grid)
    c = grid[y % s][x % s] + (x // s) + (y // s)
    while c > 9:
        c -= 9
    return c

def getCosts2(costs):
    s = len(costs) * 5
    return [[getNewVal(costs, x,y) for x in range(s)] for y in range(s)]

def p2(o1):
    costs2 = getCosts2(costs)
    s = len(costs2)
    costGrid = dijkstra(costs2, (0,0))

    print(costGrid[s-1][s-1])
    return

o1 = p1()
p2(o1)