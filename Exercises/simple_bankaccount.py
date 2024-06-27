class BankAccount:
    """This is my BankAccount class"""

    currency = '$'

    def __init__(self, number: str, holder: str, balance: int = 0):
        self._holder = holder
        self._number = number
        self._balance = balance
        self._history = []

    def __del__(self):
        print('This object is going to be collected by the garbage collector.')

    def __str__(self):
        return f'Bankaccount with number {self._number}.'

    def __repr__(self):
        return f'Bankaccount("{self._number}", "{self._holder}", {self._balance})'


    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number.upper()

    @number.setter
    def number(self, value):
        if len(value) == 18:
            self._number = value
        else:
            raise Exception('Invalid account number!')

    def withdraw(self, amount: int):
        self._balance -= amount
        self._history.append(f'Withdraw of {BankAccount.currency}{amount}')

    def deposit(self, amount: int):
        self._balance += amount
        self._history.append(f'Deposit of {BankAccount.currency}{amount}')

    def info(self):
        return f'BankAccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'



class Logging:
    def __init__(self):
        self._history = []
    def log(self, description):
        self._history.append(description)
    def show(self):
        print('History')
        print(self._history)


class SavingsAccount(BankAccount, Logging):
    def __init__(self, number: str, holder: str, balance: int = 0, interest_rate=0.5):
        BankAccount.__init__(number, holder, balance)
        Logging.__init__(self)
        self._interest_rate = interest_rate

    def info(self):
        return f'SavingsAccount with number {self._number} belongs to {self._holder} has a balance of {BankAccount.currency}{self._balance}.'

    def add_interest(self):
        self._balance += self._interest_rate / 100 * self._balance

class BirthdayAccount(SavingsAccount):
    pass

# -------------------------------------------------

acc1 = BankAccount('NL99ABCD0121234658', 'Peter')

print(acc1.info())

acc1.deposit(1000)
acc1.withdraw(231)
acc1.withdraw(20)
acc1.withdraw(100)

print(acc1.info())

print(acc1.number)

print(acc1.info())

print(str(acc1))
print(repr(acc1))

del acc1

acc2 = SavingsAccount("NL99ABCD0121234658", "Peter", 649, interest_rate=2.0)
print(str(acc2))
print(acc2.info())

acc2.add_interest()

print(acc2.info())

# print(acc2.show())
