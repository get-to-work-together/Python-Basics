class Vector:

    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __str__(self):
        return f'[{self._x}, {self._y}]'

    def __repr__(self):
        return f'Vector({self._x}, {self._y})'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        return (self._x ** 2 + self._y ** 2) ** 0.5

    # def __eq__(self, other):
    #     return self.length() == other.length()
    #
    # def __ne__(self, other):
    #     return self.length() != other.length()
    #
    # def __gt__(self, other):
    #     return self.length() > other.length()
    #
    # def __ge__(self, other):
    #     return self.length() >= other.length()
    #
    # def __lt__(self, other):
    #     return self.length() < other.length()
    #
    # def __le__(self, other):
    #     return self.length() <= other.length()

# -------------------------

v1 = Vector(4, 4)
v2 = Vector(-2, 4)

print(v1)
print(v2)

print(repr(v1))
print(repr(v2))

vectors = [
    Vector(4, 8),
    Vector(5, 2),
    Vector(4, 4),
    Vector(9, 7),
    Vector(4, 3),
    Vector(5, 1),
    Vector(1, 5),
    Vector(8, 2),
    Vector(9, 5),
]

for v in sorted(vectors, key = lambda v: v.length()):
    print(v, v.length())