with open("Day 4/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

import hashlib

def isValid(key):
    hash = hashlib.md5(bytes(key,"utf-8")).hexdigest()
    return hash[:5] == "00000"

def isValid2(key):
    hash = hashlib.md5(bytes(key,"utf-8")).hexdigest()
    return hash[:6] == "000000"

def p1():
    num = 0
    while True:
        if isValid(inp[0] + str(num)):
            break
        num += 1
    print(num)
    return

def p2():
    num = 0
    while True:
        if isValid2(inp[0] + str(num)):
            break
        num += 1
    print(num)
    return

p1()
p2()