file = open("inp.txt", "r").read()

# Parse decks
decks = file.split("\n\n")
p1, p2 = [list(map(int, deck.split("\n")[1:])) for deck in decks]
p1_copy, p2_copy = p1.copy(), p2.copy()
p1_copy2, p2_copy2 = p1.copy(), p2.copy()

# Play game
while len(p1) > 0 and len(p2) > 0:
    pick1, pick2 = p1.pop(0), p2.pop(0)
    
    if pick1 > pick2:
        p1 += [pick1, pick2]
    else:
        p2 += [pick2, pick1]

# Compute score (part 1)
deck = p1 + p2
score = sum((len(deck) - i)*c for i, c in enumerate(deck))
print(score)



# Part 2
INFINITE_GAME_STATE = 0
P1_GAME_WIN = 1
P2_GAME_WIN = 2

p1, p2 = p1_copy, p2_copy

def playRound(p1, p2, seen_decks_p1, seen_decks_p2):
    while p1 and p2:
        # Check for infinite game
        if p1 in seen_decks_p1:
            return INFINITE_GAME_STATE
        if p2 in seen_decks_p2:
            return INFINITE_GAME_STATE
        
        seen_decks_p1.append(p1.copy())
        seen_decks_p2.append(p2.copy())

        pick1, pick2 = p1.pop(0), p2.pop(0)
        # Create recursive round
        if len(p1) >= pick1 and len(p2) >= pick2:
            outcome = playRound(p1.copy()[:pick1], p2.copy()[:pick2], [], [])
            if outcome == P1_GAME_WIN or outcome == INFINITE_GAME_STATE:
                p1 += [pick1, pick2]
            else:
                p2 += [pick2, pick1]
        # Play normal round
        else:
            if pick1 > pick2:
                p1 += [pick1, pick2]
            else:
                p2 += [pick2, pick1]
        
        # Determine game state (after round)
        if len(p1) == 0:
            return P2_GAME_WIN
        elif len(p2) == 0:
            return P1_GAME_WIN

playRound(p1, p2, [], [])

deck = p1 + p2
score = sum((len(deck) - i)*c for i, c in enumerate(deck))
print(score)