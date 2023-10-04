#!/usr/bin/python3
"""unittest square.py file


    testSquare__init__
    testSquare_width
    testSquare_height
    testSquare_x
    testSquare_y
    testSquare_area
    testSquare_to_dictionary
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testSquare__init__(unittest.TestCase):
    """unittest class Square __init__"""

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Square()

    def test_one_argument(self):
        sq1 = Square(3)
        sq2 = Square(5)
        self.assertEqual(sq1.id, sq2.id - 1)

    def test_two_arguments(self):
        sq1 = Square(4, 9)
        sq2 = Square(8, 12)
        self.assertEqual(sq1.id, sq2.id - 1)


if __name__ == "__main__":
    unittest.main()
