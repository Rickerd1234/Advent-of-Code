with open("Day 2/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

keypad1 = [[1,2,3],  [4,5,6], [7,8,9]]

def p1():
    moves = inp.copy()
    x,y = 1,1
    code = ""
    for press in moves:
        for move in press:
            if move == "U":
                if y != 0:
                    y -= 1
            elif move == "R":
                if x != 2:
                    x += 1
            elif move == "D":
                if y != 2:
                    y += 1
            elif move == "L":
                if x != 0:
                    x -= 1

        code += str(keypad1[y][x])
    print(code)
    return moves

keypad2 = [ [ "",  "", "1",  "",  ""],
            [ "", "2", "3", "4",  ""],
            ["5", "6", "7", "8", "9"],
            [ "", "A", "B", "C",  ""],
            [ "",  "", "D",  "",  ""]]

def p2(o1):
    moves = o1
    x,y = 2,2
    code = ""
    for press in moves:
        for move in press:
            prev = (x,y)
            if move == "U":
                if y != 0:
                    y -= 1
            elif move == "R":
                if x != 4:
                    x += 1
            elif move == "D":
                if y != 4:
                    y += 1
            elif move == "L":
                if x != 0:
                    x -= 1
            
            val = keypad2[y][x]

            if val == "":
                x, y = prev
                continue
            
        code += val
    print(code)
    return

o1 = p1()
p2(o1)