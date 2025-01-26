�
    "v�g�  �                   �   � S r SS jrg)zZ
Module 0-add_integer
This module provides a function `add_integer`that adds two numbers.
c                 ��   � [        U [        [        45      (       d  [        S5      e[        U[        [        45      (       d  [        S5      e[        U 5      n [        U5      nX-   $ )a  
Add two integers or floats, converting them to integers if necessary.

Args:
    a (int, float): The first number.
    b (int, float): The second number, default is 98.
Returns:
    int: The sum of a and b as integers.
Raises:
    TypeError: If a or b is not an integer or float.
za must be an integerzb must be an integer)�
isinstance�int�float�	TypeError)�a�bs     �v/Users/vithushansatkunanathan/holbertonschool-higher_level_programming/python-test_driven_development/0-add_integer.py�add_integerr
      sW   � � �a�#�u��&�&��.�/�/��a�#�u��&�&��.�/�/��A��A��A��A��5�L�    N)�b   )�__doc__r
   � r   r	   �<module>r      s   ���r   