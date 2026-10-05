"""Unit tests for the numimath operations module."""

import unittest
import sys
import os

# Ensure src layout is on sys.path for direct test execution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from numimath import (
    add,
    subtract,
    multiply,
    divide,
    mean,
    median,
    percentage,
    range_span,
    __version__,
)


class TestNumimathOperations(unittest.TestCase):

    def test_version(self):
        self.assertEqual(__version__, "0.1.0")

    def test_add(self):
        self.assertEqual(add(2, 3), 5.0)
        self.assertEqual(add(-1, 1), 0.0)
        self.assertEqual(add(0.5, 0.25), 0.75)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6.0)
        self.assertEqual(subtract(0, 5), -5.0)
        self.assertEqual(subtract(3.5, 1.5), 2.0)

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12.0)
        self.assertEqual(multiply(-2, 5), -10.0)
        self.assertEqual(multiply(0, 100), 0.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(7, 2), 3.5)
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_mean(self):
        self.assertEqual(mean([1, 2, 3, 4, 5]), 3.0)
        self.assertEqual(mean([10, 20]), 15.0)
        with self.assertRaises(ValueError):
            mean([])

    def test_median(self):
        # Odd count
        self.assertEqual(median([1, 3, 2]), 2.0)
        # Even count
        self.assertEqual(median([1, 2, 3, 4]), 2.5)
        with self.assertRaises(ValueError):
            median([])

    def test_percentage(self):
        self.assertEqual(percentage(25, 100), 25.0)
        self.assertEqual(percentage(1, 4), 25.0)
        with self.assertRaises(ZeroDivisionError):
            percentage(10, 0)

    def test_range_span(self):
        self.assertEqual(range_span([10, 2, 5, 15]), 13.0)
        self.assertEqual(range_span([7, 7, 7]), 0.0)
        with self.assertRaises(ValueError):
            range_span([])


if __name__ == "__main__":
    unittest.main()
