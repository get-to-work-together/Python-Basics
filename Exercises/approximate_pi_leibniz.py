"""Leinnix approximation of PI"""

n = 10000000

total = 0.0
add_or_subtract = True
for i in range(1, n, 2):
    if add_or_subtract:
        total = total + 1/i
    else:
        total = total - 1/i
    add_or_subtract = not add_or_subtract

pi = total * 4

print('Leibniz approximation of Pi =', pi)












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
