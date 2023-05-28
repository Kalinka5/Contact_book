import unittest

from Exceptions.invalid_contact import InvalidLengthNumberException
from Exceptions.validity_checks import check_on_invalid_length_number


class TestLengthNumber(unittest.TestCase):
    def test_empty_length_number(self):
        digits = ''
        number = ''
        with self.assertRaises(InvalidLengthNumberException):
            check_on_invalid_length_number(digits, number)

    def test_6_length_number(self):
        digits = '111111'
        number = '111111'
        check_on_invalid_length_number(digits, number)

    def test_12_length_number(self):
        digits = '111111111111'
        number = '111111111111'
        check_on_invalid_length_number(digits, number)

    def test_more_than_12_length_number(self):
        digits = '111111111111111'
        number = '111111111111111'
        with self.assertRaises(InvalidLengthNumberException):
            check_on_invalid_length_number(digits, number)

    def test_valid_length_number(self):
        digits = '1111111111'
        number = '1111111111'
        check_on_invalid_length_number(digits, number)

    def test_not_str_digits(self):
        digits = 111111111111111
        number = '111111111111111'
        with self.assertRaises(TypeError):
            check_on_invalid_length_number(digits, number)

    def test_not_str_number(self):
        digits = '11111111111111'
        number = 111111111111111
        with self.assertRaises(InvalidLengthNumberException):
            check_on_invalid_length_number(digits, number)
