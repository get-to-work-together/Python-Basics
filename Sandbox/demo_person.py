
class Person:

    __slots__ = ('name', 'residence')

    def __init__(self, name, residence = 'unknown'):
        self.name = name
        self.residence = residence

    def __str__(self):
        return f'I am {self.name}. I am a Person.'

    def __repr__(self):
        return f'Person()'

    def tell(self):
        return f'I am {self.name} and I live in {self.residence}'

    def move(self, new_residence):
        self.residence = new_residence

class Student(Person):

    def __init__(self, name, residence, school):
        super().__init__(name, residence)
        self.school = school

    def tell(self):
        return f'I am {self.name}. I am a student at {self.school} and live in {self.residence}'


# -------------------------------

# Instantiation - creating an object
p1 = Person('Peter', 'Lhee')

p2 = Person('Ying Hsuan')

print(p1.tell())
print(Person.tell(p1))

print(p2.tell())

#
#
# p1.move('Eindhoven')
# print(p1.tell())

print(p1)
print(str(p1))

student1 = Student('Jaenette', 'Veldhoven', 'TU Eindhoven')
print(student1.tell())
student1.move('Amsterdam')
print(student1.tell())