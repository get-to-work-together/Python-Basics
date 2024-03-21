
class BankAccount:

    def __init__(self, holder, accountnr, balance):
        self.holder = holder
        self.accountnr = accountnr
        self.balance = balance

    def info(self):
        return f'Account {self.accountnr} belongs to {self.holder} and has a balance of $ {self.balance}.'

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount


# -----------------------------------------------------

acc1 = BankAccount('Peter', 'NL83ABCD098709809', 100)

print( acc1.info() )

acc1.deposit(200)
acc1.withdraw(24)
acc1.withdraw(98)

print( acc1.info() )
