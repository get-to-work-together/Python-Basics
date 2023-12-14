

class Person:

    # initialize all attributes
    def __init__(self, name: str, residence: str):
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}.')

    def move(self, new_residence: str):
        self.residence = new_residence


# ----------------------------------------------

p1 = Person('Peter', 'Lhee')

print(type(p1))
print(p1.name)

p1.tell()

p1.move('Eindhoven')

p1.tell()



p2 = Person('Einstein', 'Harvard')

print(type(p2))
print(p2.name)
p2.tell()
