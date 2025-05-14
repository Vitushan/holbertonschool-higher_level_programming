#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_one_element(self):
        self.assertEqual(max_integer([7]), 7)
        self.assertEqual(max_integer([-3]), -3)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-10, -20, -30, -5]), -5)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 0, 2, -3]), 2)
        self.assertEqual(max_integer([0, 0, 0, 0]), 0)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 3.9, 2.1]), 3.9)
        self.assertEqual(max_integer([1, 2.5, 3, 2]), 3)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["abc", "def", "ghi"]), "ghi")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["abc", "ab", "a"]), "abc")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_no_argument(self):
        self.assertIsNone(max_integer())

if __name__ == '__main__':
    unittest.main()
