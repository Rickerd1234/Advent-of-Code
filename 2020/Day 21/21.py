file = open("inp.txt", "r").read()

inp = file.split("\n")

# Create a dictionary with the ingredient sets for each allergen
# Also create a list containing all ingredients combined
possible_ingredients = {}
complete_ingredient_list = []
for line in inp:
    ingredients, allergens = line[:-1].split(" (contains ")
    complete_ingredient_list += ingredients.split(" ")
    ing_set = set(ingredients.split(" "))
    for alg in allergens.split(", "):
        if alg in possible_ingredients:
            possible_ingredients[alg].append(ing_set)
        else:
            possible_ingredients[alg] = [ing_set]

# Filter the common ingredients for each allergen
for alg, ing_sets in possible_ingredients.items():
    common_set = set(ing_sets[0])
    common_set = common_set.intersection(*ing_sets)
    possible_ingredients[alg] = common_set


# Use set intersection to get the unique ingredient for each allergen
solved_ingredients = {}
sorted_sets = sorted(possible_ingredients.items(), key=lambda x: len(x[1]))
while len(sorted_sets) > 0:
    alg, ing_set = sorted_sets[0]
    
    if len(ing_set) == 1:
        ing = ing_set.pop()
        solved_ingredients[alg] = ing
        sorted_sets.remove((alg, ing_set))
        for alg, ing_set in sorted_sets:
            ing_set.discard(ing)
    
    sorted_sets = sorted(sorted_sets, key=lambda x: len(x[1]))

# Part 1 solution
print(sum(1 for ing in complete_ingredient_list if ing not in solved_ingredients.values()))

# Part 2 solution
print(",".join([ing for alg, ing in sorted(solved_ingredients.items(), key=lambda x: x[0])]))