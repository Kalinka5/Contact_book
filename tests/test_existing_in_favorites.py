import unittest

from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook

from Exceptions.exist_contact import ContactExistInFavoritesException
from Exceptions.validity_checks import check_on_existing_in_favorites


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

    def test_method_str_with_fullname(self):
        exception = ContactExistInFavoritesException('Tom', 'Hardy')
        result = 'A contact \"Tom Hardy\" is already in the Favorites!'
        self.assertEqual(exception.__str__(), result)

    def test_method_str_with_only_firstname(self):
        exception = ContactExistInFavoritesException('Tom', '')
        result = 'A contact \"Tom\" is already in the Favorites!'
        self.assertEqual(exception.__str__(), result)
