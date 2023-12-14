class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def __del__(self):
        print('This car has been demolished.')

    def drive(self, km):
        self._mileage += km

    def __str__(self):
        return f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.' 

    def __repr__(self):
        return f'Car("{self._make}", "{self._model}", "{self._color}", mileage = {self._mileage})' 

# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault',
                 'Megane',
                 'metalic brown',
                 mileage = 428000)

    print(my_car)

    my_car.drive(242)
    my_car.drive(242)

    print(my_car)


