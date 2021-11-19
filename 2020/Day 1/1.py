file = open("inp.txt", "r")

val = [int(line.strip("\n")) for line in file]

def part1():
	for x in val:
		if 2020 - x in val:
			print(x * (2020-x))
			return

def part2():
	for x in val:
		for y in val:
			if 2020 - x - y in val:
				print(x * y * (2020-x-y))
				return

part1()
part2()