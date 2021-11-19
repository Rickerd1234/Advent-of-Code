def part1():
	inp = open("test.txt", "r")

	rules = [x.strip(".\n").split(" contain ") for x in inp]
	rules = [[x[0],x[1].split(", ")] for x in rules]
	
	direct_holders = [x[0] for x in rules if any("shiny gold bag" in y for y in x[1])]

	rule_dict = {}
	for rule in rules:
		rule_dict[rule[0]] = rule[1]
	
	c = 0
	for rule in rules:
		if recurseCheck(rule[0], rule_dict, direct_holders): c += 1
	print(c)

def recurseCheck(start, rules, direct_holders):
	print(start)
	print(start)
	if start in direct_holders:
		return True
	elif start in rules.keys():
		return any(recurseCheck(x, rules, direct_holders) for x in rules[start])
	else:
		return False

def part2():
	return

part1()
part2()
