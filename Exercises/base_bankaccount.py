
class BankAccount(object):

    __slots__ = ('_holder', '_number', '_balance')

    currency = '€'

    def __init__(self, holder, number, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def info(self):
        return f'BankAccount with number {self._number}'\
               f' belongs to {self._holder}'\
               f' has a balance of {BankAccount.currency}{self._balance}.'

    @classmethod
    def change_currency(cls, new_currency):
        cls.currency = new_currency



class SavingsAccount(BankAccount):

    def __init__(self, holder, number, balance = 0, interest = 0):
        super().__init__(self, holder, number, balance)
        self._interest = interest

    def info(self):
        return f'SavingsAccount with number {self._number}'\
               f' belongs to {self._holder}'\
               f' has a balance of {SavingsAccount.currency}{self._balance}.'\
               f' Interest rate = {self._interest}%'

    def add_interest(self, years):
        self._balance *= self._balance * self._interest / 100 * years
        
    @staticmethod
    def calculate_interest(amount, interest):
        return amount + amount * interest / 100


# -------------------------------------------------

acc1 = SavingsAccount('Peter', 'NL99ABCD0121234658', interest = 2.8)

BankAccount.change_currency('$')

print(acc1.info())

acc1.deposit(1000)
acc1.withdraw(231)
acc1.withdraw(20)
acc1.withdraw(100)

print(acc1.info())

acc1.add_interest(2)

print(acc1.info())


