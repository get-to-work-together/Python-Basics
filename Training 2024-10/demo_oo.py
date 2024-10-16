
class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence

# ------------------------------

# Instantiation
p = Person('Peter', 'Lhee')

# Methodes
p.tell()
p.move('Eindhoven')
p.tell()
