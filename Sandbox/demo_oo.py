

class Person:

    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence):
        self.residence = new_residence

# ----------------------------------

p = Person('Peter', 'Lhee')

p.age = 54

print(p)
print(p.name, p.residence)

p.tell()
Person.tell(p)

p.move('Eindhoven')
Person.move(p, 'Amsterdam')
p.tell()
