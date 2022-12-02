from tqdm import trange
file = open("inp.txt", "r").read()

cups = list(map(int, file))
cups_copy = cups.copy()
MIN, MAX = min(cups), max(cups)

def move(cups, active):
    pickup = cups[active+1:active+4] + (cups[0:active+4-len(cups)] if active+4 > len(cups) else [])
    temp = [cup for cup in cups if cup not in pickup]

    target = cups[active] - 1
    while target in pickup or target < MIN:
        if target < MIN:
            target = MAX
        else:
            target -= 1
    destination = temp.index(target)
    new = temp[:destination+1] + pickup + temp[destination+1:]

    new_active = new.index(cups[active])
    new_active = (new_active + 1) % len(cups)

    return new, new_active

active = 0
for _ in range(100):
    cups, active = move(cups, active)

# Part 1
marker = cups.index(1)
print("".join(map(str, cups[marker+1:] + cups[:marker])))


# Part 2
S = 1_000_000
steps = 10_000_100
cups_S = len(cups_copy)

# Successor links
links = [cups_copy[(cups_copy.index(i+1)+1) % cups_S] for i in range(cups_S)] + [i for i in range(MAX+2, S+1)]
if cups_S < S:
    links[cups_copy[-1]-1] = cups_S + 1
    links = links + [cups_copy[0]]

# Reconstruct original cups setup (used for debugging)
def reconstruct(links, first, max_len=-1):
    out = []
    prev = first
    i = 0
    while prev not in out:
        if i > max_len and max_len > 0:
            break
        out.append(prev)
        prev = links[prev-1]
        i += 1
    return out

active = cups_copy[0]
for _ in trange(steps):
    # Get next element
    succ = links[active-1]

    # Define pickup, succ -> element after pickup
    pickup = []
    for _ in range(3):
        pickup.append(succ)
        succ = links[succ-1]

    # Get target to place the pickup
    target = active - 1
    while target in pickup or target < MIN:
        if target < MIN:
            target = S
        else:
            target -= 1
    
    new_after_pickup = links[target-1]

    # Update links
    links[active-1] = succ
    links[target-1] = pickup[0]
    links[pickup[-1]-1] = new_after_pickup
    active = succ

first = links[0]
second = links[first-1]
print(first * second)