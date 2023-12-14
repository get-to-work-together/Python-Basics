from __future__ import print_function

import math

user_input = input('Enter radius: ')
radius = float(user_input)

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Radius', radius)
print('Area', area)
print('Circumference', circumference)
