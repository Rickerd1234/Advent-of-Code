# Imports
from sys import argv
from os.path import dirname


# Read input from file
with open(dirname(argv[0]) + "/inp.txt", "r") as file:
    inp = [line.strip("\n") for line in file]

mapping = {
    "A": "Rock", "B": "Paper", "C":"Scissors",
    "X": "Rock", "Y": "Paper", "Z":"Scissors"}

scores = {
    "Rock": 1, "Paper": 2, "Scissors": 3
}

p1_wins = {("Rock", "Scissors"), ("Paper", "Rock"), ("Scissors", "Paper")}

# Part 1
def p1(inp):
    score = 0
    for game in inp:
        oppo, you = game.split(" ")
        oppo, you = mapping[oppo], mapping[you]
        
        if oppo == you: # Draw
            score += scores[you] + 3

        elif (oppo, you) in p1_wins: # Oppo wins
            score += scores[you]

        else: # You win
            score += scores[you] + 6

    print(score)

# Part 2
def p2(inp, _):
    score = 0
    for game in inp:
        oppo, outcome = game.split(" ")
        oppo = mapping[oppo]
        
        if outcome == "Y": # Draw
            score += scores[oppo] + 3

        elif outcome == "X": # Oppo wins
            you = [pick[1] for pick in p1_wins if pick[0] == oppo][0]
            score += scores[you]

        else: # You win
            you = [pick[0] for pick in p1_wins if pick[1] == oppo][0]
            score += scores[you] + 6

    print(score)
    return


# Run main functions
o1 = p1(inp)
p2(inp, o1)