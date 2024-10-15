import random

# dice1 = random.randint(1, 6)
# dice2 = random.randint(1, 6)
# dice3 = random.randint(1, 6)
# dice4 = random.randint(1, 6)
# dice5 = random.randint(1, 6)
#
# total = dice1 + dice2 + dice3 + dice4 + dice5
#
# print('Thrown', dice1, dice2, dice3, dice4, dice5)
# print('Total', total)


dices = []

for i in range(20):
    dices.append(random.randint(1, 6))

print(dices)

print(sum(dices))

















# dice = []
# for _ in range(5):
#     dice.append(random.randint(1, 6))
# print('Thrown', dice)
# print('Total', sum(dice))


# dice = [random.randint(1, 6) for _ in range(5)]
# print('Thrown', dice)
# print('Total', sum(dice))



# print('Thrown', end=' ')
# total = 0
# for i in range(5):
#     d = random.randint(1, 6)
#     total += d
#     print(d, end=' ')
# print('\nTotal', total)



# dices = []
# for _ in range(5):
#     dices.append(random.randint(1, 6))
#
# print('Thrown', dices)
# print('Total', sum(dices))


# dices = random.choices(range(1, 7), k = 5)
#
# print('Thrown', dices)
# print('Total', sum(dices))


# dices = [random.randint(1, 6) for _ in range(5)]
#
# print('Thrown', dices)
# print('Total', sum(dices))
