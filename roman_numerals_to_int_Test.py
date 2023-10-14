import unittest
from roman_numerals_to_int import roman_numerals_to_int


class TestRomanNumeralsToInt(unittest.TestCase):

    def test_area(self):
        self.assertEqual(roman_numerals_to_int('XIV'), 14)
        self.assertEqual(roman_numerals_to_int('XVI'), 16)
        self.assertEqual(roman_numerals_to_int('MCMLXXXVI'), 1986)
        self.assertEqual(roman_numerals_to_int('MMM'), 3000)
        self.assertEqual(roman_numerals_to_int('LXVIII'), 68)

        self.assertEqual(roman_numerals_to_int(11), None)
        self.assertEqual(roman_numerals_to_int('hello'), None)
        self.assertEqual(roman_numerals_to_int(['h', 'e']), None)