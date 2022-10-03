#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:43:09 2020

@author: Salifu
"""
import sys
import unittest
import inspect
import io
from contextlib import redirect_stdout
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    class for testing Rectangle class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Rectangle, inspect.isfunction)

    
    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """
        Tests if methods docstring documntation exist
        """
        for func in self.setup:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_wrong_inputted_values(self):
        """
        Test for negative and zero values
        """
        with self.assertRaises(ValueError):
            R = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            R = Rectangle(-4, -5)
        with self.assertRaises(ValueError):
            R = Rectangle(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            R = Rectangle()
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """
        Different types for inputted arguments
        """
        with self.assertRaises(TypeError):
            R = Rectangle('width', 'height')
        with self.assertRaises(TypeError):
            R = Rectangle(2.4, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            R = Rectangle(True, False)
        with self.assertRaises(TypeError):
            R = Rectangle(1, 2, True, False)
        with self.assertRaises(TypeError):
            R = Rectangle([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            R = Rectangle((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            R = Rectangle({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """
        Test for area method
        """
        R = Rectangle(10, 10)
        self.assertEqual(R.area(), 100)
        with self.assertRaises(TypeError):
            A = R.area(1)

    def test_str(self):
        """
        Test for __str__ method
        """
        R = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual("[Rectangle] (5) 3/4 - 1/2", str(R))

    def test_update_args(self):
        """
        Test for update method: args
        """
        R = Rectangle(1, 2, 3, 4, 5)
        R.update(6)
        self.assertEqual(6, R.id)
        R.update(6, 7)
        self.assertEqual(7, R.width)
        R.update(6, 7, 8)
        self.assertEqual(8, R.height)
        R.update(6, 7, 8, 9)
        self.assertEqual(9, R.x)
        R.update(6, 7, 8, 9, 10)
        self.assertEqual(10, R.y)

    def test_display(self):
        """
        Test display method
        """
        R = Rectangle(2, 3, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            R.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 3)
        R = Rectangle(2, 3, 4, 5, 6)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            R.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 5 + (' ' * 4 + '#' * 2 + '\n') * 3))

    def test_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        R = Rectangle(1, 2, 3, 4, 5)
        R.update(6, id=7)
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [6, 1, 2, 3, 4])
        R.update(6, 7, 8, x=9, y=10)
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [6, 7, 8, 3, 4])
        R.update(width=7, id=6, height=8)
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [6, 7, 8, 3, 4])
        R.update(x=40, y=5)
        self.assertEqual([R.id, R.width, R.height, R.x, R.y], [6, 7, 8, 40, 5])

    def test_dictionary(self):
        """
        Tests for dictionary method
        """
        R = Rectangle(100, 200, 300, 400, 500)
        R_dict = R.to_dictionary()
        self.assertEqual(R_dict['width'], 100)
        self.assertEqual(R_dict['height'], 200)
        self.assertEqual(R_dict['x'], 300)
        self.assertEqual(R_dict['y'], 400)
        self.assertEqual(R_dict['id'], 500)
