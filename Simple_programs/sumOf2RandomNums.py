import random

num1 = random.randint(0, 100)
num2 = random.randint(0, 100)


def sum(x, y):
  sum = x + y
  print(str(x) + "+" + str(y) + "=" + str(sum))


sum(num1, num2)
