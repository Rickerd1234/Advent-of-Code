with open("Day 3/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def getCount(pcs):
    counter = [{} for _ in pcs[0]]
    for pc in pcs:
        for i, b in enumerate(pc):
            if b in counter[i]:
                counter[i][b] += 1
            else:
                counter[i][b] = 1
    return counter

def p1():
    pcs = inp.copy()
    counter = getCount(pcs)

    gamma = ""
    epsilon = ""
    for l in counter:
        if l["1"] > l["0"]:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"

    print(int(gamma, 2) * int(epsilon, 2))
    return pcs, counter

def p2(o1):
    pcs, counter = o1

    oxy = pcs.copy()
    oxy_count = counter.copy()
    for i, l in enumerate(oxy_count):
        if len(oxy) > 1:
            l = oxy_count[i]

            if len(l) < 2:
                maxk = list(l.keys())[0]
            elif l["0"] == l["1"]:
                maxk = "1"
            else:
                maxk = max(l, key=l.get)
            
            oxy = [pc for pc in oxy if pc[i] == maxk]
            oxy_count = getCount(oxy)

    co2 = pcs.copy()
    co2_count = counter.copy()
    for i, l in enumerate(co2_count):
        if len(co2) > 1:
            l = co2_count[i]

            if len(l) < 2:
                mink = list(l.keys())[0]
            elif l["0"] == l["1"]:
                mink = "0"
            else:
                mink = min(l, key=l.get)

            co2 = [pc for pc in co2 if pc[i] == mink]
            co2_count = getCount(co2)

    print(int(oxy[0], 2) * int(co2[0], 2))
    return

o1 = p1()
p2(o1)