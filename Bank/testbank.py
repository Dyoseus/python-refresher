import unittest
import bank


class TestBank(unittest.TestCase):
    

    def testwithdraw(self):
        b1 = bank.BankAccount("Albert", 1234567890, 57305)
        self.assertEqual(b1.withdrawwithdraw(5), 57300)

    def testdeposit(self):
        b1 = bank.BankAccount("Albert", 1234567890, 57305)
        self.assertEqual(b1.deposit(10), 57315)


if __name__ == "__main__":
    unittest.main()
