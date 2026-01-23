#!/usr/bin/python3
"""Unittests for max_integer([..])."""

import os
import sys
import unittest

# Ensure we can import 6-max_integer.py from the project root
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_ordered_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_end(self):
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)

    def test_single_element(self):
        self.assertEqual(max_integer([7]), 7)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_default_argument(self):
        self.assertIsNone(max_integer())

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-10, -2, -30, -1]), -1)

    def test_mixed_positive_negative(self):
        self.assertEqual(max_integer([-10, 0, 5, -3]), 5)

    def test_duplicates(self):
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 2.7, 2.6]), 2.7)

    def test_strings(self):
        self.assertEqual(max_integer(["a", "z", "b"]), "z")

    def test_mixed_types_raises(self):
        with self.assertRaises(TypeError):
            max_integer([1, "2", 3])


if __name__ == "__main__":
    unittest.main()
