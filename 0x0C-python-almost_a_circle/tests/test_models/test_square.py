#!/usr/bin/python3
from contextlib import redirect_stdout
import contextlib
import inspect
import io
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
import sys
import json
from io import StringIO


'''
    Runs test cases for the square module
'''


class test_square(unittest.TestCase):
    '''
        Testing square
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.s = Square(5)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        del self.s

    def test_width(self):
        '''
            Testing the square width getter
        '''
        self.assertEqual(5, self.s.width)

    def test_height(self):
        '''
            Testing the square height getter
        '''
        self.assertEqual(5, self.s.height)

    def test_x(self):
        '''
            Testing square x getter and setter
        '''

        self.s.x = 54
        self.assertEqual(54, self.s.x)
        self.assertEqual(0, self.s.y)

    def test_y(self):
        '''
            Testing square y getter and setter
        '''

        self.s.y = 45
        self.assertEqual(45, self.s.y)
        self.assertEqual(0, self.s.x)

    def test_asquare_id(self):
        '''
            Test the id for square
        '''
        sq = Square(2, 0, 0, 199)
        self.assertEqual(199, sq.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square("1")

    def test_width_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(True)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square([10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, "46")

    def test_x_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, "46")

    def test_y_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, True)

    def test_y_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(-4)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(4, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            sq = Square(0, 5)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(1.07, 5)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            sq = Square(5, 8, 1.07)

    def test_area(self):
        '''
            Testing the area of the square
        '''
        self.assertEqual(self.s.area(), 5 * 5)
        sq = Square(3, 8, 8, 2)
        self.assertEqual(sq.area(), 3 * 3)

    def test_str_overload(self):
        s = Square(5, 8, 7, 88)
        self.assertEqual(s.__str__(), "[Square] (88) 8/7 - 5")

    def test_update_id(self):
        '''
            Testing the update method
        '''
        self.s.update(54)
        self.assertEqual(54, self.s.id)

    def test_update_width(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30)
        self.assertEqual(5, self.s.width)

    def test_update_height(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 10)
        self.assertEqual(5, self.s.height)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 10)
        self.assertEqual(10, self.s.x)

    def test_update_y(self):
        '''
            Testing the update method
        '''
        self.s.update(54, 30, 6, 2)
        self.assertEqual(2, self.s.y)

    def test_update_dict(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update(y=1, size=2, x=3, id=89)
        self.assertEqual(1, self.s.y)
        self.assertEqual(2, self.s.size)
        self.assertEqual(3, self.s.x)
        self.assertEqual(89, self.s.id)

    def test_update_dict_list(self):
        '''
            Testing the update method with **kwargs and *args
        '''
        self.s.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.s.id)

    def test_update_dict_no_key(self):
        '''
            Testing the update method with **kwargs
        '''
        self.s.update(y=1, size=2, xox=3, id=89)

    def test_update_string(self):
        '''
            Testing the update method with **kwargs
        '''
        # self.assertEqual(self.s.id, "str")
        with self.assertRaises(TypeError):
           self.s.update("str") 

    def test_to_dict(self):
        '''
            Testing the type that is returned from the to_dictionary method
        '''
        r1 = Square(5)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        '''
            Testing the dict that will be printed
        '''
        r1 = Square(5, 0, 0, 410)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                         {'size': 5, 'id': 410, 'x': 0, 'y': 0})

    def test_missing_height(self):
        '''
            Expecting a type error because height and width are missing
        '''
        with self.assertRaises(TypeError):
            Square()

    def test_saving_to_file(self):
        '''
            Testing saving a file into json format
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()
        t = [{"id": 346, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(t, json.loads(content))

    def test_saving_to_file_no_iter(self):
        '''
            Sending a non iterable to the function
        '''
        with self.assertRaises(TypeError):
            Square.save_to_file(self.s)

    def test_saving_to_file_None(self):
        '''
            Testing saving a file into json format sending None
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file(None)

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        '''
            Testing saving a file into json format and testing the type
        '''
        try:
            os.remove("Square.json")
        except:
            pass
        r1 = Square(5, 0, 0, 346)
        Square.save_to_file([r1])

        with open("Square.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Square.json")
        except:
            pass

    def test_json_string_type(self):
            '''
                Testing the returned type
            '''
            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 1}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            self.assertEqual(type(list_input), list)

    def test_json_string(self):
            '''
                Testing that the json string gets converted into a list
            '''
            list_input = [
                {'id': 2089, 'size': 10},
                {'id': 2712, 'size': 7}]
            json_list_input = Square.to_json_string(list_input)
            list_output = Square.from_json_string(json_list_input)
            s1 = {'id': 2089, 'size': 10}
            s2 = {'size': 7, 'id': 2712}
            self.assertEqual(list_input[0], s1)
            self.assertEqual(list_input[1], s2)

    def test_dict_to_instance(self):
        '''
            test that an instance is created from a dict
        '''
        r1 = Square(5)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        '''
            test that an instance is created from a dict
        '''
        r1 = Square(109)
        r1_dictionary = r1.to_dictionary()
        r2 = Square.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        '''
            Checking that an object was created from the
            list but has a different adress.
        '''
        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertNotEqual(id(r1), id(list_squares_output[0]))

    def test_load_from_file_same_width(self):
        '''
            Checking that an object was created from the
            list and has the same witdh
        '''
        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.width, list_squares_output[0].size)

    def test_load_from_file_same_height(self):
        '''
            Checking that an object was created from the
            list and has the same height
        '''
        r1 = Square(10)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.size, list_squares_output[0].size)

    def test_load_from_file_same_x(self):
        '''
            Checking that an object was created from the
            list and has the same x
        '''
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.x, list_squares_output[0].x)

    def test_load_from_file_same_y(self):
        '''
            Checking that an object was created from the
            list and has the same y
        '''
        r1 = Square(10, 2, 8)
        list_squares_input = [r1]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        self.assertEqual(r1.y, list_squares_output[0].y)

    def test_display_square(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(10)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n" +
                  "##########\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_one(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(1)
        r1.display()
        sys.stdout = sys.__stdout__

        output = ("#\n")
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Square(3)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)

class TestSquare(unittest.TestCase):
    """
    class for testing Square class' methods
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method for the doc tests
        """
        cls.setup = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """
        Tests if module docstring documentation exist
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_class_docstring(self):
        """
        Tests if class docstring documentation exist
        """
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_wrong_inputted_values(self):
        """
        Test for negative and zero values
        """
        with self.assertRaises(ValueError):
            S = Square(0, 0)
        with self.assertRaises(ValueError):
            S = Square(-4, -5)
        with self.assertRaises(ValueError):
            S = Square(1, 1, -2, -2)
        with self.assertRaises(TypeError):
            S = Square()
        with self.assertRaises(TypeError):
            S = Square(1, 2, 3, 4, 5, 6, 7)

    def test_inputted_types(self):
        """
        Different types for inputted arguments
        """
        with self.assertRaises(TypeError):
            S = Square('width', 'height')
        with self.assertRaises(TypeError):
            S = Square(2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(1, 2, 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square(1, 2, 2.4, 1.3)
        with self.assertRaises(TypeError):
            S = Square(True, False)
        with self.assertRaises(TypeError):
            S = Square(1, 2, True, False)
        with self.assertRaises(TypeError):
            S = Square([1, 1], 2, 3, 4)
        with self.assertRaises(TypeError):
            S = Square((1, 2), 'x value', 'y value')
        with self.assertRaises(TypeError):
            S = Square({1: 3, 2: 4}, 5, 6)

    def test_area(self):
        """
        Test for area method
        """
        S = Square(10, 10)
        self.assertEqual(S.area(), 100)
        with self.assertRaises(TypeError):
            A = S.area(1)

    def test_str(self):
        """
        Test for __str__ method
        """
        S = Square(1, 2, 3, 4)
        self.assertEqual("[Square] (4) 2/3 - 1", str(S))

    def test_update_args(self):
        """
        Test for update method: args
        """
        S = Square(1, 2, 3, 4)
        S.update(6)
        self.assertEqual(6, S.id)
        S.update(6, 7)
        self.assertEqual(7, S.size)
        S.update(6, 7, 8)
        self.assertEqual(8, S.x)
        S.update(6, 7, 8, 9)
        self.assertEqual(9, S.y)

    def test_display(self):
        """
        Test display method
        """
        S = Square(2, 0, 0, 4)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output, ('#' * 2 + '\n') * 2)
        S = Square(2, 3, 4, 5)
        with io.StringIO() as bufferIO, redirect_stdout(bufferIO):
            S.display()
            output = bufferIO.getvalue()
            self.assertEqual(output,
                             ('\n' * 4 + (' ' * 3 + '#' * 2 + '\n') * 2))

    def test_update_kwargs(self):
        """
        Test for update method: kwargs
        """
        S = Square(1, 2, 3, 4)
        S.update(6, id=7)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 1, 2, 3])
        S.update(6, 7, x=9, y=10)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(width=7, id=6, height=8)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 2, 3])
        S.update(x=40, y=5)
        self.assertEqual([S.id, S.size, S.x, S.y], [6, 7, 40, 5])

    def test_dictionary(self):
        """
        Tests for dictionary method
        """
        S = Square(100, 300, 400, 500)
        S_dict = S.to_dictionary()
        self.assertEqual(S_dict['size'], 100)
        self.assertEqual(S_dict['x'], 300)
        self.assertEqual(S_dict['y'], 400)
        self.assertEqual(S_dict['id'], 500)


class TestSquare(unittest.TestCase):
    """Test class for Square class."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_10_0(self):
        """Test Square class: check for attributes."""

        s0 = Square(1)
        self.assertEqual(s0.id, 1)
        s1 = Square(5, 3, 4)
        self.assertEqual(s1.height, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.x, 3)
        self.assertEqual(s1.y, 4)
        self.assertEqual(s1.id, 2)

    def test_10_1(self):
        """Test __str__ representation."""

        s1 = Square(9, 4, 5, 6)
        self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

    def test_10_2(self):
        """Test Square class: check for inheritance."""

        s1 = Square(6)
        self.assertTrue(isinstance(s1, Rectangle))
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertFalse(isinstance(Square, Rectangle))
        self.assertTrue(isinstance(s1, Base))
        self.assertTrue(issubclass(Square, Base))
        self.assertFalse(isinstance(Square, Base))

    # def test_10_3(self):
    #     """Test Square class: check for missing args."""

    #     with self.assertRaises(TypeError) as x:
    #         s1 = Square()
    #     self.assertEqual(
    #         "__init__() missing 1 required positional argument: 'size'", str(
    #             x.exception))

    def test_10_4(self):
        """Test Square for methods inherited from Rectangle."""

        s1 = Square(9)
        self.assertEqual(s1.area(), 81)
        s2 = Square(4, 1, 2, 5)
        s2.update(7)
        self.assertEqual(s2.id, 7)
        f = io.StringIO()
        s3 = Square(4)
        with contextlib.redirect_stdout(f):
            s3.display()
        s = f.getvalue()
        res = "####\n####\n####\n####\n"
        self.assertEqual(s, res)

    def test_11_0(self):
        """Test Square class: check for size attribute."""

        s1 = Square(8)
        self.assertEqual(s1.size, 8)
        s2 = Square(9, 8, 7, 2)
        self.assertEqual(s2.size, 9)

    def test_11_1(self):
        """Test Square class: check for wrong attributes."""

        with self.assertRaises(TypeError) as x:
            s = Square("Hello", 2)
        self.assertEqual("width must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(2, "World")
        self.assertEqual("x must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s = Square(1, 2, "Foo", 3)
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(0, 2)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(-1)
        self.assertEqual("width must be > 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, -3)
        self.assertEqual("x must be >= 0", str(x.exception))
        with self.assertRaises(ValueError) as x:
            s = Square(2, 5, -5, 6)
        self.assertEqual("y must be >= 0", str(x.exception))

    def test_12_0(self):
        """Test update method on Square."""

        s1 = Square(5)
        s1.update(10)
        self.assertEqual(s1.id, 10)
        s1.update(x=12)
        self.assertEqual(s1.x, 12)
        s1.update(size=7, id=89, y=1)
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)
        s1.update()
        self.assertEqual(s1.size, 7)
        self.assertEqual(s1.id, 89)
        self.assertEqual(s1.y, 1)

    def test_12_1(self):
        """Test for update method on Square with wrong types."""

        s1 = Square(9)
        with self.assertRaises(TypeError) as x:
            s1.update(2, 3, 4, "hello")
        self.assertEqual("y must be an integer", str(x.exception))
        with self.assertRaises(TypeError) as x:
            s1.update("hello", 8, 9)
        self.assertEqual("id must be an integer", str(x.exception))

    def test_14_0(self):
        """Test for public method to_dictionary."""

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
        self.assertEqual(len(s1_dictionary), len(s_dictionary))
        self.assertEqual(type(s1_dictionary), dict)
        s2 = Square(1, 1)
        s2.update(**s1_dictionary)
        s2_dictionary = s2.to_dictionary()
        self.assertEqual(len(s1_dictionary), len(s2_dictionary))
        self.assertEqual(type(s2_dictionary), dict)
        self.assertFalse(s1 == s2)

    # def test_14_1(self):
    #     """Test for public method to_dictionary with wrong args."""

    #     s = "to_dictionary() takes 1 positional argument but 2 were given"
    #     with self.assertRaises(TypeError) as x:
    #         s1 = Square(10, 2, 1, 9)
    #         s1_dictionary = s1.to_dictionary("Hi")
    #     self.assertEqual(s, str(x.exception))


if __name__ == '__main__':
    unittest.main()
