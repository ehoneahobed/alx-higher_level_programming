#!/usr/bin/python3
import unittest
import os
from models.rectangle import Rectangle
import json
from io import StringIO
import sys

'''
    Runs test cases for the Rectangle module
'''


class test_rectangle(unittest.TestCase):
    '''
        Testing rectangle
    '''

    def setUp(self):
        '''
            Initializing instance with width and height
            parameters
        '''
        self.r = Rectangle(5, 10)

    def tearDown(self):
        '''
            Deleting created instance
        '''
        del self.r

    def test_width(self):
        '''
            Testing the Rectangle width getter
        '''
        self.assertEqual(5, self.r.width)

    def test_height(self):
        '''
            Testing the Rectangle height getter
        '''
        self.assertEqual(10, self.r.height)

    def test_x(self):
        '''
            Testing Rectangle x getter and setter
        '''

        self.r.x = 54
        self.assertEqual(54, self.r.x)
        self.assertEqual(0, self.r.y)

    def test_y(self):
        '''
            Testing Rectangle y getter and setter
        '''

        self.r.y = 45
        self.assertEqual(45, self.r.y)
        self.assertEqual(0, self.r.x)

    def test_arectangle_id(self):
        '''
            Test the id for Rectangle
        '''
        rect = Rectangle(1, 3, 0, 0, 199)
        self.assertEqual(199, rect.id)

    def test_width_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle("1", 5)

    def test_width_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(True, 5)

    def test_width_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle([10, 6], 5)

    def test_height_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, "5")

    def test_height_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, True)

    def test_height_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, [10, 6])

    def test_x_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, "46")

    def test_x_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, [10, 6])

    def test_y_string(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, "46")

    def test_y_bool(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, True)

    def test_x_list(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1, 5, 7, [10, 6])

    def test_width_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(-4, 5)

    def test_height_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, -5)

    def test_x_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, -3)

    def test_y_negative(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(4, 5, 2, -3)

    def test_width_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 5)

    def test_height_zero(self):
        '''
            Testing with negative int
        '''
        with self.assertRaises(ValueError):
            rect = Rectangle(8, 0)

    def test_width_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(1.07, 5)

    def test_height_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 1.07)

    def test_x_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 8, 1.07)

    def test_y_float(self):
        '''
            Testing for other than int
        '''
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 5, 8, 1.07)

    def test_area(self):
        '''
            Testing the area of the rectangle
        '''
        self.assertEqual(self.r.area(), 5 * 10)
        rect = Rectangle(3, 9, 8, 8, 2)
        self.assertEqual(rect.area(), 3 * 9)

    def test_str_overload(self):
        r = Rectangle(5, 10, 8, 7, 88)
        self.assertEqual(r.__str__(), "[Rectangle] (88) 8/7 - 5/10")

    def test_update_id(self):
        '''
            Testing the update method
        '''
        self.r.update(54)
        self.assertEqual(54, self.r.id)

    def test_update_width(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30)
        self.assertEqual(30, self.r.width)

    def test_update_height(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10)
        self.assertEqual(10, self.r.height)

    def test_update_x(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10, 6)
        self.assertEqual(6, self.r.x)

    def test_update_y(self):
        '''
            Testing the update method
        '''
        self.r.update(54, 30, 10, 6, 2)
        self.assertEqual(2, self.r.y)

    def test_update_dict(self):
        '''
            Testing the update method with **kwargs
        '''
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(1, self.r.y)
        self.assertEqual(2, self.r.width)
        self.assertEqual(3, self.r.x)
        self.assertEqual(89, self.r.id)

    def test_update_dict_list(self):
        '''
            Testing the update method with **kwargs and *args
        '''
        self.r.update(1000, y=1, width=2, x=3, id=89)
        self.assertEqual(1000, self.r.id)

    def test_to_dict(self):
        '''
            Testing the type that is returned from the to_dictionary method
        '''
        r1 = Rectangle(5, 4)
        self.assertEqual(type(r1.to_dictionary()), dict)

    def test_to_dict_print(self):
        '''
            Testing the dict that will be printed
        '''
        r1 = Rectangle(5, 4, 0, 0, 400)
        r1_dict = r1.to_dictionary()
        self.assertEqual(r1_dict,
                         {'height': 4, 'id': 400, 'width': 5, 'x': 0, 'y': 0})

    def test_missing_height(self):
        '''
            Expecting a type error because height and width are missing
        '''
        with self.assertRaises(TypeError):
            Rectangle()

    def test_missing_width(self):
        '''
            Expecting an error because width is missing
        '''
        with self.assertRaises(TypeError):
            Rectangle(1)

    # write these tests for square as well
    def test_saving_to_file(self):
        '''
            Testing saving a file into json format
        '''
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file([r1])

        with open("Rectangle.json", "r") as file:
            content = file.read()
        t = [{"x": 0, "y": 0, "id": 346, "height": 10, "width": 5}]
        self.assertEqual(t, json.loads(content))

    def test_saving_to_file_no_iter(self):
        '''
            Sending a non iterable to the function
        '''
        with self.assertRaises(TypeError):
            Rectangle.save_to_file(self.r)

    def test_saving_to_file_None(self):
        '''
            Testing saving a file into json format sending None
        '''
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual("[]", content)

    def test_saving_to_file_type(self):
        '''
            Testing saving a file into json format sending None
        '''
        try:
            os.remove("Rectangle.json")
        except:
            pass
        r1 = Rectangle(5, 10, 0, 0, 346)
        Rectangle.save_to_file(None)

        with open("Rectangle.json", "r") as file:
            content = file.read()

        self.assertEqual(str, type(content))
        try:
            os.remove("Rectangle.json")
        except:
            pass

    def test_json_string_type(self):
            '''
                Testing the returned type
            '''
            list_input = [
                {'id': 2089, 'width': 10, 'height': 4},
                {'id': 2712, 'width': 1, 'height': 7}]
            json_list_input = Rectangle.to_json_string(list_input)
            list_output = Rectangle.from_json_string(json_list_input)
            self.assertEqual(type(list_input), list)

    def test_json_string(self):
            '''
                Testing that the json string gets converted into a list
            '''
            list_input = [
                {'id': 2089, 'width': 10, 'height': 4},
                {'id': 2712, 'width': 1, 'height': 7}]
            json_list_input = Rectangle.to_json_string(list_input)
            list_output = Rectangle.from_json_string(json_list_input)
            s1 = {'id': 2089, 'width': 10, 'height': 4}
            s2 = {'height': 7, 'id': 2712, 'width': 1}
            self.assertEqual(list_input[0], s1)
            self.assertEqual(list_input[1], s2)

    def test_dict_to_instance(self):
        '''
            test that an instance is created from a dict
        '''
        r1 = Rectangle(5, 8, 3)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertNotEqual(r1, r2)

    def test_isnot_dict_to_instance(self):
        '''
            test that an instance is created from a dict
        '''
        r1 = Rectangle(109, 80, 76)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertIsNot(r1, r2)

    def test_load_from_file_not_the_same(self):
        '''
            Checking that an object was created from the
            list but has a different adress.
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertNotEqual(id(r1), id(list_rectangles_output[0]))

    def test_load_from_file_same_width(self):
        '''
            Checking that an object was created from the
            list and has the same witdh
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.width, list_rectangles_output[0].width)

    def test_load_from_file_same_height(self):
        '''
            Checking that an object was created from the
            list and has the same height
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.height, list_rectangles_output[0].height)

    def test_load_from_file_same_x(self):
        '''
            Checking that an object was created from the
            list and has the same x
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.x, list_rectangles_output[0].x)

    def test_load_from_file_same_y(self):
        '''
            Checking that an object was created from the
            list and has the same y
        '''
        r1 = Rectangle(10, 7, 2, 8)
        list_rectangles_input = [r1]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        self.assertEqual(r1.y, list_rectangles_output[0].y)

    def test_display_square(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(10, 4)
        r1.display()
        sys.stdout = sys.__stdout__
        output = ("##########\n" +
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
        r1 = Rectangle(1, 2)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '#\n#\n'
        self.assertEqual(capturedOutput.getvalue(), output)

    def test_display_square_size_zero(self):
        '''
            Checking the stdout output by capturing it
        '''
        capturedOutput = StringIO()
        sys.stdout = capturedOutput
        r1 = Rectangle(3, 7)
        r1.display()
        sys.stdout = sys.__stdout__

        output = '###\n###\n###\n###\n###\n###\n###\n'
        self.assertEqual(capturedOutput.getvalue(), output)
