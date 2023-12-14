class Car:

    def __init__(self, make, model, color, mileage = 0):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

    def info(self):
        return f'This great {self.color} {self.make} {self.model} as driven {self.mileage}km.'

    def drive(self, km):
        self.mileage += km
        print(f'Driving {km}km.')


# -------------------------------------------------------

if __name__ == '__main__':

    my_car = Car('Renault', 'Megane', 'metalic brown')
    my_car.drive(200)
    my_car.drive(300)
    print(my_car.info())

