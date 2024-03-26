
class BankAccount:

    currency = '$'

    def __init__(self, holder, accountnr, balance):
        self._holder = holder
        self._accountnr = accountnr
        self._balance = balance

    def info(self):
        return f'Account {self._accountnr} belongs to {self._holder} and has a balance of {BankAccount.currency} {self._balance}.'

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


class SavingsAccount(BankAccount):

    def info(self):
        return f'SavingsAccount!! {self._accountnr} belongs to {self._holder} and has a balance of {BankAccount.currency} {self._balance}.'


# -----------------------------------------------------

acc1 = BankAccount('Peter', 'NL83ABCD098709809', 100)

print( acc1.info() )

acc1.deposit(200)
acc1.withdraw(24)
acc1.withdraw(98)

print( acc1.info() )

acc2 = SavingsAccount('Ebrahim', 'NL83ABCD098777809', 10000)

print( acc2.info() )
