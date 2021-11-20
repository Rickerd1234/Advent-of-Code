with open("Day 10/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def nextSeq(sequence):
    new = ""
    prev = ""
    c = 0
    for char in sequence[-1]:
        if char == prev or prev == "":
            c += 1
        else:
            new += str(c) + prev
            c = 1
        
        prev = char

    if c > 0:
        new += str(c) + prev
    return sequence + [new]

def p1():
    seq = inp.copy()
    for _ in range(40):
        seq = nextSeq(seq)
    print(len(seq[-1]))
    return seq

def p2(o1):
    seq = o1.copy()
    for _ in range(10):
        seq = nextSeq(seq)
    print(len(seq[-1]))
    return

o1 = p1()
p2(o1)