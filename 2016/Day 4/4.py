with open("Day 4/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def charCount(s):
    d = {}
    for c in s:
        if c == "-":
            continue

        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

def sortDict(d, reverse = False):
    return dict(sorted(d.items(), key = lambda x: x[1], reverse = reverse))

def isRealRoom(enc, given):
    dic = sortDict(charCount(enc), reverse = True)
    m = max(dic.values())
    chk = ""
    for s in range(m, 0, -1):
        new = ""
        for k,v in dic.items():
            if v == s:
                new += k
        
        chk += "".join(sorted(new))

        if len(chk) >= 5:
            return chk[:5] == given

def p1():
    rooms = inp.copy()
    score = 0
    real_rooms = []
    for room in rooms:
        enc, id_sum = room.rsplit("-", 1)
        id, sum = id_sum[:-1].split("[")
        
        if isRealRoom(enc, sum):
            real_rooms += [room]
            score += int(id)
    print(score)
    return real_rooms

def shiftWord(txt, v):
    v %= 26
    word = ""
    for c in txt:
        if c == "-":
            word += " "
        else:
            word += chr(ord("a") + ((ord(c) + v - ord("a")) % 26))
    return word


def p2(o1):
    rooms = o1
    for room in rooms:
        enc, id_sum = room.rsplit("-", 1)
        id, _ = id_sum[:-1].split("[")
        word = shiftWord(enc, int(id))
        if "northpole" in word:
            print(id)
    return

o1 = p1()
p2(o1)