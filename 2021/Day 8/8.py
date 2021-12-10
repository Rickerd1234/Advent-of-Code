with open("Day 8/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

unique_lengths = {2:1, 4:4, 3:7, 7:8}

def p1():
    notes = inp.copy()
    c = 0
    for note in notes:
        _, opt = note.split(" | ")
        lens = [len(o) for o in opt.split(" ")]
        c += sum([1 for l in lens if l in unique_lengths])
    print(c)
    return notes

def getDiff(a, b):
    return "".join(set(a).symmetric_difference(set(b)))

def getUnion(a, b):
    return "".join(set(a).union(set(b)))

def getSegmentValues(smap):
    sms = ["" for _ in range(7)]

    #Difference between 1 and 7 -> upper segment
    sms[0] = getDiff(smap[1], smap[7])

    #Middle segment: len(6) but not contain diff between 1 and 4
    diff4_1 = getDiff(smap[1], smap[4])
    t = [d for d in smap[-1] if len(d) == 6]    #0, 6, 9
    for d in t:
        if not diff4_1[0] in d:
            sms[3] = diff4_1[0]
            smap[-1].remove(d)
            smap[0] = d
            break
        elif not diff4_1[1] in d:
            sms[3] = diff4_1[1]
            smap[-1].remove(d)
            smap[0] = d
            break

    #Lower segment: len(6) contains all from 4 and 7 (remaining part)
    union4_7 = getUnion(smap[4], smap[7])
    t = [d for d in smap[-1] if len(d) == 6]    #6, 9
    for d in t:
        if set(union4_7).issubset(d):
            smap[-1].remove(d)
            smap[9] = d
            sms[6] = getDiff(d, union4_7)
        else:
            smap[-1].remove(d)
            smap[6] = d
            sms[2] = getDiff(d, smap[8])

    sms[4] = getDiff(smap[8], smap[9])

    #Extract 2
    for d in smap[-1]:
        if set("".join(sms)).issubset(d):
            smap[-1].remove(d)
            smap[2] = d
            break

    #Extract 3 and 5
    for d in smap[-1].copy():
        if sms[2] in d:
            smap[-1].remove(d)
            smap[3] = d
            
        else:
            smap[-1].remove(d)
            smap[5] = d

    sms[1] = getDiff(smap[3], smap[9])
    sms[5] = getDiff(smap[2] + sms[1], smap[8]) 
    
    return smap

def getValue(smap, opts):
    smap = dict([(v,k) for k,v in smap.items() if k != -1])
    num = ""
    for opt in opts:
        sopt = ''.join(sorted(opt))
        num += str(smap[sopt])
    return int(num)
        

def p2(o1):
    notes = o1
    c = 0
    for note in notes:
        ipt, opt = note.split(" | ")
        data = ipt.split(" ") + opt.split(" ")

        smap = {-1:[]}
        for d in data:
            ds = ''.join(sorted(d))
            if len(ds) in unique_lengths:
                smap[unique_lengths[len(ds)]] = ds
            else:
                if ds not in smap[-1]:
                    smap[-1] += [ds]

        smap[-1].sort(key=len)
        smap = getSegmentValues(smap)

        c += getValue(smap, opt.split(" "))

    print(c)
    return

o1 = p1()
p2(o1)