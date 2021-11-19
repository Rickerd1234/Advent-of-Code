file = open("inp.txt", "r")

test  = ''''''

val = file.read().split(",")
val = [int(v) for v in val]
#val = [0,3,6]

def part1():
	print(spoken(val, 2020))

def spokenOld(nums, index):
	track = nums.copy()
	track.reverse()
	for i in range(len(nums), index):
		if track[0] not in track[1:]:
			j = 0
		else:
			j = track[1:].index(track[0]) + 1

		track = [j] + track
	track.reverse()

	return track[-1]

def spoken(nums, index):
	last_seen = {}
	
	for i, j in enumerate(nums):
		if i != len(nums) -1:
			last_seen[j] = i

	last_val = j
	for i in range(len(nums), index):
		if last_val not in last_seen:
			j = 0
		else:
			j = i - last_seen[last_val] - 1

		last_seen[last_val] = i - 1
		last_val = j
	return last_val

def part2():
	print(spoken(val, 30000000))

part1()
part2()