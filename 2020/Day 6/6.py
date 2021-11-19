file = open("inp.txt", "r")

inp = file.read()

def part1():
    groups = inp.split("\n\n")
    c = 0
    for g in groups:
        l = []
        persons = [x for x in g.split("\n") if x]
        
        for p in persons:
            l += [i for i in p if i not in l]

        c += len(l)
    print(c)

def part2():
    groups = inp.split("\n\n")
    c = 0
    for g in groups:
        persons = [x for x in g.split("\n") if x]
        
        p = persons[0]
        l = [i for i in p if i]
        
        for p in persons:
            l = [x for x in l if x in p]
            
        c += len(l)
    print(c)

part1()
part2()