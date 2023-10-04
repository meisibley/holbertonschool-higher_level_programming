#!/usr/bin/python3
"""unittest rectangle.py file


    testRectangle__init__
    testRectangle_width
    testRectangle_height
    testRectangle_x
    testRectangle_y
    testRectangle_area
    testRectangle_to_dictionary
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class testRectangle__init__(unittest.TestCase):
    """unittest class Rectangle __init__"""

    def test_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_one_argument(self):
        with self.assertRaises(TypeError):
            Rectangle(10)

    def test_two_arguments(self):
        rect1 = Rectangle(4, 9)
        rect2 = Rectangle(8, 12)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_four_arguments(self):
        rect1 = Rectangle(4, 9, 23, 4)
        rect2 = Rectangle(8, 12, 2, 6)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle(3, 4, 5, 9, 0, 12)

    def test_width_getter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(5, rect.width)

    def test_height_getter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(6, rect.height)

    def test_x_getter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(7, rect.x)

    def test_y_getter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        self.assertEqual(8, rect.y)

    def test_width_setter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        rect.width = 10
        self.assertEqual(10, rect.width)

    def test_height_setter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        rect.height = 10
        self.assertEqual(10, rect.height)

    def test_x_setter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        rect.x = 10
        self.assertEqual(10, rect.x)

    def test_y_setter(self):
        rect = Rectangle(5, 6, 7, 8, 9)
        rect.y = 10
        self.assertEqual(10, rect.y)


class testRectangle_width(unittest.TestCase):
    """unittest Rectangle width method"""

    def test_none_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 5)

    def test_str_width(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("integer", 5)


if __name__ == "__main__":
    unittest.main()
