#!/usr/bin/python3
import unittest
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

    # def test_update_width(self):
    #     '''
    #         Testing the update method
    #     '''
    #     self.s.update(54, 30)
    #     self.assertEqual(30, self.s.width)

    # def test_update_height(self):
    #     '''
    #         Testing the update method
    #     '''
    #     self.s.update(54, 10)
    #     self.assertEqual(10, self.s.height)

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

    # def test_update_string(self):
    #     '''
    #         Testing the update method with **kwargs
    #     '''
    #     self.s.update("str")
    #     self.assertEqual(self.s.id, "str")

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
