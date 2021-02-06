# Unit test for calculating cube volume
# By: Kyle Huang
import unittest
from cube import calc_cube
from avg_elem import avg_list
from name import name


class CubeTest(unittest.TestCase):
    # check for negative number
    # Edge case
    def test_negative(self):
        self.assertEqual(calc_cube(-2), 8.0)

    # Check for raised value error
    # Fail case
    def test_type_error(self):
        with self.assertRaises(ValueError):
            calc_cube('a')

    # check for whole number
    # Good case
    def test_whole_number(self):
        self.assertEqual(calc_cube(5), 125.0)


class ListTest(unittest.TestCase):
    # Test for whole numbers in a list
    # Good case
    def test_whole_number(self):
        ls = [1, 2, 3, 4, 5, 6]
        self.assertEqual(avg_list(ls), 3.5)

    # test for empty list
    # Edge Case
    def test_empty(self):
        self.assertEqual(avg_list([]), 0)

    # test for list that contains a char
    # Fail case
    def test_char(self):
        ls = [1, 2, 3, 4, 'a', 6]
        # There is a type error
        with self.assertRaises(TypeError):
            avg_list(ls)


class NameTest(unittest.TestCase):
    # Test for name with first and last
    # Good case
    def test_whole_name(self):
        first = "Kyle"
        last = "Huang"
        self.assertEqual(name(first, last), "Kyle Huang")

    # test for no first name
    # Edge case
    def test_no_first(self):
        first = ""
        last = "Huang"
        self.assertEqual(name(first, last), " Huang")

    # Test for int as one of the names
    # Fail case
    def test_int_name(self):
        first = "Kyle"
        last = 1
        with self.assertRaises(TypeError):
            name(first, last)

if __name__ == '__main__':
    unittest.main()
