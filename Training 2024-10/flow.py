gender = 'm'

if gender == 'm':
    print('dear sir')
elif gender == 'v':
    print('dear madame')
elif gender == 'x':
    print('dear person')
else:
    print('beloved')

    print('how do you do?')



gender = 'f'

match gender:
    case 'm':
        print('man')
    case 'f' | 'v':
        print('woman')
    case _:
        print('other')


for number in range(1, 11, 2):
    print(number)

import string
for c in string.ascii_lowercase:
    print(c)

magicnumber = 11

for i in range(1, 21):
    if i == magicnumber:
        continue
    print(i)
