with open("Day 9/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def p1():
    comp = inp[0]
    open = False
    i = 0
    dec = 0
    while i < len(comp):
        if comp[i] == "(":
            found = ""
            open = True
            i += 1
            continue
        elif comp[i] == ")":
            open = False
            a, b = found.split("x")
            dec += int(a) * int(b)
            i += 1 + int(a)
            continue

        if open:
            found += comp[i]
            i += 1
            continue

        dec += 1
        i += 1
    print(dec)
    return comp

def recDec(txt):
    t = 0
    while txt != "":
        try:
            indo = txt.index("(")
            indc = txt.index(")")
        except:
            t += len(txt)
            break
        AxB = txt[indo +1 : indc]
        a, b = AxB.split("x")
        t += indo
        t += int(b) * recDec(txt[indc+1 : indc + int(a) +1])
        txt = txt[indc + int(a) +1 :]
    return t
    

def p2(o1):
    comp = o1
    print(recDec(comp))
    return

o1 = p1()
p2(o1)