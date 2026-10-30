import unittest

from shop import apply_discount, total

class TestShop(unittest.TestCase):
    def test_total(self):
        self.assertEqual(total([10, 20, 30]), 60)

    def test_apply_discount(self):
        self.assertEqual(apply_discount(50, 10), 45)

if __name__ == "__main__":
    unittest.main()
