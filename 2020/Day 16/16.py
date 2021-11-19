file = open("inp.txt", "r")

test  = '''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''

rules, my_ticket, nearby_tickets = file.read().split("\n\n")
rules = rules.split("\n")
my_ticket = my_ticket.split("\n")[1].split(",")
nearby_tickets = nearby_tickets.split("\n")[1:]

ranges = []
for rule in rules:
	first_range, second_range = rule.split(": ")[1].split(" or ")
	a, b = first_range.split("-")
	ranges.append((int(a),int(b)))
	c, d = second_range.split("-")
	ranges.append((int(c),int(d)))

def part1():
	p2_copy = nearby_tickets.copy()
	c = 0
	for ticket in nearby_tickets:
		# print()
		# print(ticket)
		for v in ticket.split(","):
			found = True
			v = int(v)

			# print(v)
			for r in ranges:
				if v >= r[0] and v <= r[1]:
					# print(r)
					found = False
					break

			if found:
				# print(v)
				p2_copy.remove(ticket)
				c += v

	print(c)
	return p2_copy

def getRanges(v):
	o = []
	for i in range(len(ranges) // 2):
		r1, r2 = ranges[2*i : 2*i + 2]
		if (v >= r1[0] and v <= r1[1]) or (v >= r2[0] and v <= r2[1]):
			o.append(i)
	return o

def part2(nearbies):
	f_dict = {}
	for ticket in nearbies:
		for i, field in enumerate(ticket.split(",")):
			valid_ranges = getRanges(int(field))
			if i not in f_dict:
				f_dict[i] = valid_ranges

			f_dict[i] = [x for x in valid_ranges if x in f_dict[i]]

	def_dict = {}
	used_values = []
	not_done = True
	while not_done:
		for k, v in f_dict.items():
			if len(v) == 1:
				v = v[0]
				def_dict[k] = v
				used_values.append(v)
				
				for k2, v2 in f_dict.items():
					if k != k2:
						if v in v2:
							f_dict[k2] = [x for x in v2 if x != v]

				if all(len(y) == 1 for y in f_dict.values()):
					not_done = False

	departure = [x for x, y in def_dict.items() if y <= 5]

	s = 1
	for d in departure:
		s *= int(my_ticket[d])

	print(s)

p2_tickets = part1()
part2(p2_tickets)