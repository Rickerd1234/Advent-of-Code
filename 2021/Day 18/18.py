from json import loads
from itertools import permutations
with open("Day 18/inp.txt", "r") as file:
    inp = [loads(line.strip("\n")) for line in file]


class Pair():
    def __init__(self, left, right, depth):
        self.left = left
        self.lp = lambda: type(self.left) == Pair
        self.right = right
        self.rp = lambda: type(self.right) == Pair
        self.depth = depth
        self.par = ""
        self.hasP = lambda: self.par != ""

    def simple(self):
        s = "["
        if self.lp():
            s += self.left.simple()
        else:
            s += str(self.left)
        s += ","
        if self.rp():
            s += self.right.simple()
        else:
            s += str(self.right)
        s += "]"
        return s

    def depthInc(self):
        if self.rp():
            self.right.depthInc()
        if self.lp():
            self.left.depthInc()
        self.depth += 1

    def getPairs(self):
        c = [self]
        if self.lp():
            c += self.left.getPairs()
        if self.rp():
            c += self.right.getPairs()
        return c

    def addR(self, r):
        if self.rp():
            self.right.addR(r)
        else:
            self.right += r
    
    def addL(self, l):
        if self.lp():
            self.left.addL(l)
        else:
            self.left += l

    def findFirstL(self):
        if not self.hasP(): return False
        elif self == self.par.right:
            return self.par
        elif self.par.hasP():
            return self.par.findFirstL()
        else:
            return False

    def findFirstR(self):
        if not self.hasP(): return False
        elif self == self.par.left:
            return self.par
        elif self.par.hasP():
            return self.par.findFirstR()
        else:
            return False

    def explode(self):
        hasExploded = False
        if self.lp():
            (l,r), hasExploded = self.left.explode()
            if hasExploded: return (l,r), hasExploded
            if (l,r) != (-1,-1):
                self.left = 0

                if self.rp():
                    self.right.addL(r)
                else:
                    self.right += r

                nl = self.findFirstL()
                if nl:
                    if nl.lp():
                        nl.left.addR(l)
                    else:
                        nl.left += l
                
                return (l,r), True

        if hasExploded: return (l,r), hasExploded
        if self.rp():
            (l,r), hasExploded = self.right.explode()
            if hasExploded: return (l,-r), hasExploded
            if (l,r) != (-1,-1):
                self.right = 0

                if self.lp():
                    self.left.addR(l)
                else:
                    self.left += l

                nr = self.findFirstR()
                if nr:
                    if nr.rp():
                        nr.right.addL(r)
                    else:
                        nr.right += r

                return (l,r), True

        if self.depth == 4:
            return (self.left, self.right), False

        return (-1,-1), False

    def getSplit(self, v):
        l = v//2
        return Pair(l, v-l, self.depth+1)

    def split(self):
        if self.lp():
            hasSplit = self.left.split()
            if hasSplit: return hasSplit
        elif self.left >= 10:
            self.left = self.getSplit(self.left)
            self.left.par = self
            return True

        if self.rp():
            hasSplit = self.right.split()
            if hasSplit: return hasSplit
        elif self.right >= 10:
            self.right = self.getSplit(self.right)
            self.right.par = self
            return True
        
        return False

    def reduce(self):
        while True:
            _, hasExploded = self.explode()
            if hasExploded: continue
            
            hasSplit = self.split()
            
            if not hasExploded and not hasSplit:
                break

    def getMagnitude(self, lm, rm):
        s = 0
        if self.lp():
            s += self.left.getMagnitude(lm,rm) * lm
        else:
            s += self.left * lm

        if self.rp():
            s += self.right.getMagnitude(lm,rm) * rm
        else:
            s += self.right * rm
        return s

def addPairs(p1, p2):
    p1.depthInc()
    p2.depthInc()
    n = Pair(p1, p2, 0)
    p1.par = n
    p2.par = n
    return n

def parse(nr, d):
    if type(nr[0]) == list:
        l = parse(nr[0], d+1)
    else:
        l = nr[0]
    
    if type(nr[1]) == list:
        r = parse(nr[1], d+1)
    else:
        r = nr[1]

    p = Pair(l, r, d)

    if p.lp():
        l.par = p
    if p.rp():
        r.par = p
    return p

def p1():
    nrs = [parse(r, 0) for r in inp]
    p = nrs[0]
    p.reduce()
    for nr in nrs[1:]:
        p = addPairs(p, nr)
        p.reduce()
    print(p.getMagnitude(3,2))
    return

def p2(o1):
    max = 0
    for p1, p2 in permutations(inp, 2):
        p = addPairs(parse(p1, 0), parse(p2, 0))
        p.reduce()
        c = p.getMagnitude(3,2)
        if c > max:
            max = c
    print(max)
    return

o1 = p1()
p2(o1)