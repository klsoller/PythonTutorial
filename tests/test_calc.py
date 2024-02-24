"""
test_calc.py
Doc summary.
LICENSE: All Rights Reserved.
"""

import sys
import os

# fmt: off

## this turns the black formatting off.
sys.path.append("../PythonTutorial")
cd = os.path

# fmt: on

import tests.calc as calc
import unittest

# capital name for constants
COLOR = (255, 255, 255)


class Test_Class(unittest.TestCase):

    def test_add(self):
        # result = calc.add(10, 5)  # Don't do this.
        # self.assertEqual(result, 15)  # Don't do this.
        self.assertEqual(calc.add(10, 5), 15)  # This is better code.
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)

        # self.assertRaises(ValueError, calc.divide, 10, 0)  # Don't do this.
        with self.assertRaises(ValueError):  # This is better code.
            calc.divide(10, 0)


if __name__ == "__main__":
    unittest.main()
