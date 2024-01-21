
class Person(object):

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def __repr__(self):
        return f'Person("{self._name}", "{self._residence}")'

    def __str__(self):
        return f'Person: {self._name} with residence {self._residence}'
        
    def tell(self):
        print(f'I am {self._name} and I live in {self._residence}.')

    def move(self, new_residence):
        self._residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customer_number):
        super().__init__(name, residence)
        self._customer_number = customer_number

    def tell(self):
        print(f'I am a customer and my name is {self._name}. Nr {self._customer_number}')
        


# -------------------------------

p1 = Person('Peter', 'Lhee')

p1.tell()
p1.move('Eindhoven')
p1.tell()

print(str(p1))
print(repr(p1))

print(p1)

cust1 = Customer('Aneesh', 'Lhee', 'VIP000450')
cust1.tell()
