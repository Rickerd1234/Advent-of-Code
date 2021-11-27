with open("Day 7/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def hasABP(s):
    for i in range(len(s) - 3):
        if s[i] == s[i + 3] and s[i+1] == s[i+2] and not s[i] == s[i+1]:
            return True
    return False

def getABAs(s):
    abas = []
    for i in range(len(s) - 2):
        if s[i] == s[i + 2] and not s[i] == s[i+1]:
            abas += [s[i:i+3]]
    return abas


def p1():
    ips = inp.copy()
    count = 0
    for ip in ips:
        parts = []
        hypers = []
        while "[" in ip or "]" in ip:
            try:
                o = ip.index("[")
            except:
                o = -1
            try:
                c = ip.index("]")
            except:
                c = -1
            if o > -1 and o < c:
                start, ip = ip.split("[", 1)
                parts += [start]
            else:
                hyper, ip = ip.split("]", 1)
                hypers += [hyper]
        parts += [ip]
            
        if any(hasABP(part) for part in parts) and not any(hasABP(hyper) for hyper in hypers):
            count += 1
    print(count)
    return

def ababab(abas, babs):
    if len(abas) == 0 or len(babs) == 0:
        return False

    for aba in abas:
        if aba[1] + aba[0] + aba[1] in babs:
            return True
    return False

def p2(o1):
    ips = inp.copy()
    count = 0
    for ip in ips:
        parts = []
        hypers = []
        while "[" in ip or "]" in ip:
            try:
                o = ip.index("[")
            except:
                o = -1
            try:
                c = ip.index("]")
            except:
                c = -1
            if o > -1 and o < c:
                start, ip = ip.split("[", 1)
                parts += [start]
            else:
                hyper, ip = ip.split("]", 1)
                hypers += [hyper]
        parts += [ip]

        abas = []
        for part in parts:
            abas += getABAs(part)

        babs = []
        for hyper in hypers:
            babs += getABAs(hyper)

        if ababab(abas, babs):
            count += 1
    print(count)
    return

o1 = p1()
p2(o1)