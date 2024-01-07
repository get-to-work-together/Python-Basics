import unittest
from bankaccount import BankAccount


class BankAccountTests(unittest.TestCase):

    def test_instantiation(self):
        acc1 = BankAccount('NR08867537', 'HOLDER', balance=10)
        self.assertEquals(10, acc1.balance)

    def test_deposit(self):
        acc1 = BankAccount('NR08867537', 'HOLDER', balance=10)
        acc1.deposit(123)
        self.assertEquals(133, acc1.balance)

    def test_withdraw(self):
        acc1 = BankAccount('NR08867537', 'HOLDER', balance=10)
        acc1.withdraw(100)
        self.assertEquals(-90, acc1.balance)


if __name__ == '__main__':

    unittest.main()