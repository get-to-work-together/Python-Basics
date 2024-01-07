
# import section
import random



# data input section
n = int(input('How many random numbers do you want? '))



# processing section
random_numbers = [random.randint(1, 100) for _ in range(n)]

occuranceas = dict()
for number in set(random_numbers):
    occuranceas[number] = random_numbers.count(number)



# output section
print(random_numbers)

print(occuranceas)
