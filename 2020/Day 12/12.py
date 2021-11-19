file = open("inp.txt", "r")

test  = '''F10
N3
F7
R90
F11'''

val = file.read().split("\n") #file.read()
#val = [int(v) for v in val]

directions = ["N", "E", "S", "W"]

def part1():
	direction = "E"
	n, e = 0, 0
	for line in val:
		op, arg = line[0], int(line[1:])
		if op == "F":
			op = direction
		elif op == "R":
			direction = directions[(directions.index(direction) + arg // 90) % 4]
		elif op == "L":
			direction = directions[(directions.index(direction) - arg // 90) % 4]

		if op in directions:
			if op == "N":
				n += arg
			elif op == "E":
				e += arg
			elif op == "S":
				n -= arg
			elif op == "W":
				e -= arg

	print(abs(n) + abs(e))

def part2():
	direction = "E"
	wn, we = 1, 10
	n, e = 0, 0
	for line in val:
		op, arg = line[0], int(line[1:])
		if op == "F":
			n += wn * arg
			e += we * arg
		elif op == "R":
			if arg == 90:
				wn, we = -we, wn
			elif arg == 270:
				wn, we = we, -wn
			elif arg == 180:
				wn = -wn
				we = -we
		elif op == "L":
			if arg == 90:
				wn, we = we, -wn
			elif arg == 270:
				wn, we = -we, wn
			elif arg == 180:
				wn = -wn
				we = -we

		if op in directions:
			if op == "N":
				wn += arg
			elif op == "E":
				we += arg
			elif op == "S":
				wn -= arg
			elif op == "W":
				we -= arg

	print(abs(n) + abs(e))

part1()
part2()