# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def visualize(parts, size):
    for y in range(*size):
        for x in range(*size):
            for part in parts:
                if (part.x, part.y) == (x,y):
                    print(part.label,end="")
                    break
            else:
                print(".",end="")
        print()
    print()

class Head():
    def __init__(self):
        self.x, self.y = 0, 0
        self.label = "H"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

class Rope():
    def __init__(self, label, pred):
        self.x, self.y = 0, 0
        self.label = label
        self.pred = pred

        self.visited = {(self.x, self.y)}

    def update(self):
        # Compute distance
        x_dist = abs(self.pred.x-self.x)
        y_dist = abs(self.pred.y-self.y)
        distance = ((x_dist)**2 + (y_dist)**2)**(1/2)

        # Move required
        if distance >= 2:
            if y_dist == 0:
                self.x = (self.x + self.pred.x)//2
            elif x_dist == 0:
                self.y = (self.y + self.pred.y)//2
            # Diagonal cases
            else:
                if self.pred.x > self.x:
                    self.x += 1
                else:
                    self.x -= 1

                if self.pred.y > self.y:
                    self.y += 1
                else:
                    self.y -= 1

            self.visited.add((self.x, self.y))

    def __repr__(self):
        return self.label

# Part 1
# Part 2
def p12(inp):
    head = Head()
    tails = []
    pred = head
    for i in range(9):
        new_rope = Rope(str(i+1), pred)
        tails.append(new_rope)
        pred = new_rope

    for move in inp:
        dir, dist = move.split(" ")
        dist = int(dist)

        for _ in range(dist):
            dx, dy = (0,0)
            if dir == "U":
                dy = 1
            elif dir == "D":
                dy = -1
            elif dir == "R":
                dx = 1
            elif dir == "L":
                dx = -1
            
            head.move(dx,dy)
            for tail in tails:
                tail.update()

    print(len(tails[0].visited))
    print(len(tails[-1].visited))


# Run main functions
p12(inp)