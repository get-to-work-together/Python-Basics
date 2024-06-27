class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def info(self):
        return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.'

    def drive(self, km):
        self._mileage += km
        print(f'Driving {km}km.')


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown', 459600)
    my_car.drive(200)
    my_car.drive(300)
    print(my_car.info())

