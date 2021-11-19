import itertools
file = open("inp.txt", "r")

test  = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''

val = file.read().split("\n")
val = [int(v) for v in val]
val.sort()

def part1():
	diff1 = diff3 = 1
	for i, v in enumerate(val[1:]):
		diff = v - val[i]
		if diff == 3:
			diff3 += 1
		elif diff == 1:
			diff1 += 1
	print(diff1 * diff3)

def validSubCombis(sub):
	if len(sub) <= 2:
		return 1
	else:
		rs = 0
		for c in getCombis(sub[1:-1]):
			if valid(sub, c):
				rs += 1
		return rs

def valid(sub, c):
	if len(c) < 1:
		return sub[-1] - sub[0] <= 3
	if c[0] - sub[0] <= 3 and sub[-1] - c[-1] <= 3:
		for i in range(len(sub) - 1):
			if sub[i + 1] - sub[i]  > 3:
				return False
		return True
	return False

def getCombis(sub):
	combis = []
	for i in range(len(sub) + 1):
		combis += list(itertools.combinations(sub, i))
	return combis


def part2():
	m = max(val) + 3
	arr = [0] + val.copy() + [m]

	poss = 1
	i = 1
	diff = arr[i] - arr[i-1]
	sub = []
	while i < len(arr):
		if diff == 1:
			sub.append(arr[i-1])
		if diff == 3:
			poss *= validSubCombis(sub)
			sub = [arr[i-1]]
		diff = arr[i] - arr[i-1]
		i += 1
	if len(sub) > 1:
		poss *= validSubCombis(sub)
	print(poss)

part1()
part2()