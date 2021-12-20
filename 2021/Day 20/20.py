lit = "#"
unlit = " "

with open("Day 20/inp.txt", "r") as file:
    enhance, image = file.read().split("\n\n")
    enhance = "".join([lit if c == "#" else unlit for c in enhance.strip("\n")])
    image = ["".join([lit if c == "#" else unlit for c in row]) for row in image.split("\n")]

s2b = {lit:"1", unlit:"0"}

def step(image, enhance, outer):
    w, h = len(image[0]), len(image)
    ec = s2b[outer]
    outer = enhance[int(9 * ec, 2)]

    new_img = []
    for y in range(-1,h+1):
        row = ""
        for x in range(-1,w+1):
            bits = ""
            for yoff in (-1,0,1):
                ny = y + yoff
                if ny < 0 or ny >= h:
                    bits += ec * 3
                    continue

                for xoff in (-1,0,1):
                    nx = x + xoff
                    if nx < 0 or nx >= w:
                        bits += ec
                        continue

                    bits += s2b[image[ny][nx]]
            row += enhance[int(bits, 2)]
        new_img.append(row)
    return new_img, outer

def printImg(img):
    for row in img:
        print(row)

def litCount(img):
    return sum([sum([p == lit for p in row]) for row in img])

def p1():   
    img = image
    otr = unlit
    for _ in range(2):
        img, otr = step(img, enhance, otr)
    
    print(litCount(img))
    return image, otr

def p2(o1):
    img, otr = o1
    for _ in range(50):
        img, otr = step(img, enhance, otr)
    
    print(litCount(img))
    # printImg(img)
    return

o1 = p1()
p2(o1)