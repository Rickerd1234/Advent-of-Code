# Imports
from tqdm import trange
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = file.read().strip("\n")

shapes = ["-","+","L","|","#"]
height_dict = {
    "-":1,
    "+":3,
    "L":3,
    "|":4,
    "#":2
}
dir_dict = {
    "<":-1,
    ">":1
}


class Block():
    def __init__(self, shape, tlx,tly):
        self.shape = shape
        self.tlx, self.tly = tlx, tly
        if shape == "-":
            self.bb = {
                (tlx,tly),
                (tlx+1,tly),
                (tlx+2,tly),
                (tlx+3,tly)
            }
        elif shape == "+":
            self.bb = {
                (tlx+1,tly),
                (tlx,tly-1),
                (tlx+1,tly-1),
                (tlx+2,tly-1),
                (tlx+1,tly-2),
            }
        elif shape == "L":
            self.bb = {
                (tlx+2,tly),
                (tlx+2,tly-1),
                (tlx+2,tly-2),
                (tlx+1,tly-2),
                (tlx,tly-2),
            }
        elif shape == "|":
            self.bb = {
                (tlx,tly),
                (tlx,tly-1),
                (tlx,tly-2),
                (tlx,tly-3)
            }
        elif shape == "#":
            self.bb = {
                (tlx,tly),
                (tlx+1,tly),
                (tlx,tly-1),
                (tlx+1,tly-1)
            }
        self.brx, self.bry = (max(self.bb, key=lambda c: c[0])[0], min(self.bb, key=lambda c: c[1])[1])
        
    def move(self, xo, yo, lw, rw, bottom, coll_bb):
        # Collides with wall
        if not (lw <= self.tlx + xo <= rw and lw <= self.brx + xo <= rw and self.bry + yo >= bottom):   
            return False

        # Collides with collision bounding box
        new_bb = {(x+xo, y+yo) for (x,y) in self.bb}
        if len(new_bb.intersection(coll_bb)) > 0:
            return False
        
        self.tlx += xo
        self.brx += xo
        self.tly += yo
        self.bry += yo
        self.bb = new_bb
        return True
            
    def getBB(self):
        return self.bb


def findRepetition(ls, min_length=1):
    for i in range(min_length,len(ls)//2+1):
        if ls[:i] == ls[i:2*i]:
            return ls[:i]
    return ls


# Part 1 & 2
def p12(inp):
    pt1_range = 2022
    search_range = max(len(inp) * len(shapes), pt1_range)
    pt2_range = 1_000_000_000_000

    lw, rw = 0, 6
    bottom = 0
    tlx = 2

    reset_patterns = {}
    reset_bbs = {}
    reset_moves = {}
    reset_step_order = []
    prev_reset_height = 0
    prev_reset_block = 0
    prev_reset_moves = 0

    step_i = 0
    c_max = 0
    coll_box = set()
    for i in range(search_range):
        shape = shapes[i % len(shapes)]
        tly = c_max + height_dict[shape] + 2
        block = Block(shape,tlx,tly)

        block.move(dir_dict[inp[step_i]], 0, lw, rw, bottom, coll_box)
        step_i = (step_i + 1) % len(inp)
        while block.move(0,-1, lw, rw, bottom, coll_box):
            block.move(dir_dict[inp[step_i]], 0, lw, rw, bottom, coll_box)
            step_i = (step_i + 1) % len(inp)

        coll_box = coll_box.union(block.getBB())
        c_max = max(c_max, max(coll_box, key=lambda c: c[1])[1] + 1)

        # Prune collision box if an entire row is filled, keep track of the details for part 2
        for j in range(c_max, max(0, c_max-5), -1):
            if all((i,j) in coll_box for i in range(lw, rw+1)):
                old_coll_box = coll_box.copy()
                coll_box = {(x,y) for (x,y) in coll_box if y > j}
                bottom = j + 1

                step_blocks = i - prev_reset_block
                prev_reset_block = i
                step_height = j - prev_reset_height
                prev_reset_height = j
                reset_move_count = step_i - prev_reset_moves
                prev_reset_moves = step_i

                if step_blocks in reset_patterns:
                    if step_height != reset_patterns[step_blocks]:
                        print(old_coll_box)
                        print(j, coll_box)
                        print("Pt2-Alert: number of blocks in step is no primary key for the height of the step")
                        exit()

                    reset_step_order.append((step_blocks, step_height, shape))
                else:
                    reset_step_order.append((step_blocks, step_height, shape))
                    reset_patterns[step_blocks] = step_height
                    reset_bbs[step_blocks] = {(x,y-bottom) for (x,y) in coll_box }
                    reset_moves[step_blocks] = reset_move_count

        # Print part 1 solution
        if i == pt1_range - 1:
            print(c_max)

    if len(reset_patterns) == 0:
        print("Pt2-Alert: no resets found in simulation")
        exit()

    # Find index from where a chunk is repeated
    for i in range(len(reset_patterns)):
        rep = findRepetition(reset_step_order[i:])
        if not len(rep) == len(reset_step_order[i:]):
            break

    if len(rep) == len(reset_step_order[i:]):
        print("Pt2-Alert: no repetition found in search_space")
        exit()

    start = reset_step_order[:i]

    # Find (chunk) index from where the repetition no longer holds:
    length_mismatch = False
    j = 1
    s = len(rep)
    while True:
        # If chunk is not equal to the repetition
        chunk = reset_step_order[i+s*j:i+s*(j+1)] 
        if len(chunk) != len(rep):
            length_mismatch = True
            break
        elif not chunk == rep:
            end = reset_step_order[i+s*j:]
            break
        j += 1

    if not length_mismatch:
        print("Pt2-Alert: Repetition does not hold for entire scope")
        exit()
    
    # Start computing the bottom for the last run of rocks
    bottom = 0                          # Bottom of the area
    remaining_search = pt2_range   # Number of blocks to drop
    moves = 0                           # Number of horizontal moves that is made

    # Compute the results for the start moves
    start_block_count = sum(step[0] for step in start)
    bottom += sum(step[1] for step in start)
    remaining_search -= start_block_count
    moves =  (moves + sum(reset_moves[step_blocks] for step_blocks, _, __ in start)) % len(inp)

    # Compute the results for the repeated moves
    rep_bottom = sum(step[1] for step in rep)
    rep_blocks = sum(step[0] for step in rep)
    rep_count = remaining_search//rep_blocks            # Number of repetitions
    bottom += rep_count * rep_bottom
    moves = (moves + sum(reset_moves[step_blocks] for step_blocks, _, __ in rep) * rep_count) % len(inp)
    remaining_search = remaining_search % rep_blocks    # Remaining number of blocks

    # Quickly cover reset jumps
    jump_i = 0
    while remaining_search > rep[jump_i][0]:
        step_blocks, step_height, step_shape = rep[jump_i]
        jump_i = (jump_i + 1) % len(rep)

        remaining_search -= step_blocks
        bottom += step_height
        moves = (moves + reset_moves[step_blocks]) % len(inp) 

    # Prepare for block dropping
    bottom += 1
    coll_box = {(x,y+bottom) for (x,y) in reset_bbs[step_blocks]}
    c_max = max(coll_box, key=lambda c: c[1])[1] + 1        # Running maximum
    shape_off = shapes.index(step_shape)                    # Get the offset of shapes (index of first shape that we drop)
    step_i = moves                                          # Index of horizontal moves

    for i in range(remaining_search -1):
        shape = shapes[(shape_off + i+1) % len(shapes)]
        tly = c_max + height_dict[shape] + 2
        block = Block(shape,tlx,tly)

        block.move(dir_dict[inp[step_i]], 0, lw, rw, bottom, coll_box)
        step_i = (step_i + 1) % len(inp)
        while block.move(0,-1, lw, rw, bottom, coll_box):
            block.move(dir_dict[inp[step_i]], 0, lw, rw, bottom, coll_box)
            step_i = (step_i + 1) % len(inp)

        coll_box = coll_box.union(block.getBB())
        c_max = max(c_max, max(coll_box, key=lambda c: c[1])[1] + 1)

    print(c_max)

# Run main functions
p12(inp)