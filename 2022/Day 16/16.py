# Imports
from collections import deque
from functools import cache
from itertools import combinations, permutations
from sys import argv
from os.path import dirname

# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    edge_dict = {}
    flow_dict = {}
    inp = []
    for line in file:
        valve, rest = line.replace("Valve ","").strip().split(" has flow rate=")
        filter_str = "tunnels lead to valves" if "valves" in rest else "tunnel leads to valve"
        flow_rate, pipes = rest.split(f"; {filter_str} ")
        pipes = pipes.split(", ")
        inp.append((valve, int(flow_rate), pipes))
        flow_dict[valve] = int(flow_rate)
        edge_dict[valve] = pipes

    dijkstra_dicts = {}
    for valve, fr, _ in inp:
        # Only for valves with a flow rate > 0
        # Compute the shortest paths to all other valves
        if fr > 0 or valve == "AA":
            dist_dict = {valve:0}
            queue = deque()
            queue.append(valve)
            while queue:
                node = queue.popleft()
                for neighbor in edge_dict[node]:
                    if neighbor not in dist_dict:
                        dist_dict[neighbor] = dist_dict[node] + 1
                        queue.append(neighbor)
            
            # Filter the shortest path dict for flow rate > 0
            dijkstra_dicts[valve] = dict(((k,v) for k,v in dist_dict.items() if flow_dict[k] > 0 and k != valve))


# Part 1
def p1(_):
    max_t = 30
    start = "AA"

    queue = deque([(start, 0, "")])
    possible_states = {(start, 0, ""): (0, 0, set(), "AA")}
    while queue:
        (valve, time, open_str) = current = queue.popleft()
        acc_flow, flow, opened, path = possible_states[current]

        # Move to and open 'neighbor' for 'dist' + 1 time
        for neighbor, dist in dijkstra_dicts[valve].items():
            if neighbor not in opened:
                if time + dist + 1 <= max_t:
                    new_state = (neighbor, time+dist+1, open_str)
                    if not new_state in possible_states or possible_states[new_state][0] < acc_flow + flow*(dist+1):
                        new_opened = opened.copy()
                        new_opened.add(neighbor)
                        possible_states[new_state] = (acc_flow + flow*(dist+1), flow + flow_dict[neighbor], new_opened, path+"_"+neighbor)
                        queue.append(new_state)

    
    computeTotal = lambda k, v: (max_t - k[1]) * v[1] + v[0]
    opt = max(possible_states.items(), key=lambda v: computeTotal(*v))
    print(computeTotal(*opt))


@cache
def getOrder(time, order, max_t):
    out = []
    for neighbor, dist in dijkstra_dicts[order[-2:]].items():
        if neighbor not in order and time + dist + 1 <= max_t:
            out.append((order+neighbor, time + dist + 1))
    return out

@cache
def getMax(items, max_t, start):
    m = 0
    for perm in permutations([items[i:i+2] for i in range(2,len(items),2)]):
        if len(perm) == 0:
            continue
        t = dijkstra_dicts[start][perm[0]] + 1
        score = 0
        flow = flow_dict[perm[0]]
        for i in range(len(perm)-1):
            t += dijkstra_dicts[perm[i]][perm[i+1]] + 1
            score += (dijkstra_dicts[perm[i]][perm[i+1]] + 1) * flow
            flow += flow_dict[perm[i+1]]
        score += (max_t - t) * flow
        m = max(m, score)
    return m

# print(getMax("AAHH", 26, "AA"))

def p2(_, __):
    max_t = 26
    start = "AA"

    p1s = [[(start, 0)]]
    while True:
        new = []
        for order, time in p1s[-1]:
            new += getOrder(time, order, max_t)
        if len(new) > 0:
            p1s.append(new)
        else: break
    
    getMaxDist = lambda last: max(dijkstra_dicts[last].values())

    states = [item for sublist in p1s for item in sublist if item[1] >= max_t - getMaxDist(item[0][-2:])]

    run_max = 0
    for (p1, _), (p2, _) in combinations(states[-4000:], 2):
        s_p1, s_p2 = set([p1[i:i+2] for i in range(2,len(p1),2)]), set([p2[i:i+2] for i in range(2,len(p2),2)])
        if len(s_p1.intersection(s_p2)) > 0:
            continue
        else:
            new_max = getMax(p1, max_t, start) + getMax(p2, max_t, start)
            run_max = max(run_max, new_max)
    print(run_max)


# Run main functions
o1 = p1(inp)
p2(inp, o1)