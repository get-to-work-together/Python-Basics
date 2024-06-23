
class BankAccount(object):
    """Simple BankAccount class"""

    currency = '€'

    def __init__(self, holder, number, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            raise Exception('Not enough credit!')

    def deposit(self, amount):
        self._balance += amount

    def info(self):
        return f'BankAccount with number {self._number}'\
               f' belongs to {self._holder}'\
               f' and has a balance of {BankAccount.currency}{self._balance}.'


class SavingsAccount(BankAccount):

    def __init__(self, holder, number, balance = 0, interest = 10):
        super().__init__(holder, number, balance)
        self._interest = interest

    def info(self):
        return f'SavingsAccount with number {self._number}'\
               f' belongs to {self._holder}'\
               f' and has a balance of €{self._balance:.2f}.'

    def add_interest(self):
        self._balance += (self._interest / 100) * self._balance


# -------------------------------------------------

if __name__ == '__main__':

    acc1 = SavingsAccount('Peter', 'NL99ABCD0121234658')

    print(acc1.info())

    acc1.deposit(1000)
    acc1.withdraw(231)
    acc1.withdraw(20)
    acc1.withdraw(100)

    acc1.add_interest()
    acc1.add_interest()
    acc1.add_interest()
    acc1.add_interest()

    print(acc1.info())


