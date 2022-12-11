# Imports
import copy
import math
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = file.read().split("\n\n")


# Part 1
def p1(inp):
    monkeys = []
    for monkey in inp:
        id_str, start_str, func_str, test_str, true_str, false_str = monkey.split("\n")
        id = int(id_str[:-1].split(" ")[1])
        start = list(map(int, start_str.split(": ")[1].split(", ")))
        op = eval("lambda old: " + func_str.split(" = ")[1])
        test = int(test_str.split(" by ")[1])
        true = int(true_str.split(" ")[-1])
        false = int(false_str.split(" ")[-1])
        monkeys.append({
                "id": id,
                "items": start,
                "op": op,
                "test": test,
                "true": true,
                "false": false,
                "inspections": 0
            })

    monkeys_copy = copy.deepcopy(monkeys)
    
    for _ in range(20):
        for m_data in sorted(monkeys, key=lambda m: m["id"]):
            while m_data["items"]:
                old, *m_data["items"] = m_data["items"]
                new = m_data["op"](old) // 3
                tested = new % m_data["test"]
                getNewMonkeyItems = lambda tgt: [monkey["items"] for monkey in monkeys if monkey["id"]==tgt][0]
                if tested == 0:
                    getNewMonkeyItems(m_data["true"]).append(new)
                else:
                    getNewMonkeyItems(m_data["false"]).append(new)
                m_data["inspections"] += 1
    
    print(math.prod(sorted([monkey["inspections"] for monkey in monkeys], reverse=True)[:2]))
    return monkeys_copy

# Part 2
def p2(_, monkeys):
    combined_mod = math.prod([monkey["test"] for monkey in monkeys])
    for _ in range(10_000):
        for m_data in sorted(monkeys, key=lambda m: m["id"]):
            while m_data["items"]:
                old, *m_data["items"] = m_data["items"]
                new = m_data["op"](old) % combined_mod
                tested = new % m_data["test"]
                getNewMonkeyItems = lambda tgt: [monkey["items"] for monkey in monkeys if monkey["id"]==tgt][0]
                if tested == 0:
                    getNewMonkeyItems(m_data["true"]).append(new)
                else:
                    getNewMonkeyItems(m_data["false"]).append(new)
                m_data["inspections"] += 1
    
    print(math.prod(sorted([monkey["inspections"] for monkey in monkeys], reverse=True)[:2]))


# Run main functions
o1 = p1(inp)
p2(inp, o1)