names = []

while True:
    name = input('Enter a name: ')

    if name == '':
        break

    names.append(name)

print('\nThe entered names are:')

for name in sorted(names):
    print(name)
