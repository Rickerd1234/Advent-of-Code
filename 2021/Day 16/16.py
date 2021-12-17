with open("Day 16/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def getPackets(BITS, maxpacks = -1):
    packets = []
    #print(BITS, maxpacks)
    while len(BITS) >= 8 and (len(packets) < maxpacks or maxpacks == -1):
        #print(BITS, maxpacks)
        p = 0
        packetVersion = int(BITS[p:p+3], 2)
        p += 3
        typeID = int(BITS[p:p+3], 2)
        p += 3
        
        if typeID == 4:
            number = ""
            while BITS[p] != "0":
                number += BITS[p+1:p+5]
                p += 5
            number += BITS[p+1:p+5]
            BITS = BITS[p+5:]
            
            #print("found literal packet " + str(int(number, 2)))
            packets.append((packetVersion, typeID, int(number, 2)))
            continue

        lengthTypeID = BITS[p]
        p += 1
        
        if lengthTypeID == "0":
            length = int(BITS[p:p+15], 2)
            p += 15
            #print("looking for " + str(length) +  " bits")
            subs, _ = getPackets(BITS[p:p+length])
            BITS = BITS[p+length:]
        else:
            length = int(BITS[p:p+11], 2)
            p += 11
            #print("looking for " + str(length) +  " packets")
            subs, BITS = getPackets(BITS[p:], maxpacks=length)
        
        packets.append((packetVersion, typeID, subs))
    
    return packets, BITS

def getVersionSum(pack):
    ver, tID, cont = pack
    
    if tID == 4:
        return ver

    return ver + sum([getVersionSum(p) for p in cont])


def p1():
    h2b = lambda x: format(int(x, 16), '04b')
    BITS = "".join([h2b(h) for h in inp[0]])

    ps = getPackets(BITS)[0]
    print(getVersionSum(ps[0]))
    return ps

def getValue(pack):
    _, tID, cont = pack
    
    if tID == 4:
        if cont < 0:
            print("HEY", pack)
        return cont

    coll = [getValue(p) for p in cont]
    if tID == 0:
        if sum(coll) < 0:
            print("OOF")
        return sum(coll)
    elif tID == 1:
        P = 1
        for p in coll:
            P *= p
        return P
    elif tID == 2:
        return min(coll)
    elif tID == 3:
        return max(coll)
    elif tID == 5:
        return int(coll[0] > coll[1])
    elif tID == 6:
        return int(coll[0] < coll[1])
    elif tID == 7:
        return int(coll[0] == coll[1])

def p2(o1):
    ps = o1
    print(getValue(ps[0]))
    return

o1 = p1()
p2(o1)