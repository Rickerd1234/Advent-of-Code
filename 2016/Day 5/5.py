with open("Day 5/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

import hashlib

def correctHash(t):
    res = hashlib.md5(bytes(t, "utf-8")).hexdigest()
    return res[:5] == "00000", res

def p1():
    did = inp[0]
    i = 0
    p = ""
    while True:
        if len(p) == 8:
            break
        cor, h = correctHash(did + str(i))
        if cor:
            p += h[5]
        i += 1
    print(p)
    return

def p2(o1):
    did = inp[0]
    i = 0
    p = ["" for _ in range(8)]
    found = 0
    while True:
        if found == 8:
            break
        cor, h = correctHash(did + str(i))
        if cor:
            ind = int(h[5], 16)
            if ind < 8 and p[ind] == "":
                found += 1
                p[ind] += h[6]
        i += 1
    print("".join(p))
    return

o1 = p1()
p2(o1)