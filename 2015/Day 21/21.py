# Imports
from sys import argv
from os.path import dirname
from z3 import *

# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

weapons = [
    ("Dagger", 8, 4, 0),
    ("Shortsword", 10, 5, 0),
    ("Warhammer", 25, 6, 0),
    ("Longsword", 40, 7, 0),
    ("Greataxe", 74, 8, 0)
]

armors = [
    ("Leather", 13, 0, 1),
    ("Chainmail", 31, 0, 2),
    ("Splintmail", 53, 0, 3),
    ("Bandedmail", 75, 0, 4),
    ("Platemail", 102, 0, 5)
]

rings = [
    ("Damage+1", 25, 1, 0),
    ("Damage+2", 50, 2, 0),
    ("Damage+3", 100, 3, 0),
    ("Defense+1", 20, 0, 1),
    ("Defense+2", 40, 0, 2),
    ("Defense+3", 80, 0, 3)
]

# Part 1
def p1(inp):
    B_hp_const, B_damage_const, B_armor_const = [int(a.split(": ")[1]) for a in inp]

    solver = Optimize()
    gold = Int("gold")
    P_hp = Int("P_hp")
    P_damage = Int("P_damage")
    P_armor = Int("P_armor")

    B_hp = Int("B_hp")
    B_damage = Int("B_damage")
    B_armor = Int("B_armor")

    # Set weapon requirements
    w_bools = []
    w_gold = Int("Weapon-Gold")
    w_dmg = Int("Weapon-Damage")
    for weapon, cst, dmg, _ in weapons:
        w_bool = Int(weapon)
        solver.add(Or(w_bool == 0, w_bool == 1))
        solver.add(If(w_bool > 0, w_gold == cst, True))
        solver.add(If(w_bool > 0, w_dmg == dmg, True))
        w_bools.append(w_bool)
    solver.add(Sum(w_bools) == 1) # Exactly one weapon

    # Set armor requirements
    a_bools = []
    a_gold = Int("Armor-Gold")
    a_arm = Int("Armor-Armor")
    for armor, cst, _, arm in armors:
        a_bool = Int(armor)
        solver.add(Or(a_bool == 0, a_bool == 1))
        solver.add(If(a_bool > 0, a_gold == cst, True))
        solver.add(If(a_bool > 0, a_arm == arm, True))
        a_bools.append(a_bool)
    solver.add(Sum(a_bools) <= 1) # At most one weapon
    solver.add(If(Sum(a_bools) == 0, And(a_gold == 0, a_arm == 0), True)) # If none, gain no stats from this

    # Set ring requirements
    r_bools = []
    for ring, cst, dmg, arm in rings:
        r_bool = Int(ring)
        solver.add(Or(r_bool == 0, r_bool == 1))
        r_bools.append(r_bool)
    solver.add(Sum(r_bools) <= 2) # At most two weapons

    # Compute gold and stats based on all combinations of two rings
    r_gold = Int("Ring-Gold")
    r_dmg = Int("Ring-Damage")
    r_arm = Int("Ring-Armor")
    for i, (ring, cst, dmg, arm) in enumerate(rings):
        for j, (ring2, cst2, dmg2, arm2) in enumerate(rings):
            if i <= j: continue
            r_bool, r_bool2 = r_bools[i], r_bools[j]
            solver.add(If(And(r_bool > 0, r_bool2 > 0), r_dmg == dmg + dmg2, True))
            solver.add(If(And(r_bool > 0, r_bool2 > 0), r_arm == arm + arm2, True))
            solver.add(If(And(r_bool > 0, r_bool2 > 0), r_gold == cst + cst2, True))

    # Compute gold and stats based on single ring
    for i, (ring, cst, dmg, arm) in enumerate(rings):
        r_bool = r_bools[i]
        solver.add(If(And(r_bool > 0, Sum(r_bools) == 1), And(r_gold == cst, r_dmg == dmg, r_arm == arm), True))

    # Set values based on no rings
    solver.add(If(Sum(r_bools) == 0, And(r_gold == 0, r_dmg == 0, r_arm == 0), True)) 

    # Combine player stats
    solver.add(P_hp == 100)
    solver.add(P_damage == w_dmg + r_dmg)
    solver.add(P_armor == a_arm + r_arm)

    # Define boss stasts
    solver.add(B_hp == B_hp_const)
    solver.add(B_damage == B_damage_const)
    solver.add(B_armor == B_armor_const)

    # Combine costs and set minimizer
    solver.add(gold == w_gold + a_gold + r_gold)

    # Create checkpoint for part 2
    solver.push()

    # Add requirement to play and win the game
    player_hit = If(P_damage - B_armor > 0, P_damage - B_armor, 1)
    boss_hit = If(B_damage - P_armor > 0, B_damage - P_armor, 1)
    solver.add((P_hp / boss_hit) >= (B_hp / player_hit))
    
    min_cost = solver.minimize(gold)

    # Solve and show solution
    solver.check()
    solver.lower(min_cost)
    model = solver.model()
    print(model[gold])
    return solver, P_hp, P_damage, P_armor, B_hp, B_damage, B_armor, gold

# Part 2
def p2(inp, o1):
    solver, P_hp, P_damage, P_armor, B_hp, B_damage, B_armor, gold = o1

    # Restore checkpoint
    solver.pop()

    # Add requirement to play and lose the game
    player_hit = If(P_damage - B_armor > 0, P_damage - B_armor, 1)
    boss_hit = If(B_damage - P_armor > 0, B_damage - P_armor, 1)
    solver.add((P_hp / boss_hit) < (B_hp / player_hit))
    
    max_cost = solver.maximize(gold)

    # Solve and show solution
    solver.check()
    solver.upper(max_cost)
    model = solver.model()
    print(model[gold])


# Run main functions
o1 = p1(inp)
p2(inp, o1)