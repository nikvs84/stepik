import unittest
from multifilter import multifilter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_multifilter(self):
        def mul2(x):
            return x % 2 == 0

        def mul3(x):
            return x % 3 == 0

        def mul5(x):
            return x % 5 == 0

        a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

        self.assertListEqual([0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30],
                             list(multifilter(a, mul2, mul3, mul5)))

        self.assertListEqual([0, 6, 10, 12, 15, 18, 20, 24, 30],
                             list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))

        self.assertListEqual([0, 30], list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))


if __name__ == '__main__':
    unittest.main()
