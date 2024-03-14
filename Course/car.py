class Car:

    unit = 'miles'   # class wide attribute

    # __slots__ = ['_make', '_model', '_color', '_mileage', '_number_of_seats']

    def __init__(self, make, model, color, mileage = 0, number_of_seats = 4):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage
        self._number_of_seats = number_of_seats

    def __repr__(self):
        return f'Car({self._make}, {self._model}, {self._color}, {self._mileage})'

    def __str__(self):
        return f'make: {self._make} model: {self._model} color: {self._color} mileage: {self._mileage}'

    def __add__(self, other):
        return self._mileage + other._mileage

    def __eq__(self, other):
        return self._mileage == other._mileage
    def __ne__(self, other):
        return self._mileage != other._mileage
    def __lt__(self, other):
        return self._mileage < other._mileage
    def __le__(self, other):
        return self._mileage <= other._mileage
    def __gt__(self, other):
        return self._mileage > other._mileage
    def __ge__(self, other):
        return self._mileage >= other._mileage

    def info(self):
        print( f'This great {self._color} {self._make} {self._model} as driven {self._mileage} {self.unit}.' )

    def drive(self, distance):
        self._mileage += distance
        print(f'Driving {distance} {self.unit}.')

    @classmethod
    def change_unit(cls, new_unit):
        cls.unit = new_unit

    @staticmethod
    def create_instance():
        make = input('Make? : ')
        model = input('Model? : ')
        color = input('Color? : ')
        mileage = int(input('Mileage? : '))

        car = Car(make, model, color, mileage)

        return car


# ---------------------------------------------

if __name__ == '__main__':

    Car.change_unit('mls')

    my_car = Car('Renault', 'Megane', 'metalic brown', 451000)
    # my_car = Car.create_instance()

    my_car.drive(250)

    my_car.info()

    print(str(my_car))
    print(repr(my_car))

    your_car = Car('VW', 'beetle', 'white', 123450)

    print(my_car > your_car)
