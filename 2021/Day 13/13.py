with open("Day 13/inp.txt", "r") as file:
    dots, folds = file.read().split("\n\n")
    dots = [tuple([int(v) for v in line.split(",")]) for line in dots.split("\n")]
    folds = folds.split("\n")

from copy import deepcopy

def printPaper(paper):
    for line in paper:
        print("".join(["  " if s == "." else "■■" for s in line]))

def foldPaper(paper, val, horizontal):
    if horizontal:
        fold = [row[val+1:] for row in paper]
        paper = [row[:val] for row in paper]
    else:
        fold = paper.copy()[val:]
        paper = paper[:val]

    if not horizontal:
        fold = reversed(fold)
    for y, r in enumerate(fold):
        if horizontal:
            r = reversed(r)
        for x, s in enumerate(r):
            if s == "#":
                paper[y][x] = s
    return paper

def countDots(paper):
    return sum([sum([1 for s in r if s == "#"]) for r in paper])

def p1(dots, folds):
    maxy = max([t[0] for t in dots])
    maxx = max([t[1] for t in dots])
    paper = [["." for _ in range(maxy + 1)] for _ in range(maxx + 1)]
    for x,y in dots:
        paper[y][x] = "#"

    axis, value = folds[0].split("=")
    paper = foldPaper(paper, int(value), axis[-1] == "x")
    
    print(countDots(paper))
    return paper, folds[1:]

def p2(o1):
    paper, folds = o1
    for fold in folds:
        axis, value = fold.split("=")
        paper = foldPaper(paper, int(value), axis[-1] == "x")
    printPaper(paper)
    return

o1 = p1(dots, folds)
p2(o1)