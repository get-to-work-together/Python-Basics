class Car:
    """Simulates a car.

    Many useful methods"""

    def __init__(self, make, model, color, mileage=0):
        """My initialization function

        @param make - Make of the car. E.g. Porsche
        @param model - Model. e.g. 911"""

        self._make = make # ignored
        self._model = model
        self._color = color
        self._mileage = mileage

    def __str__(self):
        """"""
        return f'{self._color} {self._make} {self._model} mileage: {self._mileage}km.'

    def __repr__(self):
        return f"Car('{self._make}', '{self._model}', '{self._color}')"

    def info(self):
        print(f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.')

    def drive(self, km):
        self._mileage += km
        print(f'Driving {km}km.')


# -----------------------------

if __name__ == '__main__':
    car = Car('Porsche', '911', 'Red')
    car.drive(200)
    car.info()