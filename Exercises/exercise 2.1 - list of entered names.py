names = []

while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)
    else:
        break

print('\nThe entered names are:')

names.sort()

for name in names:
    print(name)