with open("Day 10/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

scores = {")":3, "]":57, "}":1197, ">":25137}
scores2 = {")":1, "]":2, "}":3, ">":4}
match = {"(":")", "[":"]", "{":"}", "<":">"}

def p1():
    s = 0
    corrupted = []
    for line in inp:
        needs = []
        for c in line:
            if c in match:
                needs.append(match[c])
            elif needs[-1] != c:
                s += scores[c]
                corrupted.append(line)
                break
            else:
                needs = needs[:-1]

    print(s)
    return corrupted

def p2(o1):
    corrupted = o1.copy()
    lines = [line for line in inp.copy() if line not in corrupted]

    line_scores = []
    for line in lines:
        needs = []
        for c in line:
            if c in match:
                needs.append(match[c])
            else:
                needs = needs[:-1]
        
        needs.reverse()
        s = 0
        for c in needs:
            s *= 5
            s += scores2[c]
        line_scores.append(s)

    line_scores.sort()
    print(line_scores[len(line_scores)//2])
    return

o1 = p1()
p2(o1)