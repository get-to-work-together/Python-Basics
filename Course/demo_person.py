
class Person(object):

    def __init__(self, name, residence):
        self._name = name
        self._residence = residence

    def tell(self):
        return f'I am {self._name} and I live in {self._residence}'

    def move(self, new_residence):
        self._residence = new_residence


from dataclasses import dataclass

@dataclass
class Person:
    _name: str
    _residence: str

    def tell(self):
        return f'I am {self._name} and I live in {self._residence}'

    def move(self, new_residence):
        self._residence = new_residence


class Customer(Person):

    def __init__(self, name, residence, customernr):
        super().__init__(name, residence)
        self._customernr = customernr

    def tell(self):
        return f'I am a customer [{self._customernr}] and my name is {self._name} and I live in {self._residence}'



# --------------------------------------------------

if __name__ == '__main__':

    p1 = Person('Peter', 'Lhee')
    p2 = Customer('Dennis', 'Roosendaal', 'VIP98798798')

    print( p1.tell() )
    print( p2.tell() )

    p2.move('Eindhoven')

    print( p2.tell() )

    print( Person.tell(p2) )
