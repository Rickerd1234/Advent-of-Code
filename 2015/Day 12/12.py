with open("Day 12/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

import json

def objSum(obj):
    s = 0
    t = type(obj)
    if t == list:
        if len(obj) == 0:
            pass
        else:
            s += sum([objSum(o) for o in obj])
    
    elif t == dict:
        s += objSum(list(obj.values()))

    elif t == int:
        s += obj
    
    return s

def p1():
    obj = json.loads(inp[0])
    print(objSum(obj))
    return

def objSum2(obj):
    s = 0
    t = type(obj)
    if t == list:
        if len(obj) == 0:
            pass
        else:
            s += sum([objSum2(o) for o in obj])
    
    elif t == dict:
        vals = list(obj.values())
        if all(v != "red" for v in vals):
            s += objSum2(vals)

    elif t == int:
        s += obj
    
    return s

def p2(o1):
    obj = json.loads(inp[0])
    print(objSum2(obj))
    return

o1 = p1()
p2(o1)