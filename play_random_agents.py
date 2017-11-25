from functions import Match, RandomAgent
from copy import deepcopy
# play a game between two random agents, print the moves and the result

# initialize agents and match
player1 = RandomAgent()
player2 = deepcopy(player1)
match = Match(player1, player2)
# play loop until end game
match.play()
print("Player1's actions:")
for step in zip(player1.history):
    print(step)
print("Player2's actions:")
for step in zip(player2.history):
    print(step)
print('sequence of game states')
for _ in match.history:
    print(_)
print('game result is', match.result)
