#Author: Esther
# test_tax_calculator.py

import unittest
from tax_calculator import calculate_tax

class TestTaxCalculator(unittest.TestCase):
    def test_no_tax_below_12000(self):
        self.assertEqual(calculate_tax(10000), 0)

    def test_20_percent_tax_between_12000_and_36000(self):
        self.assertEqual(calculate_tax(15000), 600)  # 20% of (15000 - 12000)

    def test_40_percent_tax_above_36000(self):
        self.assertEqual(calculate_tax(40000), 6400)  # 40% of (40000 - 36000) + 20% of (36000 - 12000)

    


if __name__ == '__main__':
    unittest.main()
