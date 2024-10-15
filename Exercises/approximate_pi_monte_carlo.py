"""Monte Carlo approximation of PI"""

import math
import random

n = 10_000_000

n_shorter_than_1 = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    length = math.sqrt(x ** 2 + y ** 2)
    if length <= 1.0:
        n_shorter_than_1 += 1

q = n_shorter_than_1 / n

pi = q * 4

print('Monte Carlo approximation of Pi =', pi)

print(f'The math library has Pi = {math.pi}')

d = abs(pi - math.pi)
precentage = d / math.pi * 100

print(f'This is accurate to {100 - precentage}%')

for i, (d1, d2) in enumerate(zip(f'{pi:.20f}', f'{math.pi:.20f}')):
    if d1 != d2:
        break

# accurate_decimals = int(-math.log(d, 10))
accurate_decimals = i - 1   # i starts at 0 and also counts the decimal point

print(f'Accurate to {accurate_decimals} decimals')




