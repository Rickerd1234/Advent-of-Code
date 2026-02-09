with open("Day 10/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

class Bot():
    def __init__(self, bot):
        self.bot = bot
        self.lval = -1
        self.rval = -1
        self.map = ("", "")

    def setMap(self, low, high):
        self.map = (low, high)

    def getMap(self):
        return self.map

    def rec(self, value):
        val = int(value)
        if self.lval == -1:
            self.lval = val
        elif self.rval == -1:
            if self.lval > val:
                self.lval, self.rval = val, self.lval
            else:
                self.rval = val
        else:
            print("error, " + self.bot + " already has 2 values")
    
    def getVal(self):
        return self.lval, self.rval

    def isFull(self):
        return self.lval != -1 and self.rval != -1

def p1():
    bots = inp.copy()
    moves = []
    bs = []
    for bot in bots:
        if bot[:3] == "bot":
            i, lh = bot.split(" gives low to ")
            l, h = lh.split(" and high to ")
            b = Bot(i)
            b.setMap(l, h)
            bs.append(b)
        else:
            v, t = bot[6:].split(" goes to ")
            moves += [(t, v)]
    
    outputs = {}
    while moves != []:
        t,v = moves[0]
        for b in bs:
            if b.bot == t:
                b.rec(v)
                vs = b.getVal()
                if vs == (17, 61):
                    print(b.bot[4:])

                if b.isFull():
                    (lt, ht), (lv, hv) = b.getMap(), vs
                    moves += [(lt, lv), (ht, hv)]

                break

            if t[:6] == "output":
                t, v = int(t[6:]), int(v)
                outputs[t] = v

                break
        moves = moves[1:]
    return outputs

def p2(o1):
    os = o1
    print(os[0] * os[1] * os[2])
    return

o1 = p1()
p2(o1)