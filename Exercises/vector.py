
class Vector:
    """My Vector class which also supports vector addition"""

    def __init__(self, x, y):
        self._x = x         # set _x attribute
        self._y = y

    def __str__(self):
        return f'[{self._x}, {self._y}]'

    def __add__(self, other):
        return Vector(self._x + other._x, self._y + other._y)

    def length(self):
        """Calculate the langth using pythagoras"""
        return (self._x ** 2 + self._y ** 2) ** 0.5

    def __lt__(self, other):
        return self.length() < other.length()

    def __le__(self, other):
        return self.length() <= other.length()

    def __gt__(self, other):
        return self.length() > other.length()

    def __ge__(self, other):
        return self.length() >= other.length()

    def __eq__(self, other):
        return self.length() == other.length()

    def __ne__(self, other):
        return self.length() != other.length()


# -------------------------------------------------------------------------

if __name__ == '__main__':

    v1 = Vector(3, 4)
    v2 = Vector(-1, 1)

    print(f'v1 = {v1}')
    print(f'v2 = {v2}')

    v3 = v1 + v2

    print(v1)

    print(f'v1 + v2 = {v3}')

    print(f'length = {v3.length()}')

    if v1 > v2:
        print('v1 is longer')
    elif v2 > v1:
        print('v2 is longer')
    else:
        print('v1 and v2 are equal')