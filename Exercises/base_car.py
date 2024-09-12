class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def drive(self, km):
        self._mileage += km

    def info(self):
        return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.'

    def __str__(self):
        return f'My {self._color} {self._make} {self._model} as driven {self._mileage}km.'

    def __repr__(self):
        return f'Car("{self._color}", "{self._make}", "{self._model}", {self._mileage})'






# from dataclasses import dataclass
#
# @dataclass
# class Car:
#
#     _make: str
#     _model: str
#     _color: str
#     _mileage: int = 0
#
#     def drive(self, km):
#         self._mileage += km
#
#     def info(self):
#         return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.'


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault',
                 'Megane',
                 'metalic brown',
                 466000)

    print(my_car.info())

    my_car.drive(242)
    my_car.drive(242)

    print(my_car.info())

    print(str(my_car))
    print(repr(my_car))

