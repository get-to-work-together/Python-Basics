
class Person:

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence



# ----------------------------


p1 = Person('Peter')
p2 = Person('Katsia', 'Eindhoven')

p1.tell()
p2.tell()

p1.move('Eindhoven')

p1.tell()
# Person.tell(p1)

