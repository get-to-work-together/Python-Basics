import math

radius = float(input('Enter radius: '))

area = math.pi * radius ** 2
circumference = 2 * math.pi * radius

print('Radius', radius)
print('Area', area)
print('Circumference', circumference)

print(f'Radius: {radius:.3f}')
print(f'Area: {area:.3f}')
print(f'Circumference {circumference:.3f}')

print('Radius: %.3f' % radius)
print('Area: %.3f' % area)
print('Circumference %.3f' % circumference)