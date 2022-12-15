# Imports
from sys import argv
from os.path import dirname
from z3 import *


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def computeOverlap(rlow, rhigh, ranges):
    head = []
    tail = []
    overlapped = False
    low = math.inf
    high = -math.inf
    for (rl, rh) in ranges:
        if rh < rlow:
            head.append((rl,rh))
        elif rl > rhigh:
            tail.append((rl,rh))
        else:
            overlapped = True
            low = min(rl, rlow, low)
            high = max(rh, rhigh, high)
    return head + ([(low, high)] if overlapped else [(rlow, rhigh)]) + tail

# Part 1
def p1(inp):
    splitcoords = lambda coords: tuple(map(int, coords.replace("x=","").replace("y=","").split(",")))
    splitline = lambda line: tuple(map(splitcoords, line.replace("Sensor at ","").split(": closest beacon is at ")))
    
    sensors = {}

    ranges = []
    beacons = set()
    row = 2_000_000
    for (x,y),(cx,cy) in map(splitline, inp):
        beacon = (cx,cy)
        if cy == row:
            beacons.add(beacon)

        total_dist = abs(x-cx) + abs(y-cy)
        row_dist = total_dist - abs(y-row)
        if row_dist > 0:
            ranges = computeOverlap(x-row_dist, x+row_dist+1, ranges)
        
        sensors[(x,y)] = total_dist # Used in Pt2
    
    beacon_count = sum(1 for (bx,by) in beacons if by == row and any(bx in range(rs,re+1) for (rs,re) in ranges))
    print(sum([rh - rl for (rl, rh) in ranges]) - beacon_count)
    return sensors

# Part 2
def p2(inp, sensors):
    search_space = 4_000_000

    solver = Solver()
    X = Int("X_coord")
    Y = Int("Y_coord")
    solver.add(0 <= X, X <= search_space)
    solver.add(0 <= Y, Y <= search_space)


    for (sx,sy), d in sensors.items():
        abso = lambda v: If(v >= 0, v, -v)
        solver.add(abso(sx - X) + abso(sy - Y) > d)

    solver.check()
    model = solver.model()
    print(model[X].as_long() * 4_000_000 + model[Y].as_long())


# Run main functions
o1 = p1(inp)
p2(inp, o1)