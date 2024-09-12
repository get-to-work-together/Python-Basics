
class Person:

    # initializing attributes
    def __init__(self, name, residence):
        self.name = name
        self.residence = residence

    # methods
    def tell(self):
        print(f'I am {self.name} and I live in {self.residence}')

    def move(self, new_residence):
        self.residence = new_residence


class Customer(Person):

    # initializing attributes
    def __init__(self, name, customernr):
        super().__init__(name, 'unknown')
        self.customernr = customernr

    #overriding
    def tell(self):
        print(f'I am customer {self.name}. My number is {self.customernr}')


# -------------------------------------------------------

# instantiation
p1 = Person('Peter', 'Amsterdam')
p2 = Person('Kim', 'Delft')

cust1 = Customer('Saskia', 'VIP3457')

# call method
p1.tell()
p2.tell()

p1.move('Eindhoven')

p1.tell()
p2.tell()

cust1.tell()

cust1.log('Started')

