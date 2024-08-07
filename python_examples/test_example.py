from unittest import TestCase
import example

class SimpleTest(TestCase):
    def test_hello_is_equal_to_hello(self):
        self.assertEqual("hsfdello", "hello")

    def test_hello_hello_wrong(self):
        self.assertEqual("hello", "asd")

    def test_hello_bye(self):
        self.assertNotEqual("hello", "bye")








class Floattest(TestCase):
    def test_floats(self):
        self.assertAlmostEqual(0.234234235, 0.23, 6)










class MoneyFunctionTest(TestCase):
    def test_interest_gets_added(self):
        initial_money = 100
        money_after_10_years = example.calculate_bank_account_value(initial_money, 0.03, 1)

        import numpy as np

        np.array([1, 2, 3, 4])

        np.max()

        self.assertAlmostEqual(money_after_10_years, 103)


    def test_interest_on_interest(self):
        initial_money = 100
        money_after_2_years = example.calculate_bank_account_value(initial_money, 0.03, 2)
        self.assertAlmostEqual(money_after_2_years, 106.09)



    def test_money_doubles(self):
        initial_money = 100
        money_after_10_years = example.calculate_bank_account_value(initial_money, 0.03, 10)
        self.assertAlmostEqual(money_after_10_years, 200)