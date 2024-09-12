names = []

while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)

    else:
        break



print('\nThe entered names are:')

for name in sorted(names):
    print(name)
