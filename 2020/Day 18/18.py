file = open("inp.txt", "r").read()

inp = file.split("\n")


def solveExp1(exp):
	ob = 0
	out = 0
	operator = "+"
	for i, part in enumerate(exp):
		if part ==  " ":
			continue
		elif part == "(":
			if ob == 0:
				oi = i
			ob += 1
			continue
		elif part == ")":
			ob -= 1
			if ob == 0:
				val = solveExp1(exp[oi + 1:i])
			else:
				continue
		elif ob == 0:
			try:
				val = int(part)
			except:
				operator = part
				continue

		if ob == 0:
			if operator == "*":
				out *= val
			elif operator == "+":
				out += val

	return out

def solveExp2(exp):
	ob = 0
	exp_copy = ""
	for i, part in enumerate(exp):
		if part == "(":
			if ob == 0:
				oi = i
			ob += 1
			continue
		elif part == ")":
			ob -= 1
			if ob == 0:
				val = solveExp2(exp[oi + 1:i])
				exp_copy += str(val)
			continue

		if ob == 0:
			exp_copy += part

	while "+" in exp_copy:
		exp_copy2 = ""
		parts = exp_copy.split(" ")
		i = 0
		while i <= len(parts) - 1:
			part = parts[i]
			if i + 1 < len(parts):
				if parts[i + 1] == "+":
					exp_copy2 += str(int(parts[i]) + int(parts[i + 2])) + " "
					i += 3
					continue
			
			exp_copy2 += part + " "
			i += 1
		exp_copy = exp_copy2[:-1]

	parts = exp_copy.split("*")
	out = 1
	for part in parts:
		out *= int(part)
	return out

def part1():
	s = 0
	for exp in inp:
		s += solveExp1(exp)
	print(s)

def part2():
	s = 0
	for exp in inp:
		s += solveExp2(exp)
	print(s)

part1()
part2()