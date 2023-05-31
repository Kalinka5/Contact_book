import unittest

from Contact_book.contact import Contact


class TestContact(unittest.TestCase):

    def test_create_contact_with_usual_parameters(self):
        contact = Contact('Tom', 'Hardy', '111111')
        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.first_name, 'Tom')
        self.assertEqual(contact.last_name, 'Hardy')
        self.assertEqual(contact.phone_number, '111111')
        self.assertEqual(contact.department, '')
        self.assertFalse(contact.favorites)

    def test_create_contact_with_all_parameters(self):
        contact = Contact('Tom', 'Hardy', '111111', 'Stars', True)
        self.assertIsInstance(contact, Contact)
        self.assertEqual(contact.first_name, 'Tom')
        self.assertEqual(contact.last_name, 'Hardy')
        self.assertEqual(contact.phone_number, '111111')
        self.assertEqual(contact.department, 'Stars')
        self.assertTrue(contact.favorites)

    def test_convert_lastname_none_to_empty_string(self):
        contact = Contact('Tom', None, '111111')
        self.assertEqual(contact.last_name, '')

    def test_less_than_contacts(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Hugh', 'Jackman', '222222')
        self.assertLess(contact2, contact1)

    def test_compare_not_implemented_classes(self):
        contact = Contact('Tom', 'Hardy', '111111')
        result = contact.__eq__("Not a Contact object")
        self.assertEqual(result, NotImplemented)

    def test_first_contact_equals_second_contact(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Tom', 'Hardy', '111111')
        result = contact1 == contact2
        self.assertTrue(result)

    def test_first_contact_not_equals_second_contact(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Hugh', 'Jackman', '222222')
        result = contact1 == contact2
        self.assertFalse(result)

    def test_first_names_not_equals(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Hugh', 'Hardy', '111111')
        result = contact1 == contact2
        self.assertFalse(result)

    def test_last_names_not_equals(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Tom', 'Jackman', '111111')
        result = contact1 == contact2
        self.assertFalse(result)

    def test_phone_number_not_equals(self):
        contact1 = Contact('Tom', 'Hardy', '111111')
        contact2 = Contact('Tom', 'Hardy', '222222')
        result = contact1 == contact2
        self.assertFalse(result)
