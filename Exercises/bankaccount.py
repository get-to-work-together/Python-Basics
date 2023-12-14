class BankAccount:
    """This is my BankAccount class"""

    currency = '€'
    __slots__ = ('_number', '_holder', '_balance')

    def __init__(self, number, holder, balance=0):
        self._holder = holder
        self._number = number
        self._balance = balance

    @classmethod
    def set_currency(cls, new_currency):
        cls.currency = new_currency

    @staticmethod
    def calculate_sum(amount1, amount2):
        return amount1 + amount2

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value

    def withdraw(self, amount):
        self._balance -= amount
        print(f'Withdraw of {BankAccount.currency}{amount}')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of {BankAccount.currency}{amount}')

    def transfer(self, other, amount):
        self.withdraw(amount)
        other.deposit(amount)
        print(f'Transfer of {BankAccount.currency}{amount}')

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'

    @property
    def info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'

class Logging:
    def __init__(self):
        print('init')
    def log(self):
        print('logging')
    def deposit(self, amount):
        print('deposit log')


class SavingsAccount(BankAccount, Logging):
    def __init__(self, number, holder, balance = 0, interest = 0):
        BankAccount.__init__(self, number, holder, balance)
        Logging.__init__(self)
        self._interest = interest
        self.log()

    def get_info(self):
        return f'Savingsaccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}. Interest {self._interest}'


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
    acc2 = BankAccount('NL01ABCD0234567777', 'Guido')

    print(acc1.get_info())
    print(acc2.get_info())

    print(acc1.balance)
    acc1.balance = 1000000
    print(acc1.balance)

    BankAccount.set_currency('$')

    amount = BankAccount.calculate_sum(201, 298)
    acc1.deposit(amount)

    acc1.deposit(1000)
    acc1.withdraw(100)
    acc1.withdraw(22)

    acc1.transfer(acc2, 22)

    print(acc1.get_info())
    print(acc2.get_info())

    print(acc2.info)

    acc3 = SavingsAccount('SAVING123', 'Peter', interest = 10)
    acc3.deposit(1000)
    print(acc3.info)
    print(acc3.get_info())