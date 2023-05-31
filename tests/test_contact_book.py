import unittest

from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook


class TestContactBook(unittest.TestCase):

    def setUp(self) -> None:
        self.contact_book = ContactBook()

    def test_get_secure_attribute_contacts(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.__contacts = [contact]
        self.assertNotIn(contact, self.contact_book)

    def test_method_get_contacts(self):
        result = self.contact_book.get_contacts
        self.assertEqual(result, [])

    def test_method_add_contact(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        self.assertIn(contact, self.contact_book)

    def test_method_delete_contact(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        self.contact_book.delete_contact(contact)
        self.assertEqual(self.contact_book.get_contacts, [])

    def test_method_edit_contact(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        self.contact_book.edit_contact(contact, 'Hugh', 'Jackman', '222222')
        self.assertEqual(contact.first_name, 'Hugh')
        self.assertEqual(contact.last_name, 'Jackman')
        self.assertEqual(contact.phone_number, '222222')

    def test_method_get_contact_by_phone_number(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        search_contact = self.contact_book.get_contact_by_phone_number('111111')
        self.assertIs(contact, search_contact)

    def test_method_get_contact_by_nonexistent_phone_number(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        with self.assertRaises(TypeError):
            self.contact_book.get_contact_by_phone_number('222222')

    def test_method_len_contact_book(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Hugh', 'Jackman', '222222')
        self.contact_book.add_contact(contact1)
        self.contact_book.add_contact(contact2)
        length_contact_book = len(self.contact_book)
        self.assertEqual(length_contact_book, 2)

    def test_method_str(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.contact_book.add_contact(contact)
        result = 'Your Contact Book:\n\nTom           Hardy         111111\n'
        self.assertEqual(self.contact_book.__str__(), result)

    def test_method_str_without_contacts(self):
        result = 'Your Contact Book:\n\n'
        self.assertEqual(self.contact_book.__str__(), result)

    def test_method_str_without_contacts_last_name(self):
        contact = Contact('Tom', '', '111111')
        self.contact_book.add_contact(contact)
        result = 'Your Contact Book:\n\nTom                         111111\n'
        self.assertEqual(self.contact_book.__str__(), result)
