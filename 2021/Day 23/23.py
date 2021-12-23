with open("Day 23/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

from copy import deepcopy

pod_cost = {"A":1, "B":10, "C":100, "D":1000}
hall2room_travel = {
    (0,0):0, (1,0):0, (2,0):2, (3,0):4, (4,0):6,
    (0,1):2, (1,1):0, (2,1):0, (3,1):2, (4,1):4,
    (0,2):4, (1,2):2, (2,2):0, (3,2):0, (4,2):2,
    (0,3):6, (1,3):4, (2,3):2, (3,3):0, (4,3):0
    }

class Hallway():
    def __init__(self, inp, empty=False):
        if empty: return
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

    def set(self, rs, cost, hall, rooms):
        self.hall = hall
        self.h0, self.h12, self.h23, self.h34, self.h5 = self.hall
        self.rooms = rooms
        self.r1, self.r2, self.r3, self.r4 = self.rooms
        self.rs = rs
        self.cost = cost

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
            print("BONK")
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

        if st=="H":
            hall_travel = hall2room_travel[(si,ti)]
        else:
            hall_travel = hall2room_travel[(ti,si)]

        self.hall = [self.h0, self.h12, self.h23, self.h34, self.h5]
        self.rooms = [self.r1, self.r2, self.r3, self.r4]
        self.cost += ((1+sp) + (1+tp) + hall_travel) * pod_cost[pod]


    def moveIsValid(self, source, target):
        if source[0] == target[0]: return False

        st, si, sp = list(source)
        si, sp = int(si), int(sp)
        if st == "H":   #Empty source
            pod = self.hall[si][sp]
            if si == 0 and sp == 0 and self.hall[0][1] != ".": return False #Hall end exitable
            if si == 4 and sp == 1 and self.hall[4][0] != ".": return False #Hall end exitable
        else:
            pod = self.rooms[si][sp]
            if all((r == chr(ord("A") + si) or r == ".") for r in self.rooms[si]): return False #Pod should leave
            if any(r != "." for r in self.rooms[si][:sp]): return False #Room is exitable
        if pod == ".": return False

        tt, ti, tp = list(target)
        ti, tp = int(ti), int(tp)
        if tt == "H":   #Non clear target
            if self.hall[ti][tp] != ".": return False
            if ti == 0 and tp == 0 and self.hall[0][1] != ".": return False #Hall end enterable
            if ti == 4 and tp == 1 and self.hall[4][0] != ".": return False #Hall end enterable
        else:
            if self.rooms[ti][tp] != ".": return False
            if any(r != "." for r in self.rooms[ti][:tp]): return False #Room is enterable
            if pod != chr(ord("A") + ti): return False #Pod belongs in room
            if not all((r == chr(ord("A") + ti) or r == ".") for r in self.rooms[ti]): return False #Room is clear
            if not all(r == chr(ord("A") + ti) for r in self.rooms[ti][tp+1:]): return False #Room is filled

        #Hall is traversable
        if st == "R": ri, hi = si, ti
        else: ri, hi = ti, si

        if 0 <= hi - ri <= 1: return True
        if hi < ri:
            halls = range(hi+1, ri+1)
        else:
            halls = range(hi-1, ri, -1)
        for h in halls:
            if self.hall[h] != ["."]:
                return False

        return True

    def isSolved(self):
        solved = True
        for i, room in enumerate(self.rooms):
            if not all(p == chr(ord("A") + i) for p in room):
                solved = False
        return solved

def getValidMoves(state):
    hallspots = ["H00", "H01", "H10", "H20", "H30", "H40", "H41"]
    roomspots = ["R" + str(i) + str(j) for i in range(4) for j in range(state.rs)]
    for sourcespots, targetspots in [(hallspots, roomspots), (roomspots, hallspots)]:
        for source in sourcespots:
            for target in targetspots:
                if state.moveIsValid(source, target):
                    yield source, target

def solve(hw):
    finished = []
    states = [deepcopy(hw)]
    while states:
        new_states = []
        for state in states:
            for source, target in getValidMoves(state):
                new = Hallway("",empty=True)
                new.set(state.rs, state.cost, deepcopy(state.hall), deepcopy(state.rooms))
                new.move(source, target)
                if new.isSolved():
                    finished.append(new)
                else:
                    new_states.append(new)
        states = pruneStates(new_states)
    return min([f.cost for f in finished])

def pruneStates(states):
    scores = {}
    for state in states:
        key = (tuple(tuple(r) for r in state.rooms), tuple(tuple(h) for h in state.hall))
        if key in scores:
            existing = scores[key]
            if existing.cost > state.cost:
                existing.cost = state.cost
        else:
            scores[key] = state
    return list(scores.values())

def p1():
    h = Hallway(inp)
    print(solve(h))
    # h.show()
    # h.move("R10", "H00")
    # h.move("R11", "H01")
    # h.move("R30", "H40")
    # h.move("R20", "H20")
    # h.move("H20", "R11")
    # h.move("R31", "H20")
    # h.move("H20", "R10")
    # h.move("R21", "H30")
    # h.move("H30", "R31")
    # h.move("H40", "R30")
    # h.move("R00", "H20")
    # h.move("H20", "R21")
    # h.move("R01", "H20")
    # h.move("H20", "R20")
    # h.move("H01", "R01")
    # h.move("H00", "R00")
    # h.show()
    # print(h.cost)
    return

def p2(o1):
    h = Hallway(inp)
    h.unfold()
    # h.show()
    print(solve(h))
    return

o1 = p1()
p2(o1)