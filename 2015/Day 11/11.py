with open("Day 11/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def isValid(pw):
    inc_straight = False
    illegal = False
    pairs = set()
    prev = ""

    for i, char in enumerate(pw):
        curr = ord(char)
        if i + 2 < len(pw):
            if ord(pw[i+1]) == curr + 1 and ord(pw[i+2]) == curr + 2:
                inc_straight = True
        
        if char in "iol":
            illegal = True
        
        if char == prev:
            pairs.add(char)

        prev = char

    return inc_straight and not illegal and len(pairs) >= 2

def inc(chars, i):
    if i < -len(chars):
        print("looped")
    elif chars[i] == ord("z"):
        chars[i] = ord("a")
        inc(chars, i-1)
    else:
        chars[i] = chars[i] + 1

def nextPass(pw):
    chars = [ord(l) for l in pw]
    inc(chars, -1)
    return "".join(chr(c) for c in chars)

def p1():
    pw = nextPass(inp[0])
    while not isValid(pw):
        pw = nextPass(pw)
    print(pw)
    return pw

def p2(o1):
    pw = nextPass(o1)
    while not isValid(pw):
        pw = nextPass(pw)
    print(pw)
    return

o1 = p1()
p2(o1)