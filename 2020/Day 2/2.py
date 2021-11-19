file = open("inp.txt", "r")

val = [line.strip("\n") for line in file]

def valid1(pw):
	r, l, pw = pw.split(" ", 3)
	r = r.split("-", 1)
	r[0] = int(r[0])
	r[1] = int(r[1])
	l = l[0]
	c = pw.count(l)
	return r[0] <= c and c <= r[1]

def part1():
	score = 0
	for x in val:
		if valid1(x):
			score += 1
	print(score)

def valid2(pw):
	r, l, pw = pw.split(" ", 3)
	r = r.split("-", 1)
	r[0] = int(r[0]) -1
	r[1] = int(r[1]) -1
	l = l[0]
	print(r, l, pw, (pw[r[0]] == l or pw[r[1]] == l), not (pw[r[0]] == l and pw[r[1]] == l))
	return (pw[r[0]] == l or pw[r[1]] == l) and not (pw[r[0]] == l and pw[r[1]] == l)


def part2():
	score = 0
	for x in val:
		if valid2(x):
			score += 1
	print(score)

part1()
part2()