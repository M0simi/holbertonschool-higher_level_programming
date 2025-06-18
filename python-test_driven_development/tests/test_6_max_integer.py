#!/usr/bin/python3
"""Unittest for max_integer
"""
import unittest

max_integer = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        self.assertEqual(max_integer([10]), 10)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_mixed_signs(self):
        self.assertEqual(max_integer([-10, 0, 20, -5]), 20)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 0.3]), 2.7)

    def test_string(self):
        self.assertEqual(max_integer("abcd"), "d")

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(123)


if __name__ == "__main__":
    unittest.main()
