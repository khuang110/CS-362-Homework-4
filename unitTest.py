# Unit test for calculating cube volume
# By: Kyle Huang
import unittest
from cube import calc_cube
from avg_elem import avg_list
import name


class CubeTest(unittest.TestCase):
    def test_negative(self):
        self.assertEqual(calc_cube(-2), 8.0)

    def test_type_error(self):
        self.assertEqual(calc_cube("a"), "Undefined, Value Error")

    def test_whole_number(self):
        self.assertEqual(calc_cube(5), 125.0)


class ListTest(unittest.TestCase):
    # Test for whole numbers in a list
    def test_whole_number(self):
        ls = [1, 2, 3, 4, 5, 6]
        self.assertEqual(avg_list(ls), 3.5)

    # test for empty list
    def test_empty(self):
        self.assertEqual(avg_list([]), 0)

    # test for list that contains a char
    def test_char(self):
        ls = [1, 2, 3, 4, 'a', 6]
        self.assertEqual(avg_list(ls), "Type Error")


class NameTest(unittest.TestCase):
    # Test for name with first and last
    def test_whole_name(self):
        first = "Kyle"
        last = "Huang"
        self.assertEqual(name(first, last), "Kyle Huang")

if __name__ == '__main__':
    unittest.main()
