import unittest

from Exceptions.invalid_contact import InvalidNumberException
from Exceptions.validity_checks import check_on_invalid_number


class TestValidNumber(unittest.TestCase):
    def test_digits_with_letters(self):
        digits = '123456a'
        new_phone_number = '123456a'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_only_letters(self):
        digits = 'aaaaaa'
        new_phone_number = 'aaaaaa'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_with_brackets(self):
        digits = '(111)111'
        new_phone_number = '(111)111'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_with_dashes(self):
        digits = '111-111'
        new_phone_number = '111-111'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_with_plus_symbol(self):
        digits = '+111111'
        new_phone_number = '+111111'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_float_type(self):
        digits = '111.111'
        new_phone_number = '111.111'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_with_double_quotes(self):
        digits = '"111111"'
        new_phone_number = '"111111"'
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_digits_with_single_quotes(self):
        digits = "'111111'"
        new_phone_number = "'111111'"
        with self.assertRaises(InvalidNumberException):
            check_on_invalid_number(digits, new_phone_number)

    def test_valid_digits(self):
        digits = '111111'
        new_phone_number = '111111'
        check_on_invalid_number(digits, new_phone_number)

    def test_method_str(self):
        exception = InvalidNumberException('123abc')
        result = "Invalid value of phone number: \"123abc\".\n" \
                 "Number should contain only integers and dashes.\n" \
                 "Number example: \"0-(00)-000-0000\" or \"0000000000\".\n"
        self.assertEqual(exception.__str__(), result)
