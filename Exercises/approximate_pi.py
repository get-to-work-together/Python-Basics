"""Monte Carlo approximation of PI"""

import random

n = 100_000_000

n_shorter_than_1 = 0
for _ in range(n):
    x = random.random()
    y = random.random()
    length = (x ** 2 + y ** 2) ** 0.5
    if length <= 1.0:
        n_shorter_than_1 += 1

q = n_shorter_than_1 / n

pi = q * 4

print('Monte Carlo approximation of Pi =', pi)





