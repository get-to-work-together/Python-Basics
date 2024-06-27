class Person:

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def relocate(self, new_residence):
        self.residence = new_residence


# ------------------------------------

p1 = Person('Peter', 'Lhee')
p2 = Person('Jeroen')

p1.tell()
p2.tell()

p1.relocate('Eindhoven')

p1.tell()
