
class Person:

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence


# --------------------------------------------------

p = Person('Peter', 'Lhee')        # instantiation
t = Person('Kim')        # instantiation

p.tell()
t.tell()

p.move('Eindhoven')

p.tell()
