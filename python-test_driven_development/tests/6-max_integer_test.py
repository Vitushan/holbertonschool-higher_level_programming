#!/usr/bin/python3
import unittest
from 6-max_integer import max_integer  # Assure-toi que cette ligne correspond au chemin du fichier contenant ta fonction

class TestMaxInteger(unittest.TestCase):
    """Unittest pour la fonction max_integer"""

    def test_normal_case(self):
        """Test avec une liste d'entiers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_reversed_order(self):
        """Test avec une liste d'entiers dans l'ordre inverse"""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_single_element(self):
        """Test avec une liste qui contient un seul élément"""
        self.assertEqual(max_integer([5]), 5)

    def test_empty_list(self):
        """Test avec une liste vide"""
        self.assertEqual(max_integer([]), None)

    def test_negative_numbers(self):
        """Test avec des nombres négatifs"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        """Test avec des nombres positifs et négatifs"""
        self.assertEqual(max_integer([-1, 2, 3, -4]), 3)

    def test_float_numbers(self):
        """Test avec des nombres à virgule flottante"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)

if __name__ == "__main__":
    unittest.main()
