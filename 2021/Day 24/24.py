with open("Day 24/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def runProgram(mn):
    var_dict = {"w":0, "x":0, "y":0, "z":0}
    mni = 0
    insts = inp.copy()
    while insts:
        for inst in insts[:18]:
            op, *args = inst.split(" ")

            out = args[0]
            if op == "inp":
                var_dict[args[0]] = int(mn[mni])
                mni += 1
                continue

            args = [var_dict[a] if a in var_dict else int(a) for a in args]
            if op == "add":
                var_dict[out] = args[0] + args[1]
            elif op == "mul":
                var_dict[out] = args[0] * args[1]
            elif op == "div":
                var_dict[out] = args[0] // args[1]
            elif op == "mod":
                var_dict[out] = args[0] % args[1]
            elif op == "eql":
                var_dict[out] = 1 if args[0] == args[1] else 0
        insts = insts[18:]
    return list(var_dict.values())

def p1():
    #Really just debugging the input by hand, who doesn't like some ALU/Assembly
    mn = "94399898949959"
    if runProgram(mn)[-1] == 0:
        print(mn)
    else:
        print("Verification failed")
    return

def p2(o1):
    mn = "21176121611511"
    if runProgram(mn)[-1] == 0:
        print(mn)
    else:
        print("Verification failed")
    return

o1 = p1()
p2(o1)