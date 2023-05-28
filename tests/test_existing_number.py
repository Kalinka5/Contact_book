import unittest

from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact
from Exceptions.validity_checks import check_on_existing_number
from Exceptions.exist_contact import NumberExistException


class TestExistingNumber(unittest.TestCase):

    def setUp(self) -> None:
        self.contact_book = ContactBook()
        self.contact_book.add_contact(Contact("user1", "", "111111"))
        self.contact_book.add_contact(Contact("user2", "", "222222"))
        self.contact_book.add_contact(Contact("user3", "", "333333"))

    def test_number_exist_in_contact_book(self):
        normal_number = "111111"
        with self.assertRaises(NumberExistException):
            check_on_existing_number(self.contact_book, normal_number)

    def test_number_doesnt_exist_in_contact_book(self):
        normal_number = "444444"
        check_on_existing_number(self.contact_book, normal_number)
