import random
import decimal

simulations = 1000000
success = 0

for i in range(simulations):
    fourToss = random.randint(0, 1) + random.randint(0, 1) + random.randint(0,1) + random.randint(0, 1)
    if fourToss == 3:
        success += 1
    else:
        success += 0

    probability = success/simulations
    decimal_object = decimal.Decimal(probability)

    numerator, denominator = decimal_object.as_integer_ratio()


print(str(probability) + " or " + "%s / %s" % (numerator, denominator))