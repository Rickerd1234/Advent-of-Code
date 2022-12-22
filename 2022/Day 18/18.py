# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]


# Part 1
def p1(inp):
    toTup = lambda l: tuple(map(int, l.split(",")))
    cubes = set(map(toTup, inp))
    c = 0
    for (x,y,z) in cubes:
        for (xo,yo,zo) in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
            if not (x+xo, y+yo, z+zo) in cubes:
                c += 1
    print(c)
    return cubes

# Part 2
def p2(inp, cubes):
    lx, ly, lz = min(map(lambda c: c[0], cubes)), min(map(lambda c: c[1], cubes)), min(map(lambda c: c[2], cubes))
    ux, uy, uz = max(map(lambda c: c[0], cubes)), max(map(lambda c: c[1], cubes)), max(map(lambda c: c[2], cubes))
    known_pockets = []
    c = 0
    for (x,y,z) in cubes:
        for (xo,yo,zo) in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
            if (x+xo, y+yo, z+zo) not in cubes:
                current = (x+xo, y+yo, z+zo)
                # Check if the airpocket already is known to be inside
                if any(current in pk for pk in known_pockets): continue

                # Dijkstra to check if we can reach the limits of the cube (in which the droplet is contained)
                pocket = {current}
                queue = {current}
                outside = False
                while len(queue) > 0:
                    (cx, cy, cz) = queue.pop()
                    for (xo2,yo2,zo2) in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (1,0,0), (-1,0,0)]:
                        nb = (cx+xo2, cy+yo2, cz+zo2)

                        if not (lx <= cx+xo2 <= ux and ly <= cy+yo2 <= uy and lz <= cz+zo2 <= uz):
                            outside = True
                            queue = set()
                            break

                        if nb not in cubes and nb not in pocket:
                            pocket.add(nb)
                            queue.add(nb)

                if outside:
                    c += 1
                else:
                    known_pockets.append(pocket)
    print(c)


# Run main functions
o1 = p1(inp)
p2(inp, o1)