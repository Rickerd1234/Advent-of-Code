from typing import DefaultDict
with open("Day 22/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    lit = DefaultDict(bool)
    for inst in inp:
        op, xyz = inst.split(" ", 1)
        xs,ys,zs = xyz.split(",")
        (x0, x1),(y0,y1),(z0,z1) = [tuple(map(int,v[2:].split(".."))) for v in (xs,ys,zs)]

        if x0 > 50 or y0 > 50 or z0 > 50:
            continue
        if x1 < -50 or y1 < -50 or z1 < -50:
            continue

        val = (op == "on")
        for x in range(x0,x1+1):
            for y in range(y0,y1+1):
                for z in range(z0,z1+1):
                    lit[(x,y,z)] = val
    
    s = 0
    for x in range(-50,51):
            for y in range(-50,51):
                for z in range(-50,51):
                    s += int(lit[(x,y,z)])
    print(s)
    return

def rangeOverlap(r0, r1): return r0[0] <= r1[1] and r1[0] <= r0[1]

def regionOverlap(r0, r1): return all(rangeOverlap(d0, d1) for (d0, d1) in zip(r0,r1))

def regionSub(rmain, rsub):
    if not regionOverlap(rmain, rsub):
        yield rmain

    else:
        (x0l, x0h), (y0l, y0h), (z0l, z0h) = rmain
        (x1l, x1h), (y1l, y1h), (z1l, z1h) = rsub

        getCombs = lambda x0l, x0h, x1l, x1h: zip((x0l, max(x0l, x1l), x1h + 1), (x1l - 1, min(x0h, x1h), x0h))

        for xi, (x0, x1) in enumerate(getCombs(x0l, x0h, x1l, x1h)):
            if x0 > x1: continue
            for yi, (y0, y1) in enumerate(getCombs(y0l, y0h, y1l, y1h)):
                if y0 > y1: continue
                for zi, (z0, z1) in enumerate(getCombs(z0l, z0h, z1l, z1h)):
                    if z0 > z1: continue
                    if xi == 1 and yi == 1 and zi == 1: continue
                    yield (x0, x1), (y0, y1), (z0, z1)

def regionSize(r): return (r[0][1]-r[0][0] +1) * (r[1][1]-r[1][0] +1) * (r[2][1]-r[2][0] +1)

def p2(o1):
    ranges = []
    for inst in inp:
        op, xyz = inst.split(" ", 1)
        xs,ys,zs = xyz.split(",")
        region = tuple(tuple(map(int,v[2:].split(".."))) for v in (xs,ys,zs))
        ranges.append(((op == "on"), region))
    
    known = []
    new = []
    
    for on, r in ranges:
        new.clear()
        for r1 in known:
            new.extend(regionSub(r1, r))
        if on:
            new.append(r)
        known, new = new, known

    print(sum([regionSize(region) for region in known]))
    return

o1 = p1()
p2(o1)