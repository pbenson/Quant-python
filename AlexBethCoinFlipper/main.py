import random

num_trials = 1000000
bethWinCount = 0
bethWinOn2ndTurnCount = 0
for _ in range(num_trials):
    beth_turn_count = 0
    while(True):
        if random.random() < 0.25:
            break
        beth_turn_count += 1
        if random.random() < 0.25:
            bethWinCount += 1
            if beth_turn_count == 2:
                bethWinOn2ndTurnCount += 1
            break

print('Beth win percentage: ' + str(100 * bethWinCount / num_trials))

print('When she won, the % wins on her 2nd turn: ' + str(100 * bethWinOn2ndTurnCount / bethWinCount))
