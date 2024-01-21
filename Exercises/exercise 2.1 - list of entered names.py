names = []

while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)
    else:
        break

print('\nThe entered names are:')
print(names)
