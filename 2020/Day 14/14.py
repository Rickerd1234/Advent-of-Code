file = open("inp.txt", "r")

test  = '''mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1'''

val = file.read().split("\n")
val = [x.split(" = ") for x in val]

def maskedBinary(dec, mask):
	bi = format(dec, "036b")
	o = ""
	for i in range(len(bi)):
		if mask[i] != "X":
			o += mask[i]
		else:
			o += bi[i]
	return o

def part1():
	mask = "X" * 36
	mem = {}
	for l in val:
		op = l[0]
		arg = l[1]

		if op == "mask":
			mask = arg
		else:
			addr = int(op[4:-1])
			mem[addr] = maskedBinary(int(arg), mask)

	s = 0
	for m in mem.values():
		s += int(m, 2)
	
	print(s)

def fillString(i, mask):
	o = ""
	x_count = 0
	for char in i:
		if char == "X":
			o += mask[x_count]
			x_count += 1
		else:
			o += char
	return o

def maskedAddresses(addr, mask):
	bi = format(addr, "036b")
	o = ""
	x_count = 0
	for i in range(len(bi)):
		if mask[i] != "0":
			o += mask[i]
			if mask[i] == "X":
				x_count += 1
		else:
			o += bi[i]

	p = []
	for i in range(2 ** x_count):
		bi_mask = format(i, "0" + str(x_count) + "b")
		p.append(fillString(o, bi_mask))
	return p

def part2():
	mask = "X" * 36
	mem = {}
	for l in val:
		op = l[0]
		arg = l[1]

		if op == "mask":
			mask = arg
		else:
			addr = int(op[4:-1])
			for a in maskedAddresses(addr, mask):
				mem[int(a, 2)] = int(arg)

	print(sum(mem.values()))


part1()
#< 14071449958656816225774218590089124922
#= 11327140210986
part2()
#< 2584847341072700
#= 2308180581795