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
# val = test.split("\n\n")

def getPatterns(tile):
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
	view = view.split("\n")
	tiles[ID] = view
	tile_patterns[ID] = getPatterns(view)
TILE_SIZE = len(view)

def connectsTo(tile_id, tile_patterns):
	o = []
	for p2 in tile_patterns[tile_id]:
		for t, patterns in tile_patterns.items():
			if t != tile_id:
				if any(p == p2 or reverse(p) == p2 for p in patterns):
					o.append(t)
	return o

def reverse(p):
	return list(reversed([(9 - i) for i in p]))

def neighborsPossible(neighbors):
	possible_tiles = []
	for k, d in enumerate(neighbors):
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
		possible_tiles = [t for t in neighborsPossible(neighbors) if not any(t in row for row in old)]

		if possible_tiles == []:
			return False, curr

		space += " "
		for t in possible_tiles:
			new = [[z for z in row] for row in old]
			new[i][j] = t
			succes, state = solve(new, space)
			if succes:
				return True, state

	return False, curr

def printTile(tile):
	for row in tile:
		print(row)

def printGrid(grid):
	for tile_id_row in grid:
		for j in range(TILE_SIZE):
			line = ""
			for tile_id in tile_id_row:
				tile = tiles[tile_id]
				line += tile[j] + " "
			print(line)
		print()

def rotateTile(tile_id, times):
	while times > 0:
		old = copy.deepcopy(tiles[tile_id])
		tiles[tile_id] = ["".join([old[i][j] for i in reversed(range(TILE_SIZE))]) for j in range(TILE_SIZE)]
		times -= 1

	while times < 0:
		old = copy.deepcopy(tiles[tile_id])
		tiles[tile_id] = ["".join([old[i][j] for i in range(TILE_SIZE)]) for j in reversed(range(TILE_SIZE))]
		
		times += 1
	
	tile_patterns[tile_id] = getPatterns(tiles[tile_id])

def flipTile(tile_id):
	old = copy.deepcopy(tiles[tile_id])
	tiles[tile_id] = ["".join(reversed(row)) for row in old]
	tile_patterns[tile_id] = getPatterns(tiles[tile_id])
	

def rotateTiles(grid):
	for i, row in enumerate(grid):
		for j, tile_id in enumerate(row):

			tp_normal = tile_patterns[tile_id]
			tp_rotator = [tp if i > 1 else reverse(tp) for i, tp in enumerate(tp_normal)]

			if j - 1 in range(len(grid[0])):
				tp_left = tile_patterns[grid[i][j-1]][1]
				if tp_left not in (tp_rotator):
					# print("flip")
					flipTile(tile_id)
					tp_rotator = [tp if i > 1 else reverse(tp) for i, tp in enumerate(tile_patterns[tile_id])]

				for m, a in enumerate(tp_rotator):

					if a == tp_left:
						# print("rotate clockwise", m)
						rotateTile(tile_id, 3-m)
						break

			elif i - 1 in range(len(grid)):
				tp_above = tile_patterns[grid[i-1][j]][2]
				tp_rotator = [reverse(tp) for tp in tp_rotator]
				if tp_above not in (tp_rotator):
					# print("flip")
					flipTile(tile_id)
					tp_rotator = [tp if i < 2 else reverse(tp) for i, tp in enumerate(tile_patterns[tile_id])]

				for m, a in enumerate(tp_rotator):
					
					if a == tp_above:
						# print("rotate cc", m)
						rotateTile(tile_id, -m)

			else:
				tp_right = tile_patterns[grid[0][1]]

				for m, a in enumerate(tp_normal):
					if a in tp_right:
						# print("rotate", (1-m))
						rotateTile(tile_id, 1-m)

def constructImage(id_grid):
	image = []
	for tile_id_row in id_grid:
		for i in range(1,TILE_SIZE-1):
			image_row = ""
			for tile_id in tile_id_row:	
				image_row += tiles[tile_id][i][1:-1]
			image.append(image_row)
	return image

def rotateImage(image):
	old = copy.copy(image)
	size = len(old)
	return ["".join([old[i][j] for i in reversed(range(size))]) for j in range(size)]

def flipImage(image):
	old = copy.copy(image)
	return ["".join(reversed(row)) for row in old]
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

def countMonsters(image):
	offsets = [(1,1),(4,1),(5,0),(6,0),(7,1),(10,1),(11,0),(12,0),(13,1),(16,1),(17,0),(18,-1),(18,0),(19,0)]
	counts = 0
	for y in range(1, len(image)-1):
		for x in range(len(image)-19):
			if image[y][x] == "#":
				monster = all([image[y+yo][x+xo] == "#" for (xo,yo) in offsets])
				counts += 1 if monster else 0
	return counts

def part1():
	corners = []
	for k in tile_patterns.keys():
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
	height = width = int(len(tiles)**(1/2))
	current = [[corners[0]] +  ["X"] * (width-1)] +  [["X"] * width] * (height-1)
	succes, sol = solve(current, "")

	if not succes:
		print("FAILED")
		return
	
	rotateTiles(sol)
	image = constructImage(sol)

	# Try all possible orientations
	runs = []
	runs.append(countMonsters(image))
	for _ in range(3):
		image = rotateImage(image)
		runs.append(countMonsters(image))

	image = flipImage(image)
	runs.append(countMonsters(image))
	for _ in range(3):
		image = rotateImage(image)
		runs.append(countMonsters(image))
	
	roughness = sum(sum([1 for c in row if c == "#"]) for row in image) - max(runs) * 15
	print(roughness)

corners = part1()
part2(corners)