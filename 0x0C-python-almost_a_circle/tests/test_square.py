# #!/usr/bin/python3
# """Unittest square.
# Test cases for the Square class.
# Each test has the number of the task,
# and the number of the test for that task
# (i.e 'test_17_0' for the first test of task 17)
# """

# import unittest
# import io
# import contextlib
# from models.base import Base
# from models.rectangle import Rectangle
# from models.square import Square


# class TestSquare(unittest.TestCase):
#     """Test class for Square class."""

#     def setUp(self):
#         Base._Base__nb_objects = 0

#     def test_10_0(self):
#         """Test Square class: check for attributes."""

#         s0 = Square(1)
#         self.assertEqual(s0.id, 1)
#         s1 = Square(5, 3, 4)
#         self.assertEqual(s1.height, 5)
#         self.assertEqual(s1.width, 5)
#         self.assertEqual(s1.x, 3)
#         self.assertEqual(s1.y, 4)
#         self.assertEqual(s1.id, 2)

#     def test_10_1(self):
#         """Test __str__ representation."""

#         s1 = Square(9, 4, 5, 6)
#         self.assertEqual(str(s1), "[Square] (6) 4/5 - 9")

#     def test_10_2(self):
#         """Test Square class: check for inheritance."""

#         s1 = Square(6)
#         self.assertTrue(isinstance(s1, Rectangle))
#         self.assertTrue(issubclass(Square, Rectangle))
#         self.assertFalse(isinstance(Square, Rectangle))
#         self.assertTrue(isinstance(s1, Base))
#         self.assertTrue(issubclass(Square, Base))
#         self.assertFalse(isinstance(Square, Base))

#     # def test_10_3(self):
#     #     """Test Square class: check for missing args."""

#     #     with self.assertRaises(TypeError) as x:
#     #         s1 = Square()
#     #     self.assertEqual(
#     #         "__init__() missing 1 required positional argument: 'size'", str(
#     #             x.exception))

#     def test_10_4(self):
#         """Test Square for methods inherited from Rectangle."""

#         s1 = Square(9)
#         self.assertEqual(s1.area(), 81)
#         s2 = Square(4, 1, 2, 5)
#         s2.update(7)
#         self.assertEqual(s2.id, 7)
#         f = io.StringIO()
#         s3 = Square(4)
#         with contextlib.redirect_stdout(f):
#             s3.display()
#         s = f.getvalue()
#         res = "####\n####\n####\n####\n"
#         self.assertEqual(s, res)

#     def test_11_0(self):
#         """Test Square class: check for size attribute."""

#         s1 = Square(8)
#         self.assertEqual(s1.size, 8)
#         s2 = Square(9, 8, 7, 2)
#         self.assertEqual(s2.size, 9)

#     def test_11_1(self):
#         """Test Square class: check for wrong attributes."""

#         with self.assertRaises(TypeError) as x:
#             s = Square("Hello", 2)
#         self.assertEqual("width must be an integer", str(x.exception))
#         with self.assertRaises(TypeError) as x:
#             s = Square(2, "World")
#         self.assertEqual("x must be an integer", str(x.exception))
#         with self.assertRaises(TypeError) as x:
#             s = Square(1, 2, "Foo", 3)
#         self.assertEqual("y must be an integer", str(x.exception))
#         with self.assertRaises(ValueError) as x:
#             s = Square(0, 2)
#         self.assertEqual("width must be > 0", str(x.exception))
#         with self.assertRaises(ValueError) as x:
#             s = Square(-1)
#         self.assertEqual("width must be > 0", str(x.exception))
#         with self.assertRaises(ValueError) as x:
#             s = Square(2, -3)
#         self.assertEqual("x must be >= 0", str(x.exception))
#         with self.assertRaises(ValueError) as x:
#             s = Square(2, 5, -5, 6)
#         self.assertEqual("y must be >= 0", str(x.exception))

#     def test_12_0(self):
#         """Test update method on Square."""

#         s1 = Square(5)
#         s1.update(10)
#         self.assertEqual(s1.id, 10)
#         s1.update(x=12)
#         self.assertEqual(s1.x, 12)
#         s1.update(size=7, id=89, y=1)
#         self.assertEqual(s1.size, 7)
#         self.assertEqual(s1.id, 89)
#         self.assertEqual(s1.y, 1)
#         s1.update()
#         self.assertEqual(s1.size, 7)
#         self.assertEqual(s1.id, 89)
#         self.assertEqual(s1.y, 1)

#     def test_12_1(self):
#         """Test for update method on Square with wrong types."""

#         s1 = Square(9)
#         with self.assertRaises(TypeError) as x:
#             s1.update(2, 3, 4, "hello")
#         self.assertEqual("y must be an integer", str(x.exception))
#         with self.assertRaises(TypeError) as x:
#             s1.update("hello", 8, 9)
#         self.assertEqual("id must be an integer", str(x.exception))

#     def test_14_0(self):
#         """Test for public method to_dictionary."""

#         s1 = Square(10, 2, 1)
#         s1_dictionary = s1.to_dictionary()
#         s_dictionary = {'x': 2, 'y': 1, 'id': 1, 'size': 10}
#         self.assertEqual(len(s1_dictionary), len(s_dictionary))
#         self.assertEqual(type(s1_dictionary), dict)
#         s2 = Square(1, 1)
#         s2.update(**s1_dictionary)
#         s2_dictionary = s2.to_dictionary()
#         self.assertEqual(len(s1_dictionary), len(s2_dictionary))
#         self.assertEqual(type(s2_dictionary), dict)
#         self.assertFalse(s1 == s2)

#     # def test_14_1(self):
#     #     """Test for public method to_dictionary with wrong args."""

#     #     s = "to_dictionary() takes 1 positional argument but 2 were given"
#     #     with self.assertRaises(TypeError) as x:
#     #         s1 = Square(10, 2, 1, 9)
#     #         s1_dictionary = s1.to_dictionary("Hi")
#     #     self.assertEqual(s, str(x.exception))


# if __name__ == '__main__':
#     unittest.main()
