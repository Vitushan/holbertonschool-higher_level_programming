#!/usr/bin/python3
"""
Test cases pour le module 6-max_integer
"""

import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests pour la fonction max_integer"""

    def test_positive_numbers(self):
        """Test avec des nombres positifs"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_negative_numbers(self):
        """Test avec des nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test avec des nombres mélangés (positifs et négatifs)"""
        self.assertEqual(max_integer([-10, 10, 5, -5]), 10)

    def test_single_element(self):
        """Test avec une liste à un seul élément"""
        self.assertEqual(max_integer([42]), 42)

    def test_empty_list(self):
        """Test avec une liste vide"""
        self.assertIsNone(max_integer([]))

    def test_float_numbers(self):
        """Test avec des nombres à virgule flottante"""
        self.assertEqual(max_integer([1.5, 2.7, 0.2]), 2.7)

if __name__ == '__main__':
    unittest.main()
