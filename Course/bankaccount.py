
class BankAccount(object):

    def __init__(self, holder, accountnumber, balance = 0):
        self._holder = holder
        self._number = accountnumber
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print('Not enough funds!!!')

    def info(self) -> str:
        print(f'Account {self._number} belongs to {self._holder} and has a balance of {self._balance}.')


class LogClass:
    def bell(self):
        print('BELLL!!!!')


class SavingsAccount(BankAccount, LogClass):

    def __init__(self, holder, accountnumber, balance = 0, interest = 10):
        super().__init__(holder, accountnumber, balance)
        self._interest = interest

    def add_interest(self):
        self._balance += self._balance * self._interest / 100

    def info(self) -> int:
        print(f'SavingsAccount {self._number} belongs to {self._holder} and has a balance of {self._balance}.')


# --------------------------------------------------------------------------

if __name__ == '__main__':

    acc1 = SavingsAccount('Peter', 'NL44ABCD0647586098', interest = 4)

    acc1.deposit(1200)
    acc1.withdraw(120)
    acc1.withdraw(12)
    acc1.withdraw(12)

    acc1.add_interest()

    acc1.info()
