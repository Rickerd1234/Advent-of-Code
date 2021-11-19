def checkTrees(x, y):
	inp = open("3.txt", "r")

	c = 0
	j = 0
	for i, line in enumerate(inp):
		l = line.strip("\n")
		if i % y == 0:
			ind = (j * x) % len(l)
			j += 1
			#print(ind,i)
			#print(l[ind])
			if l[ind] == "#":
				c += 1
	return c


# def checkTrees(r):
# 	c=0
# 	y = 0
# 	for i in inp:
# 		l = i.strip("\n")
# 		x = (r * y) % len(l)
# 		if l[x] == "#":
# 			c += 1
# 		y += 1
# 	return c

def part1():
	print(checkTrees(3, 1))

def part2():
	c = 1
	for i in [(1,1), (3,1), (5,1), (7,1), (1,2)]:
		out = checkTrees(i[0], i[1])
		#print(out)
		c *= out
	print(c)

#print(checkTrees(1,2))

part1()
part2()
