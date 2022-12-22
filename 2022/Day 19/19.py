# Imports
from collections import deque
from functools import cache
import math
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    blueprints = {}
    for line in file:
        bp_no, rem = line.strip().replace("Blueprint ", "").split(": ")
        cost_lines = rem.split(". ")
        cost_values = []
        for cost_line in cost_lines:
            splits = cost_line.split(" ")
            for value in splits:
                if value.isnumeric():
                    cost_values.append(int(value))
        blueprints[int(bp_no)] = {
            "ore": {"ore": cost_values[0]},
            "clay": {"ore": cost_values[1]},
            "obs": {"ore": cost_values[2], "clay": cost_values[3]},
            "geo": {"ore": cost_values[4], "obs": cost_values[5]},
        }
    inp = blueprints


# Part 1
def p1(blueprints):
    max_t = 24
    s = 0
    for bp_id, bp in blueprints.items():
        (ore, ore_r, clay, clay_r, obs, obs_r, geo, geo_r, t) = (0,1,0,0,0,0,0,0,0)
        queue = deque([(ore, ore_r, clay, clay_r, obs, obs_r, geo, geo_r, t)])
        handled = set()
        final_states = []
        opt = 0
        while queue:
            (ore, ore_r, clay, clay_r, obs, obs_r, geo, geo_r, t) = queue.pop()
            ttl = max_t - t

            if geo + geo_r*ttl + (ttl*(ttl-1)//2) < opt:
                continue
            if geo > opt:
                opt = geo

            if t > max_t:
                continue

            if t < max_t:               
                if ore >= bp["geo"]["ore"] and obs >= bp["geo"]["obs"]:
                    new = (ore-bp["geo"]["ore"]+ore_r, ore_r, clay+clay_r, clay_r, obs-bp["geo"]["obs"]+obs_r, obs_r, geo+geo_r, geo_r+1, t+1)
                    if new not in handled:
                        queue.append(new)
                        handled.add(new)

                if ore >= bp["obs"]["ore"] and clay >= bp["obs"]["clay"] and obs_r < bp["geo"]["obs"]:
                    new = (ore-bp["obs"]["ore"]+ore_r, ore_r, clay-bp["obs"]["clay"]+clay_r, clay_r, obs+obs_r, obs_r+1, geo+geo_r, geo_r, t+1)
                    if new not in handled:
                        queue.append(new)
                        handled.add(new)
                
                if ore >= bp["clay"]["ore"] and clay_r < bp["obs"]["clay"]:
                    new = (ore-bp["clay"]["ore"]+ore_r, ore_r, clay+clay_r, clay_r+1, obs+obs_r, obs_r, geo+geo_r, geo_r, t+1)
                    if new not in handled:
                        queue.append(new)
                        handled.add(new)
                
                if ore >= bp["ore"]["ore"] and ore_r < max(bp["ore"]["ore"], bp["clay"]["ore"], bp["obs"]["ore"], bp["geo"]["ore"]):
                    new = (ore-bp["ore"]["ore"]+ore_r, ore_r+1, clay+clay_r, clay_r, obs+obs_r, obs_r, geo+geo_r, geo_r, t+1)
                    if new not in handled:
                        queue.append(new)
                        handled.add(new)
                
                new = (ore+ore_r, ore_r, clay+clay_r, clay_r, obs+obs_r, obs_r, geo+geo_r, geo_r, t+1)
                if new not in handled:
                    queue.append(new)
                    handled.add(new)
            else:
                final_states.append((ore, ore_r, clay, clay_r, obs, obs_r, geo, geo_r, t))
        opt = max(final_states, key=lambda c: c[6])
        s += bp_id * opt[6]
    print(s)

opts = {1:0, 2:0, 3:0}
@cache
def recursiveMax(current, bp_id):
    bp = blueprints[bp_id]
    (ore, ore_r, clay, clay_r, obs, obs_r, geo, geo_r, prev_ore, ttl) = current
    options = set()

    if geo + (geo_r*ttl) + (ttl*(ttl-1)//2) < opts[bp_id]:
        return current
    if geo > opts[bp_id]:
        opts[bp_id] = geo

    if ttl == 0:
        return current

    if ttl > 0:
        if ore >= bp["geo"]["ore"] >= prev_ore and obs >= bp["geo"]["obs"]:
            new = (ore-bp["geo"]["ore"]+ore_r, ore_r, clay+clay_r, clay_r, obs-bp["geo"]["obs"]+obs_r, obs_r, geo+geo_r, geo_r+1, 0, ttl-1)
            options.add(new)

        if ore >= bp["obs"]["ore"] >= prev_ore and clay >= bp["obs"]["clay"] and obs_r <= bp["geo"]["obs"] and (ttl*obs_r)+obs < bp["geo"]["obs"]*ttl:
            new = (ore-bp["obs"]["ore"]+ore_r, ore_r, clay-bp["obs"]["clay"]+clay_r, clay_r, obs+obs_r, obs_r+1, geo+geo_r, geo_r, 0, ttl-1)
            options.add(new)
        
        if  ore >= bp["clay"]["ore"] >= prev_ore and (clay_r*ttl)+clay < bp["obs"]["clay"]*ttl:
            new = (ore-bp["clay"]["ore"]+ore_r, ore_r, clay+clay_r, clay_r+1, obs+obs_r, obs_r, geo+geo_r, geo_r, 0, ttl-1)
            options.add(new)
        
        if ore >= bp["ore"]["ore"] >= prev_ore and (ore_r*ttl)+ore < max(bp["ore"]["ore"], bp["clay"]["ore"], bp["obs"]["ore"], bp["geo"]["ore"])*ttl:
            new = (ore-bp["ore"]["ore"]+ore_r, ore_r+1, clay+clay_r, clay_r, obs+obs_r, obs_r, geo+geo_r, geo_r, 0, ttl-1)
            options.add(new)
        
        if len(options) < 4:
            new = (ore+ore_r, ore_r, clay+clay_r, clay_r, obs+obs_r, obs_r, geo+geo_r, geo_r, ore, ttl-1)
            options.add(new)

    return max(map(lambda opt: recursiveMax(opt, bp_id), options), key=lambda c: c[6])

# Part 2
def p2(blueprints, _):
    max_t = 32
    s = 1
    for bp_id in blueprints:
        if bp_id > 3: break
        current = (0,1,0,0,0,0,0,0,0,max_t)
        opt = recursiveMax(current, bp_id)
        s *= opt[6]
    print(s)


# Run main functions
o1 = p1(inp)
p2(inp, o1)