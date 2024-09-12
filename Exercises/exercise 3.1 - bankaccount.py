class BankAccount:

    def __init__(self, number, holder, balance = 0):
        self._number = number
        self._holder = holder
        self._balance = balance

    def withdraw(self, amount):
        self._balance -= amount

    def deposit(self, amount):
        self._balance += amount

    def get_info(self):
        return f'Bankaccount with number {self._number} belongs to {self._holder} has a balance of €{self._balance}.'


# ---------------------------------------------------------

if __name__ == '__main__':

    acc1 = BankAccount('NL23ABCD0345673456', 'Peter')
    acc2 = BankAccount('NL12ABCD9283740029', 'Guido', balance = 1000)

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
