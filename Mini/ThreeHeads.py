import random

simulations = 1000000
success = 0

for i in range(simulations):
    fourToss = random.randint(0, 1) + random.randint(0, 1) + random.randint(0,1) + random.randint(0, 1)
    if fourToss == 3:
        success += 1
    else:
        success += 0

print(success)