import unittest
import stringcalculator


class TestStringMethods(unittest.TestCase):

    def test_zero_args(self):
        self.assertEqual(stringcalculator.Add(""), 0)

    def test_one_args(self):
        self.assertEqual(stringcalculator.Add("1"), int(1))

    def test_two_args(self):
        self.assertEqual(stringcalculator.Add("2,3"), int(5))


if __name__ == '__main__':
    unittest.main()
