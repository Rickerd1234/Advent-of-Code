file = open("inp.txt", "r")

test = '''.#.
..#
###'''

#Modified input, it works only for odd row/column length, so add if necessary
val = file.read().split("\n")

def part1():
	gen = val.copy()
	s = len(gen)

	active = []
	off = s//2
	for y in range(-off, off + 1):
		for x in range(-off, off + 1):
			if gen[y + off][x + off] == "#":
				active.append((0, y, x))

	z_range = 1
	off += 1
	diff = [-1, 0, 1]
	for i in range(6):
		temp = active.copy()

		for z in range(-z_range, z_range + 1):
			
			for y in range(-off, off + 1):
				
				for x in range(-off, off + 1):
					cell = (z,y,x)
					isActive = cell in active

					#print()
					n_count = 0
					for z_off in diff:
						for y_off in diff:
							for x_off in diff:
								if not (z_off == y_off == x_off == 0):
									#print((z+z_off, (y+y_off), (x+x_off)))
									if (z+z_off, y+y_off, x+x_off) in active:
									#	print("n")
										n_count += 1

					#print(cell, isActive, n_count)
					if (n_count == 3 and not isActive):
						temp.append(cell)
						#print("added")
					elif (n_count in [2,3] and isActive):
						#print("kept")
						continue
					elif isActive:
						temp.remove(cell)
						#print("removed")
					else:
						#print("skipped")
						continue
		active = temp.copy()
		off += 1
		z_range += 1

	print(len(active))


def part2():
	gen = val.copy()
	s = len(gen)

	active = []
	off = s//2
	for y in range(-off, off + 1):
		for x in range(-off, off + 1):
			if gen[y + off][x + off] == "#":
				active.append((0, 0, y, x))

	zw_range = 1
	off += 1
	diff = [-1, 0, 1]
	for i in range(6):
		temp = active.copy()

		for w in range(-zw_range, zw_range + 1):

			for z in range(-zw_range, zw_range + 1):
				
				for y in range(-off, off + 1):
					
					for x in range(-off, off + 1):
						cell = (w,z,y,x)
						isActive = cell in active

						#print()
						n_count = 0
						for w_off in diff:
							for z_off in diff:
								for y_off in diff:
									for x_off in diff:
										if not (w_off == z_off == y_off == x_off == 0):

											if (w+w_off, z+z_off, y+y_off, x+x_off) in active:
												n_count += 1

						#print(cell, isActive, n_count)
						if (n_count == 3 and not isActive):
							temp.append(cell)
							#print("added")
						elif (n_count in [2,3] and isActive):
							#print("kept")
							continue
						elif isActive:
							temp.remove(cell)
							#print("removed")
						else:
							#print("skipped")
							continue
		active = temp.copy()
		off += 1
		zw_range += 1

	print(len(active))

part1()
part2()