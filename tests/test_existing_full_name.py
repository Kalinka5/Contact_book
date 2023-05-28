import unittest

from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact
from Exceptions.validity_checks import check_on_existing_name
from Exceptions.exist_contact import NameExistException


class TestExistingFullName(unittest.TestCase):

    def setUp(self) -> None:
        self.contact_book = ContactBook()
        self.contact_book.add_contact(Contact("Test1", "User1", "111111"))
        self.contact_book.add_contact(Contact("Mr/Mrs", "User2", "222222"))
        self.contact_book.add_contact(Contact("User3", "", "333333"))

    def test_exist_only_first_name(self):
        first_name = 'Test1'
        last_name = ''
        check_on_existing_name(self.contact_book, first_name, last_name)

    def test_exist_only_last_name(self):
        first_name = ''
        last_name = 'User2'
        check_on_existing_name(self.contact_book, first_name, last_name)

    def test_exist_full_name(self):
        first_name = 'User3'
        last_name = ''
        with self.assertRaises(NameExistException):
            check_on_existing_name(self.contact_book, first_name, last_name)

    def test_names_different_contacts(self):
        first_name = 'Test1'
        last_name = 'User2'
        check_on_existing_name(self.contact_book, first_name, last_name)

    def test_first_name_with_space(self):
        first_name = 'User3 '
        last_name = ''
        check_on_existing_name(self.contact_book, first_name, last_name)

    def test_not_exist_name_in_contact_book(self):
        first_name = 'Tom'
        last_name = 'Hardy'
        check_on_existing_name(self.contact_book, first_name, last_name)
