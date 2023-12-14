
class Glass:

    def __init__(self, volume):
        self.volume = volume
        self.contents = 'empty'
        self.amount_in_glass = 0

    def fill(self, beverage, amount):
        self.contents = beverage
        self.amount_in_glass = amount

    def drink(self, amount):
        self.amount_in_glass -= amount
        print(f"That's good {self.contents}")

    def empty(self):
        self.contents = 'empty'
        self.amount_in_glass = 0

    def status(self):
        if self.contents == 'empty':
            print(f'The glass is empty')
        else:
            print(f'The glass contains {self.amount_in_glass}ml of {self.contents}')

# ---------------------------------------------

g = Glass(200)
g.status()

g.fill('Cola', 180)
g.status()

g.drink(100)
g.status()

g.empty()
g.status()
