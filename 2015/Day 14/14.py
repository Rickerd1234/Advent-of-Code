with open("Day 14/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

def dist(reindeer, time):
    _, speed, duration, rest = reindeer
    time -= duration
    dist = speed
    dist += speed * (time // (duration + rest))
    return dist * duration

def p1():
    descs = inp.copy()
    data = []
    for desc in descs:
        name, info = desc.split(" can fly ")
        speed, info = info.split(" km/s for ")
        duration, info = info.split(" seconds, but then must rest for ")
        rest, _ = info.split(" seconds.")
        speed, duration, rest = int(speed), int(duration), int(rest)
        data.append((name, speed, duration, rest))

    print(max([dist(rein, 2503) for rein in data]))
    return data

def updateDists(data, rein_dists, t):
    for rein in data:
        n, s, d, r = rein
        if 0 < t % (r + d) <= d:
            diff = s
        else:
            diff = 0
        rein_dists[n] = rein_dists[n] + diff

def p2(o1):
    data = o1
    score_dict = {}
    rein_dists = dict([(rein[0], 0) for rein in data])
    for t in range(1, 2504):
        updateDists(data, rein_dists, t)
        m = max(rein_dists.values())
        for r, d in rein_dists.items():
            if d == m:
                if r not in score_dict:
                    score_dict[r] = 1
                else:
                    score_dict[r] += 1

    print(max(score_dict.values()))
    return

o1 = p1()
p2(o1)