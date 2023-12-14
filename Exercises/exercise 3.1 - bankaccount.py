class BankAccount:

    # classwide attribute
    __slots__ = ('_holder', '_number', '_balance')
    currency = '€'

    def __init__(self, number, holder, balance = 0):
        self._holder = holder
        self._number = number
        self._balance = balance

    def __str__(self):
        return f'Bankaccount: {self._number} - {self._holder}, balance = {BankAccount.currency}{self._balance}.'

    def __repr__(self):
        return f'Bankaccount("{self._number}", "{self._holder}", {self._balance})'

    def __eq__(self, other):
        return self._balance == other._balance

    def __ne__(self, other):
        return self._balance != other._balance

    def __gt__(self, other):
        return self._balance > other._balance

    def __ge__(self, other):
        return self._balance >= other._balance

    def __lt__(self, other):
        return self._balance < other._balance

    def __le__(self, other):
        return self._balance <= other._balance


    def withdraw(self, amount):
        self._balance -= amount
        print(f'Withdraw of €{amount}')

    def deposit(self, amount):
        self._balance += amount
        print(f'Deposit of €{amount}')

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'

    @classmethod
    def change_currency(cls, currency):
        cls.currency = currency

    @staticmethod
    def change_currency(currency):
        BankAccount.currency = currency


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
    acc2 = BankAccount('NL01ABCD0234567777', 'Guido', balance = 1000)

    print(repr(acc1))
    print(str(acc1))
    print(repr(acc2))
    print(str(acc2))

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

    print(acc1 > acc2)