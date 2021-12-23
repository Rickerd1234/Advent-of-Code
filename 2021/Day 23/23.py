with open("Day 23/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

pod_cost = {"A":1, "B":10, "C":100, "D":1000}

class Hallway():
    def __init__(self, inp):
        self.h0 = [".","."]
        self.r1 = []
        self.h12 = ["."]
        self.r2 = []
        self.h23 = ["."]
        self.r3 = []
        self.h34 = ["."]
        self.r4 = []
        self.h5 = [".","."]
        self.hall = [self.h0, self.h12, self.h23, self.h34, self.h5]
        self.rooms = [self.r1, self.r2, self.r3, self.r4]
        for line in inp[2:4]:
            self.r1.append(line[3])
            self.r2.append(line[5])
            self.r3.append(line[7])
            self.r4.append(line[9])
        self.rs = 2
        self.cost = 0

    def show(self):
        print(" ".join(["".join(h) for h in self.hall]))
        for i in range(self.rs):
            print(" |" + self.r1[i] + "|" + self.r2[i] + "|" + self.r3[i] + "|" + self.r4[i] + "|")
        print()

    def unfold(self):
        self.r1 = [self.r1[0]] + list("DD") + [self.r1[-1]]
        self.r2 = [self.r2[0]] + list("CB") + [self.r2[-1]]
        self.r3 = [self.r3[0]] + list("BA") + [self.r3[-1]]
        self.r4 = [self.r4[0]] + list("AC") + [self.r4[-1]]
        self.rooms = [self.r1, self.r2, self.r3, self.r4]
        self.rs += 2

    def move(self, source, target):
        if not self.moveIsValid(source, target):
            print("WHAT THE FACK MAN")
        st, si, sp = list(source)
        si, sp = int(si), int(sp)
        if st == "H":
            pod = self.hall[si][sp]
            self.hall[si][sp] = "."
            if si == 0: sp = 1 - sp
        else:
            pod = self.rooms[si][sp]
            self.rooms[si][sp] = "."
        
        tt, ti, tp = list(target)
        ti, tp = int(ti), int(tp)

        if tt == "H":
            hall = self.hall[ti]
            hall[tp] = pod
            if ti == 0: tp = 1 - tp
        else:
            room = self.rooms[ti]
            room[tp] = pod

        if ti == 4: ti -= 1
        if si == 4: si -= 1
        self.cost += ((1+sp) + (1+tp) + abs(ti-si)*2) * pod_cost[pod]

    def isReachable(self, pos, istarget):
        print(pos, istarget)
        valid = True
        st, si, sp = list(pos)
        si, sp = int(si), int(sp)

        if st == "H":
            if si == 0 and sp == 0:
                if not self.hall[si][1] == ".":
                    valid = False
            elif si == 0 and sp == 1:
                pass
            elif not all(p == "." for p in self.hall[si][:sp]):
                valid = False

            if self.hall[si][sp] == ".":
                valid = istarget

        else:
            if istarget and not all(p == chr(ord("A") + si) or p == "." for p in self.rooms[si]):
                valid = False
            
            if not all(p == "." for p in self.rooms[si][:sp]):
                valid = False

            if self.rooms[si][sp] == ".":
                valid = istarget

        return valid

    def moveIsValid(self, source, target):
        return self.isReachable(source, False) and self.isReachable(target, True) and source[0] != target[0]

    def isSolved(self):
        solved = True
        for i, room in enumerate(self.rooms):
            if not all(p == chr(ord("A") + i) for p in room):
                solved = False
        return solved

    def backtrack(self):
        print("c")
        if self.isSolved():
            print(self.cost)

        hallspots = ["H00", "H01", "H10", "H20", "H30", "H40", "H41"]
        roomspots = ["R" + str(i) + str(j) for i in range(4) for j in range(4)]

        for source in hallspots + roomspots:
            for target in hallspots + roomspots:
                if self.moveIsValid(source, target):
                    print(source, target)
                    old_cost = self.cost
                    self.move(source, target)
                    self.backtrack()
                    self.move(target, source)
                    self.cost = old_cost

def p1():
    h = Hallway(inp)
    h.show()
    h.move("R10", "H00")
    h.move("R11", "H01")
    h.move("R30", "H40")
    h.move("R20", "R11")
    h.move("R31", "R10")
    h.move("R21", "R31")
    h.move("H40", "R30")
    h.move("R00", "R21")
    h.move("R01", "R20")
    h.move("H01", "R01")
    h.move("H00", "R00")
    h.show()
    print(h.cost)
    return

def p2(o1):
    h = Hallway(inp)
    h.unfold()
    h.backtrack()

    h.show()

    return

#< 56334
#< 57158

o1 = p1()
p2(o1)