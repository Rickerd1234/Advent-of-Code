# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    field, raw_directions = file.read().split("\n\n")
    i = 0
    acc = ""
    directions = []
    while i < len(raw_directions):
        if raw_directions[i].isalpha():
            if acc.isnumeric():
                acc = int(acc)
            directions.append(acc)
            directions.append(raw_directions[i])
            acc = ""
        else:
            acc += raw_directions[i]
        i += 1
    if acc:
        if acc.isnumeric():
            acc = int(acc)
        directions.append(acc)
    inp = field.split("\n"), directions

offset_map = {
    0: (1,0),
    90: (0,1),
    180: (-1,0),
    270: (0,-1)
}


def wrapAround(x,y, facing, step, field):
    xo, yo = offset_map[facing]
    nx, ny = x+xo*step, y+yo*step
    
    if facing == 0:
        nx = min(field[ny].index("."), field[ny].index("#"))
        # print("A:", (nx, ny), x,y,facing,step)
    elif facing == 90:
        ny = min(i for i in range(len(field)) if (0 <= i < len(field) and 0 <= nx < len(field[i])) and not field[i][nx] == " ")
        # print("B:", (nx, ny), x,y,facing,step)
    elif facing == 180:
        nx = len(field[ny]) - 1
        # print("C:", (nx, ny), x,y,facing,step)
    else:
        ny = max(i for i in range(len(field)) if (0 <= i < len(field) and 0 <= nx < len(field[i])) and not field[i][nx] == " ")
        # print("D:", (nx, ny), x,y,facing,step)

    if field[ny][nx] == "#":
        return x,y
    else:
        return nx, ny


# Part 1
def p1(inp):
    field, directions = inp
    y = 0
    x = field[y].index(".")
    facing = 0

    for d in directions:
        if d == "R":
            facing = (facing + 90) % 360

        elif d == "L":
            facing = (facing - 90) % 360

        else:
            nx, ny = x, y
            for step in range(d):
                xo, yo = offset_map[facing]
                nx, ny = nx+xo, ny+yo
                if not (0 <= ny < len(field) and 0 <= nx < len(field[ny])) or field[ny][nx] == " ":
                    wx, wy = wrapAround(x,y, facing, step, field)
                    # Wrap around is blocked, so undo this last step
                    if (wx,wy) == (x,y):
                        nx -= xo
                        ny -= yo
                        break
                    nx, ny = wx, wy
                if field[ny][nx] == ".":
                    continue
                elif field[ny][nx] == "#":
                    nx -= xo
                    ny -= yo
                    break
            x,y = nx, ny
    print((y+1)*1000 + (x+1)*4 + facing//90)


def wrapAroundCube(x,y, facing, step, field):
    xo, yo = offset_map[facing]
    nx, ny = x+xo*step, y+yo*step
    
    if facing == 0:
        if ny in range(0, 50):
            nx = 99
            ny = (149 - ny)
            nf = 180
        elif ny in range(50, 100):
            nx = ny + 50
            ny = 49
            nf = 270
        elif ny in range(100, 150):
            nx = 149
            ny = (149 - ny)
            nf = 180
        elif ny in range(150, 200):
            nx = (ny - 100)
            ny = 149
            nf = 270
        else:
            print("WHUT!")
        # print("A:", (nx, ny), x,y,facing,step)
    elif facing == 90:
        if nx in range(0, 50):
            nx = (100 + nx)
            ny = 0
            nf = 90
        elif nx in range(50, 100):
            ny = (100 + nx)
            nx = 49
            nf = 180
        elif nx in range(100, 150):
            ny = (nx - 50)
            nx = 99
            nf = 180
        else:
            print("WHUT")
        # print("B:", (nx, ny), x,y,facing,step)
    elif facing == 180:
        if ny in range(0, 50):
            nx = 0
            ny = (149 - ny)
            nf = 0
        elif ny in range(50, 100):
            nx = ny - 50
            ny = 100
            nf = 90
        elif ny in range(100, 150):
            nx = 50
            ny = (149 - ny)
            nf = 0
        elif ny in range(150, 200):
            nx = ny - 100
            ny = 0
            nf = 90
        else:
            print("WHUT!")
        # print("C:", (nx, ny), x,y,facing,step)
    else:
        if nx in range(0, 50):
            ny = 50 + nx
            nx = 50
            nf = 0
        elif nx in range(50, 100):
            ny = 100 + nx
            nx = 0
            nf = 0
        elif nx in range(100, 150):
            nx = nx - 100
            ny = 199
            nf = 270
        else:
            print("WHUT")
        # print("D:", (nx, ny), x,y,facing,step)
    if field[ny][nx] == "#":
        return x,y, facing
    else:
        return nx, ny, nf


# Verify Cube Wraps
field = inp[0]
# Right
assert wrapAroundCube(149,0,0,1,field) == (99,149,180)
assert wrapAroundCube(149,49,0,1,field) == (99,100,180)
assert wrapAroundCube(99,51,0,1,field) == (101,49,270) # 99,50 gets blocked
assert wrapAroundCube(99,99,0,1,field) == (149,49,270)
assert wrapAroundCube(99,100,0,1,field) == (149,49,180)
assert wrapAroundCube(99,149,0,1,field) == (149,0,180)
assert wrapAroundCube(49,150,0,1,field) == (50,149,270)
assert wrapAroundCube(49,199,0,1,field) == (99,149,270)
# Down
assert wrapAroundCube(0,199,90,1,field) == (100,0,90)
assert wrapAroundCube(49,199,90,1,field) == (149,0,90)
assert wrapAroundCube(50,149,90,1,field) == (49,150,180)
assert wrapAroundCube(99,149,90,1,field) == (49,199,180)
assert wrapAroundCube(100,49,90,1,field) == (99,50,180)
assert wrapAroundCube(148,49,90,1,field) == (99,98,180) #149,49 gets blocked
# Left
assert wrapAroundCube(50,0,180,1,field) == (0,149,0)
assert wrapAroundCube(50,49,180,1,field) == (0,100,0)
assert wrapAroundCube(50,50,180,1,field) == (0,100,90)
assert wrapAroundCube(50,99,180,1,field) == (49,100,90)
assert wrapAroundCube(0,100,180,1,field) == (50,49,0)
assert wrapAroundCube(0,149,180,1,field) == (50,0,0)
assert wrapAroundCube(0,150,180,1,field) == (50,0,90)
assert wrapAroundCube(0,199,180,1,field) == (99,0,90)
# Up
assert wrapAroundCube(0,50,270,1,field) == (50,50,0)
assert wrapAroundCube(49,50,270,1,field) == (50,99,0)
assert wrapAroundCube(50,0,270,1,field) == (0,150,0)
assert wrapAroundCube(99,0,270,1,field) == (0,199,0)
assert wrapAroundCube(100,0,270,1,field) == (0,199,270)
assert wrapAroundCube(149,0,270,1,field) == (49,199,270)


# Part 2
def p2(inp, _):
    field, directions = inp
    y = 0
    x = field[y].index(".")
    facing = 0
    
    for d in directions:
        if d == "R":
            facing = (facing + 90) % 360

        elif d == "L":
            facing = (facing - 90) % 360

        else:
            nx, ny = x, y
            for step in range(d):
                xo, yo = offset_map[facing]
                nx, ny = nx+xo, ny+yo
                if not (0 <= ny < len(field) and 0 <= nx < len(field[ny])) or field[ny][nx] == " ":
                    wx, wy, facing = wrapAroundCube(x,y, facing, step, field)
                    # Wrap around is blocked, so undo this last step
                    if (wx,wy) == (x,y):
                        nx -= xo
                        ny -= yo
                        break
                    nx, ny = wx, wy
                if field[ny][nx] == ".":
                    continue
                elif field[ny][nx] == "#":
                    nx -= xo
                    ny -= yo
                    break
            x,y = nx, ny
    print((y+1)*1000 + (x+1)*4 + facing//90)


# Run main functions
o1 = p1(inp)
p2(inp, o1)