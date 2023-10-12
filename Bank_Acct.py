class BankAccount:
    def __init__(self, opening_balance, rate, account_number, date_opening):
        self.balance = opening_balance
        self.rate = rate
        self.acct_number = account_number
        self.date_opn = date_opening

    def deposit(self, amount):
        try:
            self.balance += amount
        except TypeError:
            raise TypeError

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount

    @staticmethod
    def transfer(from_account, to_account, amount):
        from_account.withdraw(amount)
        to_account.deposit(amount)


import unittest


class BankAccountTests(unittest.TestCase):
    def testWithdrawal(self):

        self.account = BankAccount(18, 2, '19657867', '2023-05-31')
        self.account.withdraw(16)
        self.assertEqual(self.account.balance, 2)

    def testTransfer(self):

        account1 = BankAccount(20, 2, '19657867', '2023-05-31')
        account2 = BankAccount(10, 2, '19657888', '2023-01-31')
        self.account.transfer(account1, account2, 10)
        self.assertEqual(account1.balance, 10)
        self.assertEqual(account2.balance, 20)
