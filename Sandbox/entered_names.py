from __future__ import print_function

names = []

while True:
    name = input('Enter a name: ')

    if name:
        names.append(name)
    else:
        break

for name in sorted(names):
    print(name)
