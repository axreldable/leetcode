import unittest
from random import randint

from hacker_runk.akvelon_test_1 import getMaxArray, getMaxArray_naive


class TestMaxDotProduct(unittest.TestCase):
    def test_small(self):
        for (arr, answer) in [
            ([2, 2, 3, 4, 0, 1, 2, 0], [5, 1]),
            ([2, 2, 3, 4, 0, 1, 2, 0], [5, 1]),
        ]:
            self.assertEqual(getMaxArray(arr), answer)

    def test_vs_naive(self):
        for n in (10, 20):
            for max_value in (1, 2, 10, 10 ** 5):
                arr = [randint(0, max_value) for _ in range(n)]
                print(arr)
                left = getMaxArray_naive(arr)
                right = getMaxArray(arr)
                self.assertEqual(left, right)

    def test_speed(self):
        for n in (10, 20):
            for max_value in (1, 2, 10, 10 ** 5):
                arr = [randint(0, max_value) for _ in range(n)]
                print(getMaxArray(arr))


if __name__ == '__main__':
    unittest.main()
