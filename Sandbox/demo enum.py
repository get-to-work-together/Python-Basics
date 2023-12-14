from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(repr(Color.RED))

print(type(Color.RED))

print(isinstance(Color.GREEN, Color))

for color in Color:
    print(color)

