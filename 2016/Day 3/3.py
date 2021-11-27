with open("Day 3/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    triangles = inp.copy()
    score = 0
    for triangle in triangles:
        a,b,c = [int(x) for x in triangle.split(" ") if x != ""]
        valid = lambda x,y,z: x + y > z and x + z > y and y + z > x
        if valid(a,b,c):
            score += 1
    print(score)
    return triangles

def p2(o1):
    triangles = o1
    aa, bb, cc = [], [], []
    for triangle in triangles:
        a,b,c = [int(x) for x in triangle.split(" ") if x != ""]
        aa.append(a)
        bb.append(b)
        cc.append(c)
    
    score = 0
    trs = aa + bb + cc
    for i in range(0, len(trs), 3):
        valid = lambda x,y,z: x + y > z and x + z > y and y + z > x
        a,b,c = trs[i:i+3]
        if valid(a,b,c):
            score += 1
    print(score)
    return

o1 = p1()
p2(o1)