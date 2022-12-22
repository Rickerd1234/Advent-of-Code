# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [int(line.strip("\n")) for line in file]

class Node():
    def __init__(self, val, pos):
        self.val = val
        self.turn = pos

    def setPred(self, pred):
        self.pred = pred

    def setSucc(self, succ):
        self.succ = succ

    def __repr__(self) -> str:
        return f"{self.pred.val} -> {self.val} -> {self.succ.val}"

# Part 1
def p1(inp):
    nodes = [Node(val, i) for i, val in enumerate(inp)]

    s = len(nodes)
    for i, node in enumerate(nodes):
        pred = nodes[(i-1) % s]
        succ = nodes[(i+1) % s]
        node.setPred(pred)
        node.setSucc(succ)
    
    zero_node = [node for node in nodes if node.val == 0][0]

    for i in range(s):
        node = [node for node in nodes if node.turn == i][0]
        if node.val%(s-1) == 0:
            continue

        old_pred = node.pred
        old_succ = node.succ

        v = node.val % (s-1)
        if v > 0:
            tgt = node
            for _ in range(v):
                tgt = tgt.succ
            new_pred = tgt
            new_succ = tgt.succ
        else:
            tgt = node.pred
            for _ in range(0, v, -1):
                tgt = tgt.pred
            new_pred = tgt
            new_succ = tgt.succ
        old_pred.setSucc(old_succ)
        old_succ.setPred(old_pred)

        new_pred.setSucc(node)
        node.setSucc(new_succ)
        new_succ.setPred(node)
        node.setPred(new_pred)

    node = zero_node
    i = 0
    sommie = 0
    while True:
        if (i%s) == (1000%s) or (i%s) == (2000%s) or (i%s) == (3000%s):
            sommie += node.val

        i += 1
        node = node.succ
        if node == zero_node:
            break

    print(sommie)

# Part 2
def p2(inp, _):
    nodes = [Node(val*811589153, i) for i, val in enumerate(inp)]

    s = len(nodes)
    for i, node in enumerate(nodes):
        pred = nodes[(i-1) % s]
        succ = nodes[(i+1) % s]
        node.setPred(pred)
        node.setSucc(succ)
    
    zero_node = [node for node in nodes if node.val == 0][0]

    for _ in range(10):
        for i in range(s):
            node = [node for node in nodes if node.turn == i][0]
            if node.val%(s-1) == 0:
                continue

            old_pred = node.pred
            old_succ = node.succ

            v = node.val % (s-1)
            if v > 0:
                tgt = node
                for _ in range(v):
                    tgt = tgt.succ
                new_pred = tgt
                new_succ = tgt.succ
            else:
                tgt = node.pred
                for _ in range(0, v, -1):
                    tgt = tgt.pred
                new_pred = tgt
                new_succ = tgt.succ
            old_pred.setSucc(old_succ)
            old_succ.setPred(old_pred)

            new_pred.setSucc(node)
            node.setSucc(new_succ)
            new_succ.setPred(node)
            node.setPred(new_pred)

    node = zero_node
    i = 0
    sommie = 0
    while True:
        if (i%s) == (1000%s) or (i%s) == (2000%s) or (i%s) == (3000%s):
            print(node)
            sommie += node.val

        i += 1
        node = node.succ
        if node == zero_node:
            break

    print(sommie)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)