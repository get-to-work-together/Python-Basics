class Car:

    DISTANCE_UNITS = 'km'
    VOLUME_UNIT = 'l'
    number_of_cars = 0

    def __init__(self, make, model, color, mileage = 0, usage = None):
        self._make = make
        self._model = model
        self._color = color
        self._mileage = mileage
        self._started = False
        self._usage = usage         # mpg or kmpl
        self._tank = 0
        Car.number_of_cars += 1

    def __del__(self):
        print('Your car has been demolished.')
        Car.number_of_cars -= 1

    def __str__(self):
        return f'{self._color} {self._make} {self._model} mileage: {self._mileage}{Car.DISTANCE_UNITS}. Tank {self._tank:.1f}{Car.VOLUME_UNIT}.'

    def __repr__(self):
        return f"Car('{self._make}', '{self._model}', '{self._color}')"

    def info(self):
        print( f'This great {self._color} {self._make} {self._model} as driven {self._mileage}{Car.DISTANCE_UNITS}.' )
        if self._started:
            print( f'The engine is still running.')

    def drive(self, km):
        if self._started:
            self._mileage += km
            print(f'Driving {km}{Car.DISTANCE_UNITS}.')
            if self._usage is not None:
                amount_gas = self.calculate_amount_of_gas(km)
                self._tank -= amount_gas
                print(f'On this drive you used {amount_gas:.1f} {Car.VOLUME_UNIT} of gasoline.')

        else:
            print('Please start your car first.')

    def calculate_amount_of_gas(self, number_of_kilometers):
        return number_of_kilometers / self._usage

    def fill_up(self):
        self._tank = 60

    def start(self):
        self._started = True

    def stop(self):
        self._started = False

    @staticmethod
    def get_number_of_cars():
        return Car.number_of_cars

    @classmethod
    def get_number_of_cars(cls):
        return cls.number_of_cars

# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown', mileage = 435000, usage = 21)
    my_car.fill_up()

    my_car.start()
    my_car.drive(200)
    my_car.drive(300)

    my_car.info()
    print(my_car)

    my_car = Car('Volkswagen', 'Kever', 'white', mileage = 100000, usage = 21)

    print( str(my_car) )
    print( repr(my_car) )

    your_car = Car('Volkswagen', 'Kever', 'white', mileage = 100000, usage = 21)

    print( Car.get_number_of_cars() )