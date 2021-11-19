import copy
file = open("inp.txt", "r")

test  = '''Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...'''

val = file.read().split("\n\n")

def getPatterns(tile):
	tile = tile.split("\n")[1:]
	top = [j for j, char in enumerate(tile[0]) if char == "#"]
	bottom = [j for j, char in enumerate(tile[-1]) if char == "#"]
	left = []
	right = []
	for i, row in enumerate(tile):
		if row[0] == "#":
			left.append(i)

		if row[-1] == "#":
			right.append(i)
	return top, right, bottom, left

tiles = {}
tile_patterns = {}
connect_dict = {}
diff = [(-1,0), (0,-1), (1,0), (0,1)]
for tile in val:
	ID, view = tile.split(":\n")
	ID = ID[5:]
	tiles[ID] = tile
	tile_patterns[ID] = getPatterns(tile)

def connectsTo(tile_id, tile_patterns):
	o = []
	#print(tile_id)
	for p2 in tile_patterns[tile_id]:
		for t, patterns in tile_patterns.items():
			if t != tile_id:
				#print(t, p2, patterns)
				if any(p == p2 or reverse(p) == p2 for p in patterns):
					#print("Yes")
					o.append(t)
	return o

def reverse(p):
	return list(reversed([(9 - i) for i in p]))

def neighborsPossible(neighbors):
	possible_tiles = []
	for k, d in enumerate(neighbors):
		#print(d, connectsTo(bl[d[1]][d[0]], tile_patterns))
		if k == 0:
			possible_tiles += connectsTo(d, tile_patterns)
		else:
			new = connectsTo(d, tile_patterns)
			possible_tiles = [t for t in possible_tiles if t in new]

	return possible_tiles

def findX(sea):
	for i, row in enumerate(sea):
		for j, tile in enumerate(row):
			if tile == "X":
				return i, j
	return (-1, -1)

def solve(curr, space):
	#print(space + str(curr))
	old = [[z for z in row] for row in curr]
		
	i, j = findX(curr)
	if (i, j) == (-1, -1):
		return True, curr

	else:
		neighbors = []
		for x, y in diff:
			if x + j in range(len(curr)):
				if y + i in range(len(curr)):
					if curr[i + y][j + x] != "X":
						neighbors.append(curr[y + i][x + j])
		#print(space + str(neighbors))
		possible_tiles = [t for t in neighborsPossible(neighbors) if not any(t in row for row in old)]

		#print(space + str(possible_tiles))
		if possible_tiles == []:
			return False, curr

		space += " "
		for t in possible_tiles:
			new = [[z for z in row] for row in old]
			new[i][j] = t
			succes, state = solve(new, space)
			if succes:
				return True, state
				print("WOOHOO")

	return False, curr

def printGrid(grid):
	for tile_id_row in grid:
		tile_size = 11
		for j in range(tile_size):
			if j == 0:
				continue

			line = ""
			for tile_id in tile_id_row:
				tile = tiles[tile_id].split("\n")
				line += tile[j] + " "
			print(line)
		print()

def rotateTile(tile_id, times):
	while times > 0:
		tile_patterns[tile_id] = [tile_patterns[tile_id][-1]] + list(tile_patterns[tile_id][:-1])
		times -= 1

	while times < 0:
		tile_patterns[tile_id] = list(tile_patterns[tile_id][1:]) + [tile_patterns[tile_id][0]]
		times += 1

def reverseTile(tile_id, side):
	#Horizontal Flip
	if side % 2 == 0:
		tile_patterns[tile_id] = [reverse(tile_patterns[tile_id][0]), tile_patterns[tile_id][1], reverse(tile_patterns[tile_id][2]), tile_patterns[tile_id][3]] 
	#Vertical Flip
	else:
		tile_patterns[tile_id] = [tile_patterns[tile_id][0], reverse(tile_patterns[tile_id][1]), tile_patterns[tile_id][2], reverse(tile_patterns[tile_id][3])] 
	

def rotatedTiles(grid):
	for i, row in enumerate(grid):
		for j, tile_id in enumerate(row):
			print(i, j)

			tile = tiles[tile_id].split("\n")[1:]
			tp = tile_patterns[tile_id]
			print(tp)

			if j - 1 in range(len(grid[0])):
				tp_prev = tile_patterns[grid[i][j-1]]			
				print(tp_prev)

				for m, a in enumerate(tp):
					if a in tp_prev:
						rotateTile(tile_id, 3-m)
						#print("Left?!")

					if reverse(a) in tp_prev:
						n = tp_prev.index(reverse(a))
						reverseTile(tile_id, m)
						#print("Reverse + Rotate")
						rotateTile(tile_id, 3-m)

			elif i - 1 in range(len(grid)):
				tp_prev = tile_patterns[grid[i-1][j]]
				print(tp_prev)

				for m, a in enumerate(tp):
					if a in tp_prev:
						rotateTile(tile_id, -m)
						#print("Top?!")


					if reverse(a) in tp_prev:
						reverseTile(tile_id, m)
						print("Reverse + Rotate")
						rotateTile(tile_id, -m)

			else:
				tp_right = tile_patterns[grid[i][j+1]]
				tp_below = tile_patterns[grid[1][0]]
				print(tp_right)
				print(tp_below)

				for m, a in enumerate(tp):
					if a in tp_right:
						rotateTile(tile_id, 1-m)
					
				if tile_patterns[tile_id][2] not in tp_below:
					reverseTile(tile_id, 2)
			print(tile_patterns[tile_id])


			


	return

def part1():
	corners = []
	for k, v in tile_patterns.items():
		connections = connectsTo(k, tile_patterns)
		connect_dict[k] = connections
		if len(connections) == 2:
			corners.append(k)
	p = 1
	for c in corners:
		p *= int(c)
	print(p)
	return corners

def part2(corners):
	# c1, c2, c3, c4 = corners
	# current = [[c1] +  ["X"] * 10 + [c2]] +  [["X"] * 12] * 10  + [[c3] +  ["X"] * 10 + [c4]]
	# succes, sol = solve(current, "")

	# if not succes:
	# 	current = [[c1] +  ["X"] * 10 + [c4]] +  [["X"] * 12] * 10  + [[c3] +  ["X"] * 10 + [c2]]
	# 	succes, sol = solve(current, "")

	# if not succes:
	# 	print("FAILED")
	# 	return
	sol = [['3413', '1117', '3517', '1459', '2333', '1721', '2887', '3559', '3617', '3061', '3863', '2617'], ['1499', '1361', '2297', '1399', '2753', '3319', '3727', '2969', '3613', '2179', '1999', '2857'], ['1747', '3853', '2689', '3169', '2953', '3329', '2237', '3527', '3011', '1091', '2243', '1619'], ['3299', '1951', '2749', '1163', '3671', '1531', '1669', '2393', '2341', '2129', '3391', '2141'], ['3529', '3917', '3593', '3407', '3989', '2473', '1861', '2213', '2609', '1249', '2221', '2029'], ['2273', '3947', '2417', '2957', '1009', '3229', '3623', '2137', '1597', '3163', '2083', '2069'], ['2377', '1889', '3469', '3803', '2551', '3251', '2671', '2267', '2633', '2003', '3541', '2683'], ['3217', '1609', '1697', '2089', '2713', '1051', '2357', '3943', '1523', '3793', '1787', '1997'], ['1901', '3701', '1217', '2897', '3181', '1367', '3923', '1489', '1423', '2027', '1451', '2087'], ['2311', '1831', '1559', '2909', '2999', '2731', '1213', '3881', '1709', '1049', '2699', '3067'], ['3253', '1283', '2447', '2293', '3539', '2579', '1783', '1993', '2389', '3583', '3691', '3373'], ['3371', '1301', '2789', '3767', '3301', '1879', '3931', '1381', '3257', '1093', '1693', '3607']]
	
	sol = rotatedTiles(sol)
	#printGrid(sol)

	# image = removeGaps(sol)
	# image = rotate(image)

	# print(seaRoughness(image))

corners = part1()
part2(corners)


# print(len(tiles))
# print(['3413', '1117', '3517', '1459', '2333', '1721', '2887', '3559', '3617', '3061', '3863', '2617'])
# print(neighborsPossible(["3413"]))
# print(neighborsPossible(["1117"]))
# print(neighborsPossible(["3517"]))
# print(neighborsPossible(["1459"]))
# print(neighborsPossible(["2333"]))
# print(neighborsPossible(["1721"]))
# print(neighborsPossible(["2887"]))
# print(neighborsPossible(["3559"]))
# print(neighborsPossible(["3617"]))
# print(neighborsPossible(["3061"]))
# print(neighborsPossible(["3863"]))
# print(neighborsPossible(["2617"]))