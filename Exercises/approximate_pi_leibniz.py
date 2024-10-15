"""Leibniz approximation of PI"""

import math

n = 3_000_000

total = 0.0
add_or_subtract = True
for i in range(1, n, 2):
    if add_or_subtract == True:
        total = total + 1/i
    else:
        total = total - 1/i

    add_or_subtract = not add_or_subtract

pi = total * 4

print(f'Leibniz approximation of Pi = {pi}')

print(f'The math library has     Pi = {math.pi}')




d = abs(pi - math.pi)
percentage = d / math.pi * 100

print(f'This is accurate to {100 - percentage}%')

# print(d, math.log(d, 10), int(-math.log(d, 10)))

for i, (d1, d2) in enumerate(zip(f'{pi:.20f}', f'{math.pi:.20f}')):
    if d1 != d2:
        break

# accurate_decimals = int(-math.log(d, 10))
accurate_decimals = i - 1   # starts at 0 and do not count the decimal point

print(f'Accurate to {accurate_decimals} decimals')








##n = 10000
##
##total = 0.0
##power_of_3 = 1
##add = True
##for i in range(1, n, 2):
##    term = 1 / (i * power_of_3) 
##    total += term if add else -term
##    power_of_3 *= 3
##    add = not add
##
##pi = float(math.sqrt(12) * total)
##
##print('Leibniz approximation of Pi =', pi)




##n = 1000000
##
##total = 1.0
##for i in range(1, n):
##    nominator = 4 * i ** 2
##    denominator = nominator - 1
##    term = nominator / denominator 
##    total *= term
##
##pi = 2 * total
##
##print('Wallis product approximation of Pi =', pi)
