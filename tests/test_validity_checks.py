import unittest

from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook

from Exceptions.no_changes import ContactHasNoChanged
from Exceptions.validity_checks import validity_checks


class TestValidityChecks(unittest.TestCase):

    def test_with_old_contact(self):
        digits = '111111'
        number = '111-111'
        contact_book = ContactBook()
        new_contact = Contact('Tom', 'Hardy', '111111')
        old_contact = Contact('Hugh', 'Jackman', '222222')
        validity_checks(digits, number, contact_book, new_contact, old_contact)

    def test_without_old_contact(self):
        digits = '111111'
        number = '111-111'
        contact_book = ContactBook()
        new_contact = Contact('Tom', 'Hardy', '111111')
        validity_checks(digits, number, contact_book, new_contact)

    def test_with_old_contact_equal_to_new_contact(self):
        digits = '111111'
        number = '111-111'
        contact_book = ContactBook()
        new_contact = Contact('Tom', 'Hardy', '111111')
        old_contact = Contact('Tom', 'Hardy', '111111')
        with self.assertRaises(ContactHasNoChanged):
            validity_checks(digits, number, contact_book, new_contact, old_contact)

    def test_with_old_contact_full_names_equals(self):
        digits = '111111'
        number = '111-111'
        contact_book = ContactBook()
        new_contact = Contact('Tom', 'Hardy', '111111')
        old_contact = Contact('Tom', 'Hardy', '222222')
        validity_checks(digits, number, contact_book, new_contact, old_contact)

    def test_with_old_contact_phone_numbers_equals(self):
        digits = '111111'
        number = '111-111'
        contact_book = ContactBook()
        new_contact = Contact('Tom', 'Hardy', '111111')
        old_contact = Contact('Hugh', 'Jackman', '111111')
        validity_checks(digits, number, contact_book, new_contact, old_contact)
