file = open("inp.txt", "r")

val = file.read().split("\n")

def getSeat(seat):
	r = [i for i in range(128)]
	for j in seat[:7]:
		if j == "F":
			r = r[:len(r)//2]
		elif j == "B":
			r = r[len(r)//2:]

	c = [i for i in range(8)]
	for j in seat[6:]:
		if j == "L":
			c = c[:len(c)//2]
		elif j == "R":
			c = c[len(c)//2:]

	return r[0], c[0]

def getSeatIDs():
	seat_ids = []
	for seat in val:
		r, c = getSeat(seat)
		seat_ids.append(r * 8 + c)
	return seat_ids

def part1():
	seat_ids = getSeatIDs()
	print(max(seat_ids))

def part2():
	seat_ids = getSeatIDs()
	seat_ids.sort()
	for seat_id in seat_ids:
		if seat_id + 1 not in seat_ids and seat_id + 2 in seat_ids:
			print(seat_id + 1)

part1()
part2()