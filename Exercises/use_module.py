from bankaccount import BankAccount

acc1 = BankAccount('NL01ABCD0234567890', 'Peter')
acc2 = BankAccount('NL01ABCD0234567777', 'Guido')

print(acc1.get_info())
print(acc2.get_info())

acc1.deposit(1000)
acc1.withdraw(100)
acc1.withdraw(22)

acc1.transfer(acc2, 22)

print(acc1.get_info())
print(acc2.get_info())
