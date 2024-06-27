class BankAccount:

    # class wide attribute
    __slots__ = ['_holder', '_number', '_balance']
    last_number = 875346
    currency = '$'

    def __init__(self, number=None, holder=None, balance = 0):
        BankAccount.last_number += 1
        self._holder = holder
        if number:
            self._number = number
        else:
            self._number = BankAccount.last_number
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'

    @staticmethod
    def change_currency(new_currency):
        BankAccount.currency = new_currency

    @classmethod
    def change_currency(cls, new_currency):
        cls.currency = new_currency

# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount(holder = 'Peter')
    acc2 = BankAccount(holder = 'Guido', balance = 1000)

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
