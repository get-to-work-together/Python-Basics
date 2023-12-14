class Person:
    """
    This is a class representing a Person

    Written by Peter
    Date 2021-06-02

    Parent class of Customer

    History:
    First version - 2021-06-02 - Peter Anema
    """

    # class-wide attribute
    MAXIMUM_AGE = 110

    def __init__(self, name, residence = 'unknown'):
        self._lastname = name
        self._residence = residence

    def tell(self):
        """
        Print a nice story about yourself
        """
        print(f'My name is {self._lastname} and I live in {self._residence}')

    def move(self, new_residence):
        """
        Change residence to a new residence
        """
        self._residence = new_residence

    def get_name(self):
        """
        Getter for name
        """
        return self._lastname

class Customer(Person):

    def __init__(self, name, residence = 'unknown', customernumber='0000000'):
        super().__init__(name, residence)
        self._customernumber = customernumber

# =====================================================

p1 = Person('Peter')
p1.tell()

p2 = Person('Martin', 'Eindhoven')
p2.tell()

p1.move('Utrecht')
p1.tell()

Person.MAXIMUM_AGE = 120
print(Person.MAXIMUM_AGE)

c1 = Customer('Mariana', 'Eindhoven')
c1.tell()


