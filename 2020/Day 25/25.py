file = open("inp.txt", "r").read()

inp = file.split("\n")
pk1, pk2 = map(int, inp)
# pk1, pk2 = 5764801, 17807724

mod = 20201227

def getLoopSize(sn, outcome):
    loop_size = 0
    val = 1
    while val != outcome:
        val *= sn
        val %= mod
        loop_size += 1
    return loop_size

def transform(sn, loop_size):
    val = 1
    for _ in range(loop_size):
        val *= sn
        val %= mod
    return val

# Part 1
loop_size2 = getLoopSize(7, pk2)
print(transform(pk1, loop_size2))

# Part 2 is free, once you've completed all prior parts