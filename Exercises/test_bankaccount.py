import unittest

from simple_bankaccount import BankAccount


class TestBankAccount(unittest.TestCase):

    def test_upper(self):
        actual = 'foo'.upper()
        expected = 'FOO'
        self.assertEqual(expected, actual)
        
    def test_balance(self):
        acc = BankAccount('123', 'Peter')
        self.assertEqual(0, acc.balance)
        acc.deposit(123)
        self.assertEqual(123, acc.balance)
        acc.withdraw(23)
        self.assertEqual(101, acc.balance)
        


if __name__ == '__main__':
    unittest.main()
