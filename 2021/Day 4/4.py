with open("Day 4/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

import time

def getBoard(txt):
    return [[int(f) for f in row.split(" ") if f != ""] for row in txt]

def hasWon(board):
    fullRow = lambda r: all(f == -1 for f in r)
    fullCol = lambda x, b: all(b[y][x] == -1 for y in range(5))
    return any(fullRow(r) for r in board) or any(fullCol(x, board) for x in range(5))

def concat(board):
    out = []
    for r in board:
        out += r
    return out

def getPos(i, size):
    return i % size, i // size

def sumBoard(board):
    return sum([sum([f for f in row if f != -1]) for row in board])

def showBoard(board):
    for row in board:
        print(row)

def p1():
    numbers = [int(n) for n in inp[0].split(",")]
    boards = [getBoard(inp[i + 1: i + 6]) for i in range(1, len(inp) - 1, 6)]
    linear_boards = [concat(b) for b in boards]

    for n in numbers:
        for i, b in enumerate(linear_boards):
            if n in b:
                l = b.index(n)
                x, y = getPos(l, 5)
                boards[i][y][x] = -1

                if hasWon(boards[i]):
                    print(sumBoard(boards[i]) * n)
                    return numbers
            continue
    return numbers

def p2(o1):
    numbers = o1
    boards = [getBoard(inp[i + 1: i + 6]) for i in range(1, len(inp) - 1, 6)]
    linear_boards = [concat(b) for b in boards]
    
    winners = []
    for n in numbers:
        for i, b in enumerate(linear_boards):
            if n in b and i not in winners:
                l = b.index(n)
                x, y = getPos(l, 5)
                boards[i][y][x] = -1

                if hasWon(boards[i]):
                    winners.append(i)
                    if len(winners) == len(boards):
                        print(sumBoard(boards[i]) * n)
            continue
    return

o1 = p1()
p2(o1)
