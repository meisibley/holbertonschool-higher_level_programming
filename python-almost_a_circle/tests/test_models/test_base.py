#!/usr/bin/python3
"""unittests for base.py file:


    testBase__init__
    testBase_to_json_string
    testBase_save_to_file
    testBase_from_json_string
    testBase_create
    testBase_load_from_file
"""

import os
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class testBase__init__(unittest.TestCase):
    """unittests for Base class init instances"""

    def test_id_next_seq(self):
        base_obj1 = Base()
        base_obj2 = Base()
        self.assertEqual(base_obj1.id, 1)
        self.assertEqual(base_obj2.id, 2)

    def test_id_given_value(self):
        self.assertEqual(24, Base(24).id)

    def test_id_seq(self):
        base_obj4 = Base()
        base_obj5 = Base()
        base_obj6 = Base()
        self.assertEqual(base_obj4.id, base_obj5.id - 1)
        self.assertEqual(base_obj4.id, base_obj6.id - 2)


class testBase_to_json_string(unittest.TestCase):
    """unittests for Base class to_json_string method"""

    def test_to_json_string_rectangle_type(self):
        rect = Rectangle(3, 7, 5, 2, 2)
        self.assertEqual(str, type(Base.to_json_string([rect.to_dictionary()])))

    def test_to_json_string_square_type(self):
        sq = Square(6, 5, 2, 2)
        self.assertEqual(str, type(Base.to_json_string([sq.to_dictionary()])))

    def test_to_json_string_empty_list(self):
        self.assertEqual("[]", Base.to_json_string([]))

    def test_to_json_string_none(self):
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.to_json_string()


class testBase_save_to_file(unittest.TestCase):
    """unittest save_to_file method"""

    @classmethod
    def delete_pre_files(self):
        """delete previous files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_save_to_file_one_rectangle(self):
        rect = Rectangle(3, 7, 5, 12, 2)
        Rectangle.save_to_file([rect])
        with open("Rectangle.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) == 53)

    def test_save_to_file_one_square(self):
        sq = Square(13, 7, 2, 2)
        Square.save_to_file([sq])
        with open("Square.json", "r") as a_file:
            self.assertTrue(len(a_file.read()) == 39)

    def test_save_to_file_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file()

    def test_save_to_file_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], 10)


class testBase_from_json_string(unittest.TestCase):
    """unittest from_json_string method"""

    def test_from_json_string_type(self):
        a_list = [{"id": 3, "width": 7, "height": 5, "x": 12, "y": 2}]
        json_list = Rectangle.to_json_string(a_list)
        b_list = Rectangle.from_json_string(json_list)
        self.assertEqual(list, type(b_list))

    def test_from_json_string_none(self):
        self.assertEqual([], Base.from_json_string(None))

    def test_from_json_string_empty(self):
        self.assertEqual([], Base.from_json_string("[]"))

    def test_from_json_string_no_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string()

    def test_from_json_string_too_many_arguments(self):
        with self.assertRaises(TypeError):
            Base.from_json_string([], 10)


class testBase_create(unittest.TestCase):
    """unittest create method"""

    def test_create_rectangle_original(self):
        rect1 = Rectangle(3, 7, 5, 12, 2)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (2) 5/12 - 3/7", str(rect1))

    def test_create_rectangle_new(self):
        rect1 = Rectangle(3, 7, 5, 12, 2)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertEqual("[Rectangle] (2) 5/12 - 3/7", str(rect2))

    def test_create_rectangle_is(self):
        rect1 = Rectangle(3, 7, 5, 12, 2)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertIsNot(rect1, rect2)

    def test_create_rectangle_equal(self):
        rect1 = Rectangle(3, 7, 5, 12, 2)
        rect1_dict = rect1.to_dictionary()
        rect2 = Rectangle.create(**rect1_dict)
        self.assertNotEqual(rect1, rect2)

    def test_create_square_original(self):
        sq1 = Square(3, 7, 12, 2)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (2) 7/12 - 3", str(sq1))

    def test_create_square_new(self):
        sq1 = Square(3, 7, 5, 12)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertEqual("[Square] (12) 7/5 - 3", str(sq2))

    def test_create_square_is(self):
        sq1 = Square(7, 5, 12, 2)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertIsNot(sq1, sq2)

    def test_create_square_equal(self):
        sq1 = Square(7, 5, 12, 2)
        sq1_dict = sq1.to_dictionary()
        sq2 = Square.create(**sq1_dict)
        self.assertNotEqual(sq1, sq2)


class testBase_load_from_file(unittest.TestCase):
    """unittest load_from_file method"""

    @classmethod
    def delet_pre_files(self):
        """delete previous files"""
        try:
            os.remove("Rectangle.json")
        except IOError:
            pass
        try:
            os.remove("Square.json")
        except IOError:
            pass
        try:
            os.remove("Base.json")
        except IOError:
            pass

    def test_load_from_file_one_rect(self):
        rect1 = Rectangle(7, 5, 3, 2, 1)
        rect2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertEqual(str(rect1), str(list_rect[0]))

    def test_load_from_file_rect_type(self):
        rect1 = Rectangle(7, 5, 3, 2, 1)
        rect2 = Rectangle(2, 3, 4, 5, 6)
        Rectangle.save_to_file([rect1, rect2])
        list_rect = Rectangle.load_from_file()
        self.assertTrue(all(type(obj) is Rectangle for obj in list_rect))

    def test_load_from_file_one_square(self):
        sq1 = Square(7, 5, 2, 1)
        sq2 = Square(2, 4, 5, 6)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertEqual(str(sq1), str(list_sq[0]))

    def test_load_from_file_square_type(self):
        sq1 = Square(7, 5, 2, 1)
        sq2 = Square(2, 4, 5, 6)
        Square.save_to_file([sq1, sq2])
        list_sq = Square.load_from_file()
        self.assertTrue(all(type(obj) is Square for obj in list_sq))
