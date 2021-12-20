with open("Day 19/inp.txt", "r") as file:
    inp = [line for line in file.read().split("\n\n")]
from itertools import combinations
from typing import Counter
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt

rots = [ #https://www.euclideanspace.com/maths/algebra/matrix/transforms/examples/index.htm
    [[1,0,0],[0,1,0],[0,0,1]],
    [[1,0,0],[0,0,-1],[0,1,0]],
    [[1,0,0],[0,-1,0],[0,0,-1]],
    [[1,0,0],[0,0,1],[0,-1,0]],

    [[0,-1,0],[1,0,0],[0,0,1]],
    [[0,0,1],[1,0,0],[0,1,0]],
    [[0,1,0],[1,0,0],[0,0,-1]],
    [[0,0,-1],[1,0,0],[0,-1,0]],

    [[-1,0,0],[0,-1,0],[0,0,1]],
    [[-1,0,0],[0,0,-1],[0,-1,0]],
    [[-1,0,0],[0,1,0],[0,0,-1]],
    [[-1,0,0],[0,0,1],[0,1,0]],

    [[0,1,0],[-1,0,0],[0,0,1]],
    [[0,0,1],[-1,0,0],[0,-1,0]],
    [[0,-1,0],[-1,0,0],[0,0,-1]],
    [[0,0,-1],[-1,0,0],[0,1,0]],

    [[0,0,-1],[0,1,0],[1,0,0]],
    [[0,1,0],[0,0,1],[1,0,0]],
    [[0,0,1],[0,-1,0],[1,0,0]],
    [[0,-1,0],[0,0,-1],[1,0,0]],

    [[0,0,-1],[0,-1,0],[-1,0,0]],
    [[0,-1,0],[0,0,1],[-1,0,0]],
    [[0,0,1],[0,1,0],[-1,0,0]],
    [[0,1,0],[0,0,-1],[-1,0,0]]
    ]
rotations = [np.matrix(r) for r in rots]

def getRotations(beacons):
    return [[(x,y,z) for (x,y,z) in np.dot(beacons, rotations[i]).getA()] for i in range(24)]

def plotBeacons(scns):
    ax = plt.axes(projection='3d')
    for i, bcns in enumerate(scns):
        ax.scatter3D([d[0] for d in bcns], [d[1] for d in bcns], [d[2] for d in bcns], alpha=0.3)
    plt.show()
    plt.close()

def getDiffCount(scns1, scns2):
    xdiff_count = Counter([scns1[i][0] - scns2[j][0] for i in range(len(scns1)) for j in range(len(scns2))])
    ydiff_count = Counter([scns1[i][1] - scns2[j][1] for i in range(len(scns1)) for j in range(len(scns2))])
    zdiff_count = Counter([scns1[i][2] - scns2[j][2] for i in range(len(scns1)) for j in range(len(scns2))])
    return xdiff_count.most_common()[0], ydiff_count.most_common()[0], zdiff_count.most_common()[0]

def getOverlap(total, new):
    st = set(total)
    sn = set(new)
    return list(st.intersection(sn)), list(sn - st)

def addOffset(bcns, off):
    ox,oy,oz = off
    return [(x+ox,y+oy,z+oz) for (x,y,z) in bcns]

def p1():
    scanners = [scnrs.split("\n")[1:] for scnrs in inp]
    sq = [[tuple(map(int, bcn.split(","))) for bcn in scnr] for scnr in scanners]

    comp_map = sq[0]
    sep_comp_map = [sq[0]]
    sq = sq[1:]

    offs = [(0,0,0)]

    while sq:
        rotated = getRotations(sq[0])

        fits = []
        for i in range(24):
            for m, match in enumerate(sep_comp_map):
                ox_m, oy_m, oz_m = getDiffCount(match, rotated[i])
                if ox_m[1] >= 12 and oy_m[1] >= 12 and oz_m[1] >= 12:
                    fits.append((i, m, (ox_m[0],oy_m[0],oz_m[0])))

        best = (0, [], [], ())
        if fits:
            for i, m, off in fits:
                corr_rot = rotated[i]
                offseted = addOffset(corr_rot, off)

                match = sep_comp_map[m]
                overlap, new = getOverlap(match, offseted)
                if len(overlap) >= best[0]:
                    best = (len(overlap), new, offseted, off)

        if best[0] >= 12:
            comp_map += best[1]
            sep_comp_map.append(best[2])
            offs.append(best[3])
            sq = sq[1:]
        else:
            if len(sq) == 1:
                break
            sq = sq[1:] + [sq[0]]

    plotBeacons(sep_comp_map + [offs],)
    print(len(comp_map))
    return offs

def p2(o1):
    m = 0
    for (x1,y1,z1), (x2,y2,z2) in combinations(o1, 2):
        mh = abs(x1-x2) + abs(y1-y2) + abs(z1-z2)
        if mh > m:
            m = mh
    print(m)
    return

o1 = p1()
p2(o1)