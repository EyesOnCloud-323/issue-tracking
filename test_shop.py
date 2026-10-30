import unittest

from shop import add_tax, apply_discount, total

class TestShop(unittest.TestCase):
    def test_add_tax(self):
        self.assertEqual(add_tax(100, 18), 118.0)

    def test_total(self):
        self.assertEqual(total([10, 20, 30]), 60)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(50, 10), 45)

if __name__ == "__main__":
    unittest.main()

