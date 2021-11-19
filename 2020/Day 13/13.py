from numpy import prod

file = open("inp.txt", "r")

test  = ''''''

val = file.read().split("\n")
s = int(val[0])
buses1 = [int(x) for x in val[1].split(",") if x != "x"]
buses2 = [int(x) if x != "x" else 0 for x in val[1].split(",")]



def part1():
	no_bus = True
	i = 0
	while no_bus:
		for bus in buses1:
			if (i + s) % bus == 0:
				print(bus * i)
				no_bus = False
		i += 1

def part2():
	M = 1
	for b in buses2:
		if b != 0:
			M *= b
	
	s = 0
	for b in buses2:
		if b != 0:
			s += buses2.index(b) *  (M // b) * pow(M // b, -1, b)

	print(-s % M)

part1()
part2()