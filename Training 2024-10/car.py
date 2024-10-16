class Car:

    def __init__(self, make, model, color, mileage = 0):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage

    def drive(self, distance):
        self._mileage += distance

    def info(self) -> str:
        return f'This beautiful {self._color} {self._make} {self._model} has driven {self._mileage} miles.'

    def __repr__(self) -> str:
        return f'Car("{self._make}", "{self._model}", "{self._color}", {self._mileage})'

    def __str__(self) -> str:
        return f'Car: {self._color} {self._make} {self._model} - {self._mileage}'

    def __del__(self):
        print('Your car has been demolished')



# -------------------------------------

my_car = Car('Renault', 'Megan station', 'metalic brown', 475000)

print( my_car.info() )

my_car.drive(210)
my_car.drive(210)

print( my_car.info() )

print( str(my_car) )
print( repr(my_car) )
print( my_car )
