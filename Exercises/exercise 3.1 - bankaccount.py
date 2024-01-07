class BankAccount:

    def __init__(self, number, holder, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value > 0:
            self._balance = value

    def withdraw(self, amount):
        self._balance -= amount
        print(f'Withdraw of €{amount}')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of €{amount}')

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of €{self._balance}.'


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
    acc2 = BankAccount('NL01ABCD0234567777', 'Guido', balance = 1000)

    print(acc1.get_info())
    print(acc2.get_info())

    acc1.deposit(1000)
    acc1.withdraw(100)
    acc1.withdraw(22)

    acc2.deposit(10000)
    acc2.withdraw(1090)
    acc2.withdraw(220)

    print(acc1.get_info())
    print(acc2.get_info())

    print( acc1.balance )
    acc1.balance = 1000000

    print(acc1.get_info())
