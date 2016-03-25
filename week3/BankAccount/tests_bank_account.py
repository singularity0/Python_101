import unittest
from bank_account import BankAccount


class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.initial_balance = 1000
        self.rado = BankAccount("Rado", self.initial_balance, "BGN")

    def test_bank_account_init(self):
        self.assertEqual(self.rado.name, "Rado")
        self.assertEqual(self.rado.balance(), 1000)
        self.assertEqual(self.rado.currency, 'BGN')
        self.assertEqual(
            self.rado.history(), ['Account was created', 'Balance check -> 1000$'])
        self.assertGreater(self.rado.balance(), -1)

    def test_if_created_with_negative_balance(self):
        with self.assertRaises(ValueError):
            BankAccount("rado", -10, "USD")

    def test_deposit_working(self):
        old_deposit = self.rado.balance()
        sum_to_add = 100
        self.rado.deposit(sum_to_add)
        new_deposit = self.rado.balance()
        self.assertEqual(new_deposit, old_deposit + sum_to_add)

    def test_witdrawal_possible_withnegative_ammount(self):
        self.assertFalse(self.rado.withdraw(200000))

    def test_trasfer_with_diff_currencies(self):
        self.raiko = BankAccount("Raiko", self.initial_balance, "USD")
        self.assertFalse(self.raiko.transfer_to(self.rado, 333))

    def test_history(self):
        self.rado.deposit(1000)
        self.rado.balance()
        self.rado.withdraw(500)
        self.assertEqual(self.rado.history(),
                         ['Account was created', 'Deposited 1000$', 'Balance check -> 2000$', '500$ was withdrawed'])

if __name__ == '__main__':
    unittest.main()
