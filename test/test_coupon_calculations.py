import unittest
from store import coupon_calculations as coupon


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(2.12, coupon.calculate_price(.99, 5, 10), 2)
        self.assertAlmostEqual(6.84, coupon.calculate_price(5.99, 5, 15), 2)
        self.assertAlmostEqual(10.18, coupon.calculate_price(9.99, 5, 20), 2)
        self.assertAlmostEqual(2.12, coupon.calculate_price(5.99, 10, 10), 2)
        self.assertAlmostEqual(1.45, coupon.calculate_price(5, 10, 15), 2)
        self.assertAlmostEqual(2.57, coupon.calculate_price(6.01, 10, 20), 2)

    def test_price_under_between_ten_thirty(self):
        self.assertAlmostEqual(10.72, coupon.calculate_price(10, 5, 10), 2)
        self.assertAlmostEqual(11.89, coupon.calculate_price(11.59, 5, 15), 2)
        self.assertAlmostEqual(19.47, coupon.calculate_price(18.59, 5, 20), 2)
        self.assertAlmostEqual(22.68, coupon.calculate_price(25.44, 10, 10), 2)
        self.assertAlmostEqual(27.45, coupon.calculate_price(25.44, 5, 10), 2)

    def test_price_under_between_thirty_fifty(self):
        self.assertAlmostEqual(29.15, coupon.calculate_price(30, 5, 20), 2)
        self.assertAlmostEqual(34.98, coupon.calculate_price(33.33, 5, 10), 2)
        self.assertAlmostEqual(35.93, coupon.calculate_price(41.05, 10, 15), 2)
        self.assertAlmostEqual(48.82, coupon.calculate_price(48.65, 10, 10), 2)
        self.assertAlmostEqual(45.86, coupon.calculate_price(49.99, 10, 20), 2)

    def test_price_under_over_fifty(self):
        self.assertAlmostEqual(54.88, coupon.calculate_price(50, 5, 10), 2)
        self.assertAlmostEqual(58.26, coupon.calculate_price(58.54, 10, 10), 2)
        self.assertAlmostEqual(61.92, coupon.calculate_price(78.72,10, 15), 2)
        self.assertAlmostEqual(76.25, coupon.calculate_price(99.92, 10, 20), 2)
        self.assertAlmostEqual(133.34, coupon.calculate_price(157.99, 10, 15), 2)


if __name__ == '__main__':
    unittest.main()
