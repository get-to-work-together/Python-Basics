
class Person:

    def __init__(self, name, residence):
        self._name = name.capitalize()
        self._residence = residence

    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence


class Customer(Person):

    def tell(self):
        print(f'I am {self._name} and I am a customer.')



# -------------------------------

p1 = Person('Peter', 'Lhee')

p1.tell()
p1.move('Eindhoven')
p1.tell()


p2 = Customer('Joost', 'Eindhoven')
p2.tell()
