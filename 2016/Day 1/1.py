with open("Day 1/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

directions = [(0,1), (1,0), (0,-1), (-1, 0)]

def p1():
    moves = inp[0].split(", ")
    dir = 0
    loc = (0, 0)
    for move in moves:
        turn = move[0]
        dist = int(move[1:])
        if turn == "R":
            dir = (dir + 1) % len(directions)
        else:
            dir = (dir - 1) % len(directions)

        loc = (loc[0] + directions[dir][0] * dist, loc[1] + directions[dir][1] * dist)
    print(abs(loc[0]) + abs(loc[1]))
    return

def p2(o1):
    moves = inp[0].split(", ")
    dir = 0
    loc = (0, 0)
    visited = [(0,0)]
    for move in moves:
        if len(set(visited)) != len(visited):
            break
        
        turn = move[0]
        dist = int(move[1:])
        if turn == "R":
            dir = (dir + 1) % len(directions)
        else:
            dir = (dir - 1) % len(directions)

        for _ in range(dist):
            loc = (loc[0] + directions[dir][0], loc[1] + directions[dir][1])

            if loc in visited:
                visited.append(loc)
                break
            visited.append(loc)
            
    print(abs(loc[0]) + abs(loc[1]))
    return

o1 = p1()
p2(o1)