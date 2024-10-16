
class BankAccount:

    def __init__(self, account_number, holder, balance = 0.0):
        self._account_number = account_number
        self._holder = holder
        self._balance = balance

    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

    def __str__(self):
        return f'Account {self._account_number} belongs to {self._holder} has a balance of €{self._balance:.2f}'


class SavingsAccount(BankAccount):

    def __init__(self, account_number, holder, balance = 0.0, interest = 0.1):
        super().__init__(account_number, holder, balance)
        self._interest = interest

    def __str__(self):
        return f'SavingsAccount {self._account_number} belongs to {self._holder} has a balance of €{self._balance:.2f}. Interest {self._interest}%'


# ------------------------------------------------------------------------

acc1 = BankAccount('NL99ABCD0987623451', 'Peter')
acc2 = BankAccount('NL99ABCD0987664787', 'Toby', 100)
acc3 = SavingsAccount('NL99ABCD0987612376', 'Niels', 200, 5)

accounts = []
accounts.append(acc1)
accounts.append(acc2)
accounts.append(acc3)

print( acc1 )
print( acc2 )
print( acc3 )

acc1.deposit(3000)
acc2.deposit(3000)
acc3.deposit(3000)

acc1.withdraw(300)
acc1.withdraw(24)
acc1.withdraw(230)

acc2.withdraw(10)
acc2.withdraw(400)
acc2.deposit(-230)

acc3.withdraw(1500)
acc3.withdraw(1800)
acc3.deposit(230)

for acc in accounts:
    print( acc )

