file = open("inp.txt", "r")

test  = '''nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6'''

val = file.read().split("\n")


def part1():
	i, acc = simulate(val)
	print(acc)


def simulate(ops):
	checked = []
	i = 0
	acc = 0
	while i not in checked and i < len(ops):
		op, arg = ops[i].split(" ")
		arg = int(arg)
		checked.append(i)

		if op == "nop":
			i += 1
		elif op == "jmp":
			i += arg
		elif op == "acc":
			acc += arg
			i += 1

	if i in checked:
		return -1, acc
	else:
		return i, acc

def part2():
	for j in range(len(val)):
		copy = val.copy()
		c_op, c_arg = copy[j].split(" ")
		if c_op == "jmp":
			copy[j] = "nop " + c_arg
		elif c_op == "nop":
			copy[j] = "jmp " + c_arg
		else:
			continue

		i, acc = simulate(copy)
		if i > -1:
			print(acc)
			break
		else:
			continue

part1()
part2()