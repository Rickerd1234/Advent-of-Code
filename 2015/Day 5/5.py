with open("Day 5/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def isNice(word):
    vowel_count = 0
    double = False
    previous = ""

    for char in word:
        if char in "aeiou":
            vowel_count += 1
        
        if char == previous:
            double = True
        
        if previous + char in ["ab", "cd", "pq", "xy"]:
            return False
        
        previous = char

    return vowel_count >= 3 and double

def p1():
    nices = 0
    for word in inp:
        if isNice(word):
            nices += 1
    print(nices)
    return

def isNice2(word):
    preprevious = ""
    previous = ""
    pair_dict = {}
    twice = False
    x_x = False

    for i, char in enumerate(word):
        pair = previous + char
        if pair not in pair_dict:
            pair_dict[pair] = i
        else:
            if i - pair_dict[pair] >= 2:
                twice = True

        if char == preprevious:
            x_x = True
        
        preprevious =  previous
        previous = char

    return twice and x_x

def p2():
    nices = 0
    for word in inp:
        if isNice2(word):
            nices += 1
    print(nices)
    return

p1()
p2()