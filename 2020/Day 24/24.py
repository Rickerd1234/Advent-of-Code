file = open("inp.txt", "r").read()

inp = file.split("\n")

class Grid():
    def __init__(self, width, height):
        self.grid = [[Cell(x,y) for x in range(width)] for y in range(height)]
        self.cells = list(c for r in self.grid for c in r)

        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                odd = y%2
                even = not odd

                # Northwest
                if (even and x == 0) or y == 0:
                    nw = None
                else:
                    nw = self.grid[y-1][x-even]

                # West
                if x == 0:
                    w = None
                else:
                    w = self.grid[y][x-1]

                # Southwest
                if (even and x == 0) or y == height-1:
                    sw = None
                else:
                    sw = self.grid[y+1][x-even]

                # Northeast
                if (odd and x == width-1) or y == 0:
                    ne = None
                else:
                    ne = self.grid[y-1][x+odd]

                # East
                if x == width-1:
                    e = None
                else:
                    e = self.grid[y][x+1]

                # Southeast
                if (odd and x == width-1) or y == height-1:
                    se = None
                else:
                    se = self.grid[y+1][x+odd]
                
                cell.addNeighbors([nw, w, sw, ne, e, se])

    def get(self, x, y):
        return self.grid[y][x]

    def __repr__(self):
        out = ""
        for i, row in enumerate(self.grid):
            out += ("   " if i % 2 else "") + "   ".join(map(str, row)) + "\n"
        return out

class Cell():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.white = True
        self.nextWhite = None
        
    def addNeighbors(self, neighbors):
        self.nw, self.w, self.sw, self.ne, self.e, self.se = neighbors
        self.neighbors = [neighbor for neighbor in neighbors if neighbor != None]

    def getNeighbors(self):
        return self.neighbors

    def setNextState(self, state):
        self.nextWhite = state

    def goNextState(self):
        if self.nextWhite != None:
            self.white = self.nextWhite
            self.nextWhite = None

    def __repr__(self):
        return f"{self.x}:{self.y}"

g = Grid(151, 151)

for line in inp:
    cell = g.get(75,75)
    i = 0
    while i < len(line):
        single, double = line[i], line[i:i+2]
        if single == "e":
            cell = cell.e
            i += 1
        elif single == "w":
            cell = cell.w
            i += 1
        elif double == "nw":
            cell = cell.nw
            i += 2
        elif double == "sw":
            cell = cell.sw
            i += 2
        elif double == "ne":
            cell = cell.ne
            i += 2
        elif double == "se":
            cell = cell.se
            i += 2
    cell.white = not cell.white

# Part 1
print(sum(sum(1 for cell in row if not cell.white) for row in g.grid))

# Part 2
for _ in range(100):
    for cell in g.cells:
        count = sum(1 for cell in cell.getNeighbors() if not cell.white)
        if (count == 0 or count > 2) and not cell.white:
            cell.setNextState(True)
        elif count == 2 and cell.white:
            cell.setNextState(False)

    for cell in g.cells:
        cell.goNextState()

print(sum(sum(1 for cell in row if not cell.white) for row in g.grid))