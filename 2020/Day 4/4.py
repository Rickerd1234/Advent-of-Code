file = open("inp.txt", "r")

val = file.read().split("\n\n")

requirements = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part1():
	c = 0
	for pp in val:
		if all(r in pp for r in requirements):
			c += 1
	print(c)


hexabet = "0123456789abcdefABCDEF"
numberbet = "0123456789"

def part2():
	c = 0
	for pp in val:
		if all(r in pp for r in requirements):
			byr = int(pp.split("byr:", 1)[1].partition(" ")[0].partition("\n")[0])
			val1 = byr >= 1920 and byr <= 2002

			iyr = int(pp.split("iyr:", 1)[1].partition(" ")[0].partition("\n")[0])
			val2 = iyr >= 2010 and iyr <= 2020

			eyr = int(pp.split("eyr:", 1)[1].partition(" ")[0].partition("\n")[0])
			val3 = eyr >= 2020 and eyr <= 2030

			hgt = pp.split("hgt:", 1)[1].partition(" ")[0].partition("\n")[0]
			hgt_type = hgt[-2:]
			if hgt_type == "cm":
				h = int(hgt[:-2])
				val4 = h >= 150 and h <= 193
			elif hgt_type == "in":
				h = int(hgt[:-2])
				val4 = h >= 59 and h <= 76
			else:
				val4 = False

			hcl = pp.split("hcl:", 1)[1].partition(" ")[0].partition("\n")[0]
			if len(hcl) == 7:
				if hcl[0] == "#":
					val5 = all(c in hexabet for c in hcl[1:])
				else:
					val5 = False
			else:
				val5 = False

			ecl = pp.split("ecl:", 1)[1].partition(" ")[0].partition("\n")[0]
			val6 = ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

			pid = pp.split("pid:", 1)[1].partition(" ")[0].partition("\n")[0]
			val7 = len(pid) == 9 and all(c in numberbet for c in pid)

			if val1 and val2 and val3 and val4 and val5 and val6 and val7:
				c += 1
	print(c)


part1()
part2()