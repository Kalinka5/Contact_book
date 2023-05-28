import unittest

from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact
from Exceptions.validity_checks import check_on_existing_in_favorites
from Exceptions.exist_contact import ContactExistInFavoritesException


class TestContactExistInFavorites(unittest.TestCase):

    def setUp(self) -> None:
        self.contact_book = ContactBook()
        self.contact_book.add_contact(Contact("Test1", "User1", "111111", favorites=True))
        self.contact_book.add_contact(Contact("Mr/Mrs", "User2", "222222", favorites=True))
        self.contact_book.add_contact(Contact("User3", "", "333333"))

    def test_contact_doesnt_exist_in_favorites(self):
        contact = Contact("User3", "", "333333")
        check_on_existing_in_favorites(self.contact_book, contact)

    def test_contact_exist_in_favorites(self):
        contact = Contact("Test1", "User1", "111111")
        with self.assertRaises(ContactExistInFavoritesException):
            check_on_existing_in_favorites(self.contact_book, contact)
