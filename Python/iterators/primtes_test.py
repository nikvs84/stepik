import itertools
import unittest
from primes import primes

class MyTestCase(unittest.TestCase):
    def test_generator(self):
        self.assertListEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31],
                             list(itertools.takewhile(lambda x : x <= 31, primes())))

    def test(self):
        self.assertListEqual([1, 2, 3, 4], list(i + 1 for i in range(4)))
        self.assertListEqual([1, 2, 3, 4], [i for i in range(5)][1:])
        self.assertListEqual([1, 2, 3, 4], [i + 1 for i in range(4)])


if __name__ == '__main__':
    unittest.main()
