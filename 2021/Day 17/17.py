with open("Day 17/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def getHitTrajectories(xl, xh, yl, yh):
    inTarget = lambda x,y: xl <= x <= xh and yl <= y <= yh
    overTarget = lambda x,y: xh < x or yl > y
    dx, dy = xh-xl, yh-yl

    trajectories = []
    for gy in range(yl, abs(yh)+ dy + 1):
        for gx in range(xh + 1):
            x, y = 0, 0
            vx, vy = gx, gy
            path = [(x,y)]
            while not overTarget(x,y):
                x += vx
                y += vy
                path.append((x,y))
                vx -= 1 if vx > 0 else (-1 if vx < 0 else 0)
                vy -= 1

                if inTarget(x,y):
                    trajectories.append(((gx,gy),path))
                    break

    return trajectories


def p1():
    xs, ys = inp[0].split(": x=")[1].split(", y=")
    xlow, xhigh = map(int, xs.split(".."))
    ylow, yhigh = map(int, ys.split(".."))
    trajectories = getHitTrajectories(xlow, xhigh, ylow, yhigh)

    getY = lambda t: t[1]
    highPoint = lambda p: max(p[1], key=getY)
    highest_trajectory = max(trajectories, key=highPoint)
    
    print(getY(highPoint(highest_trajectory)))
    return trajectories

def p2(o1):
    print(len(o1))
    return

o1 = p1()
p2(o1)