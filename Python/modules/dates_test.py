import unittest
import datetime
import dates


class MyTestCase(unittest.TestCase):
    def test_calculate_dt(self):
        self.assertEqual(datetime.date(2016, 5, 4), dates.calculate_dt("2016 4 20", "14"))
        self.assertEqual(datetime.date(2016, 2, 29), dates.calculate_dt("2016 2 20", "9"))

    def test_format_date(self):
        self.assertEqual("2016 4 20", dates.format_date(datetime.date(2016, 4, 20)))

    def test_calculate(self):
        self.assertEqual("2016 5 4", dates.calculate("2016 4 20", "14"))
        self.assertEqual("2016 2 29", dates.calculate("2016 2 20", "9"))
        self.assertEqual("2016 1 1", dates.calculate("2015 12 31", "1"))


if __name__ == '__main__':
    unittest.main()
