with open("Day 3/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

moves = {
        "^": (0,1),
        ">": (1,0),
        "v": (0,-1),
        "<": (-1,0)
        }

def move(coords, movement):
    return coords[0] + movement[0], coords[1] + movement[1]

def p1():
    visited = {(0,0): 1}
    coords = (0,0)
    for dir in inp[0]:
        coords = move(coords, moves[dir])
        if coords in visited:
            visited[coords] += 1
        else:
            visited[coords] = 1
    print(len(visited))
    return

def p2():
    visited = {(0,0): 1}
    coords = (0,0)
    instruction = True
    for dir in inp[0]:
        instruction = not instruction
        if not instruction:
            continue
        coords = move(coords, moves[dir])
        if coords in visited:
            visited[coords] += 1
        else:
            visited[coords] = 1

    coords = (0,0)
    instruction = False
    for dir in inp[0]:
        instruction = not instruction
        if not instruction:
            continue
        coords = move(coords, moves[dir])
        if coords in visited:
            visited[coords] += 1
        else:
            visited[coords] = 1
    print(len(visited))
    return

p1()
p2()