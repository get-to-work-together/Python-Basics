from car_module import Car

class Person:
    """This is my personal Person class"""

    def __init__(self, name):
        self._name = name
        self.cars = []

    def __repr__(self):
        return f'Person("{self._name}")'

    def __str__(self):
        return f'Person("{self._name}")'

    def info(self):
        """return a string wih info n this person object"""
        s =  f'Person {self._name}\n'
        for car in self.cars:
            s += str(car) + '\n'
        return s

    def buy_car(self, car):
        self.cars.append(car)

# ---------------

if __name__ == '__main__':

    p = Person('Peter')
    print(p)
    print(p.info())

    p.buy_car(Car('Audi', 'A2', 'black', 20000))
    print(p.info())
