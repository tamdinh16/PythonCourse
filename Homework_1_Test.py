import unittest
import Homework_1

class Homework_1_Test(unittest.TestCase):
    
    def test_addCash(self):
        self.assertEqual(300.50, Homework_1.Portfolio.addCash(Homework_1, 300.50))

if __name__ == '__main__': 
  unittest.main()


# I only tested one function (addCash) and it did not work, so I stopped right there. However, I checked the solution file bit by bit, so I think the codes in the solution file is workable in some aspects.

# When I defined test_addCash(self), if I write:
#                                           self.assertEqual(300.50, self.Portfolio.addCash(300.50))
#                                     to mean that if I add 300.50 cash, it should show the number 300.50 and not something else.
# However, it does not work because it said that Homework_1_Test does not have the module Portfolio (which is strange because we already imported Homework_1 and the self function should be it. That is why the code at the top is with Homework_1.

# When I ran the code at the top, it said: "AttributeError: module 'Homework_1' has no attribute 'CashBalance'".
# That is strange because in the Homework_1 code itself: "self.CashBalance = self.CashBalance + amount", it should call in CashBalance.

# I also tried to put the CashBalance somwhere in the function. However, all did not work and I don't want to write them down all here.

# In conclusion, I tried to imitate your fizzbuzz.test, but your test works for a single function (Fizz(i)), so it is challenging for me to compare my test for the homework which involves class and a bunch of functions.

# Thank you.
