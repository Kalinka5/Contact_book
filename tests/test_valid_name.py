import unittest

from Exceptions.invalid_contact import InvalidNameException
from Exceptions.validity_checks import check_on_invalid_name


class TestValidName(unittest.TestCase):
    def test_first_name_length_less_than_1(self):
        first_name = ''
        last_name = 'Hardy'
        with self.assertRaises(InvalidNameException):
            check_on_invalid_name(first_name, last_name)

    def test_first_name_length_more_than_12(self):
        first_name = 'Aaaaaaaaaaaaa'
        last_name = 'Hardy'
        with self.assertRaises(InvalidNameException):
            check_on_invalid_name(first_name, last_name)

    def test_last_name_length_less_than_1(self):
        first_name = 'Tom'
        last_name = ''
        check_on_invalid_name(first_name, last_name)

    def test_last_name_length_more_than_12(self):
        first_name = 'Tom'
        last_name = 'Aaaaaaaaaaaaaaa'
        with self.assertRaises(InvalidNameException):
            check_on_invalid_name(first_name, last_name)

    def test_invalid_full_name(self):
        first_name = ''
        last_name = 'Aaaaaaaaaaaaaaa'
        with self.assertRaises(InvalidNameException):
            check_on_invalid_name(first_name, last_name)

    def test_valid_full_name(self):
        first_name = 'Tom'
        last_name = 'Hardy'
        check_on_invalid_name(first_name, last_name)
