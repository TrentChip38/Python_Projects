#simulate two games
# The first game: roll a die repeatedly. 
# Stop rolling once you get a five followed by a six. 
# Your number of rolls is the amount you pay, in dollars.
# The second game: same, except that the stopping condition 
# is a five followed by a five.

#daily codings answer:
from random import randint

NUM_TRIALS = 1000

def d6():
    return randint(1, 6)

def game_one():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 6:
        prev = curr
        curr = d6()
        cost += 1
    return cost

def ev_game_one():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_one())
    average = (sum(games) / len(games))
    print(average)
    return average

def game_two():
    prev, curr = None, None
    cost = 0
    while prev != 5 or curr != 5:
        prev = curr
        curr = d6()
        cost += 1
    return cost

def ev_game_two():
    games = []
    for i in range(NUM_TRIALS):
        games.append(game_two())
    average = (sum(games) / len(games))
    print(average)
    return average

#print(d6())
game1 = ev_game_one()
game2 = ev_game_two()
