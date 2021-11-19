file = open("inp.txt", "r")

test  = '''35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576'''

val = file.read().split("\n")
val = [int(v) for v in val]

def checkValue(val):
	for v in val:
		if val[-1] - v in val[:-1]:
			return True
	return False

def part1():
	for i in range(25, len(val)):
		if not checkValue(val[i-25:i+1]):
			print(val[i])
			return val[i]

def crack(val, s):
	for i in range(len(val)):
		for j in range(len(val)):
			if sum(val[i:j]) == s:
				return val[i:j]

def part2():
	arr = crack(val, p1)
	arr.sort()
	print(arr[0] + arr[-1])

p1 = part1()
part2()