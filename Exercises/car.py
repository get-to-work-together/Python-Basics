class Car:

    def calculate_amount_of_gas(self, number_of_kilometers):
        return number_of_kilometers / self._kml

    def __init__(self, make, model, color, mileage = 0, kml = None):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage
        self._started = False
        self._kml = kml
        self._tank = 0

    def info(self):
        print( f'This great {self._color} {self._make} {self._model} as driven {self._mileage}km.' )
        if self._started:
            print( f'The engine is still running.')

    def __str__(self):
        return f'{self._color} {self._make} {self._model} mileage: {self._mileage}km. Tank {self._tank:.1f}l.'

    def __repr__(self):
        return f"Car('{self._make}', '{self._model}', '{self._color}')"

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

    def __add__(self, other):
        return self._mileage + other._mileage


    def drive(self, km):
        if self._started:
            self._mileage += km
            print(f'Driving {km}km.')
            if self._kml is not None:
                amount_gas = self.calculate_amount_of_gas(km)
                self._tank -= amount_gas
                print(f'On this drive you used {amount_gas:.1f} liters of gas.')

        else:
            print('Please start your car first.')

    def fill_up(self):
        self._tank = 60

    def start(self):
        self._started = True

    def stop(self):
        self._started = False

    def __del__(self):
        print('The car has been demolished. Too bad.')


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown', kml=21)
    my_car.fill_up()

    my_car.start()
    my_car.drive(200)
    my_car.drive(300)

    my_car.info()
    print(my_car)

    del my_car

