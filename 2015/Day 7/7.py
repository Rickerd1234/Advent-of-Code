from typing import OrderedDict


with open("Day 7/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def operation(op, circ_dict):
    if "NOT" == op[:3]:
        return 65535 - int(circ_dict[op.split(" ")[1]])

    split = op.split(" ")
    if len(split) == 1:
        return circ_dict[op]

    a, op, b = split

    a = int(a) if a.isnumeric() else circ_dict[a]
    b = int(b) if b.isnumeric() else circ_dict[b]
    
    if op == "AND":
        out = a & b
    elif op == "OR":
        out = a | b
    elif op == "LSHIFT":
        out = a << b
    elif op == "RSHIFT":
        out = a >> b
    
    return out

def updict(circ_dict, part):
    vin, out = part.split(" -> ")
    
    if vin.isnumeric():
        circ_dict[out] = int(vin)
    else:
        circ_dict[out] = operation(vin, circ_dict)

def getVars(instr):
    vin, out = instr.split(" -> ")
    if vin.isnumeric():
        vars = []
    elif "NOT" == vin[:3]:
        vars = [vin[4:]]
    else:
        split = vin.split(" ")
        if len(split) == 1:
            vars = split
        else:
            a, _, b = split
            if a.isnumeric() and b.isnumeric():
                vars = []
            elif a.isnumeric():
                vars = [b]
            elif b.isnumeric():
                vars = [a]
            else:
                vars = [a, b]
    return vars, out

def p1():
    insts = inp.copy()

    known = []
    ordered_inst = []
    i = 0
    while insts != []:
        instr = insts[i]
        req, out = getVars(instr)
        if all(v in known for v in req):
            known.append(out)
            ordered_inst.append(instr)
            insts.remove(instr)
            i -= 1
        i += 1
        if i > len(insts) - 1:
            i = 0

    circuit_dict = {}
    for part in ordered_inst:
        updict(circuit_dict, part)
    print(circuit_dict["a"])
    return circuit_dict["a"]

def p2(out1):
    insts = inp.copy()
    for i, inst in enumerate(insts):
        if getVars(inst)[1] == "b":
            insts[i] = str(out1) + " -> b"

    known = []
    ordered_inst = []
    i = 0
    while insts != []:
        instr = insts[i]
        req, out = getVars(instr)
        if all(v in known for v in req):
            known.append(out)
            ordered_inst.append(instr)
            insts.remove(instr)
            i -= 1
        i += 1
        if i > len(insts) - 1:
            i = 0

    circuit_dict = {}
    for part in ordered_inst:
        updict(circuit_dict, part)
    print(circuit_dict["a"])
    return

out1 = p1()
p2(out1)