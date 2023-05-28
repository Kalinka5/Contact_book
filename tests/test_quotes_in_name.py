import unittest

from Exceptions.validity_checks import check_on_quotes_in_name
from Exceptions.invalid_contact import InvalidNameQuotesException


class TestQuotesInName(unittest.TestCase):
    def test_single_quotes_first_name(self):
        first_name = "'Tom'"
        last_name = "Hardy"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_single_quotes_last_name(self):
        first_name = "Tom"
        last_name = "'Hardy'"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_single_quotes_full_name(self):
        first_name = "'Tom'"
        last_name = "'Hardy'"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_double_quotes_first_name(self):
        first_name = '"Tom"'
        last_name = 'Hardy'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_double_quotes_last_name(self):
        first_name = 'Tom'
        last_name = '"Hardy"'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_double_quotes_full_name(self):
        first_name = '"Tom"'
        last_name = '"Hardy"'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_single_quote_first_name(self):
        first_name = "'"
        last_name = "Hardy"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_single_quote_last_name(self):
        first_name = "Tom"
        last_name = "'"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_single_quote_full_name(self):
        first_name = "'"
        last_name = "'"
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_double_quote_first_name(self):
        first_name = '"'
        last_name = 'Hardy'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_double_quote_last_name(self):
        first_name = 'Tom'
        last_name = '"'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_only_double_quote_full_name(self):
        first_name = '"'
        last_name = '"'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_with_double_and_single_quotes_first_name(self):
        first_name = '"\''
        last_name = 'Hardy'
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_with_double_and_single_quotes_last_name(self):
        first_name = 'Tom'
        last_name = '"\''
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_with_double_and_single_quotes_full_name(self):
        first_name = '"\''
        last_name = '"\''
        with self.assertRaises(InvalidNameQuotesException):
            check_on_quotes_in_name(first_name, last_name)

    def test_without_quotes(self):
        first_name = 'Tom'
        last_name = 'Hardy'
        check_on_quotes_in_name(first_name, last_name)
