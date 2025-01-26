#!/usr/bin/python3
"""
Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer
class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_normal_case(self):
        """Test normal cases with positive integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_order(self):
        """Test list in reversed order"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test a list with a single element"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test an empty list"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test a list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test a list with positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_all_negative(self):
        """Test a list with all negative numbers"""
        self.assertEqual(max_integer([-5, -2, -3, -4]), -2)

    def test_floats(self):
        """Test a list with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 0.5]), 3.5)

    def test_mixed_int_and_float(self):
        """Test a list with both integers and floats"""
        self.assertEqual(max_integer([1, 2.5, 3, 4.5]), 4.5)

    def test_same_numbers(self):
        """Test a list with all the same numbers"""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()
