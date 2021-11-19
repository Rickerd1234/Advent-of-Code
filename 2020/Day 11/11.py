file = open("inp.txt", "r")

test  = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''

inp = file.read().split("\n")


def simulate1(old, val):
	surrounding = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1), (1,-1), (1,0), (1,1)]
	#For each cel in the column
	for i in range(len(val)):
		for j in range(len(val)):

			occ = 0
			#For each of the 8 directions
			for (x,y) in surrounding:
				ix, jy = i + x, j + y
				#Not end of row/column
				if not (ix == len(val) or ix == -1 or jy == len(val) or jy == -1):
					#Occupied seat found
					if old[ix][jy] == "#":
						occ += 1

			#If should be emptied now
			if old[i][j] == "#" and occ >= 4:
				val[i] = val[i][:j] + "L" + val[i][j + 1:]
			#If should be occupied now
			elif old[i][j] == "L" and occ == 0:
				val[i] = val[i][:j] + "#" + val[i][j + 1:]

def simulate2(old, val):
	surrounding = [(-1,-1), (-1,0), (-1,1),(0,-1), (0,1), (1,-1), (1,0), (1,1)]
	#For each cel in the column
	for i in range(len(val)):
		for j in range(len(val)):

			seen_surrounding = []
			occ = 0
			#For each of the 8 directions
			for (x,y) in surrounding:

				d = 1
				#While this direction has not been properly checked yet
				while (x,y) not in seen_surrounding:

					ix, jy = i + x * d, j + y * d
					#For seat in line -> (ix, jy) = (i,j) + d * (x,y)
					if not (ix == len(val) or ix == -1 or jy == len(val) or jy == -1):
						#Occupied seat found
						if old[ix][jy] == "#":
							occ += 1
							seen_surrounding.append((x, y))
						#Empty seat found
						elif old[ix][jy] == "L":
							seen_surrounding.append((x, y))
						d += 1
					#End of row/column
					else:
						seen_surrounding.append((x, y))

			#If should be emptied now
			if old[i][j] == "#" and occ >= 5:
				val[i] = val[i][:j] + "L" + val[i][j + 1:]
			#If should be occupied now
			elif old[i][j] == "L" and occ == 0:
				val[i] = val[i][:j] + "#" + val[i][j + 1:]

def countOccupied(val):
	s = 0
	for row in val:
		for char in row:
			if char == "#":
				s += 1
	return s

def show(arr):
	return
	print()
	print()
	print()
	for row in arr:
		print(row)
	print()
	print()
	print()

def part1():
	val = inp.copy()
	old = []
	while old != val:
		show(val)
		old = val.copy()
		simulate1(old, val)
	show(val)
	print(countOccupied(val))

def part2():
	val = inp.copy()
	old = []
	while old != val:
		show(val)
		old = val.copy()
		simulate2(old, val)
	show(val)
	print(countOccupied(val))

part1()
part2()