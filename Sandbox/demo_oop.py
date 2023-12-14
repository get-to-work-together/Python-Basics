
class Person:

    def __init__(self, name, residence = 'unknown'):
        self._name = name
        self._residence = residence

    def __repr__(self):
        return f'This is a Person object.'

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')

    def relocate(self, new_residence):
        print(f'Moving to {new_residence}')
        self._residence = new_residence


# ==================

p1 = Person('Peter', 'Lhee')
p2 = Person('Yuliyan')

p1.tell()

p1.relocate('Eindhoven')

p1.tell()

print(p1)

p2.tell()
