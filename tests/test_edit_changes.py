import unittest

from Contact_book.contact import Contact

from Exceptions.no_changes import ContactHasNoChanged
from Exceptions.validity_checks import check_values_changes


class TestEditChanged(unittest.TestCase):

    def test_contacts_values_doesnt_changed(self):
        old_contact = Contact("Test", "User", "111111")
        new_contact = Contact("Test", "User", "111111")
        with self.assertRaises(ContactHasNoChanged):
            check_values_changes(old_contact, new_contact)

    def test_contacts_all_values_changed(self):
        old_contact = Contact("Test1", "User1", "111111")
        new_contact = Contact("Test2", "User2", "222222")
        check_values_changes(old_contact, new_contact)

    def test_contacts_first_name_values_changed(self):
        old_contact = Contact("Test1", "User", "111111")
        new_contact = Contact("Test2", "User", "111111")
        check_values_changes(old_contact, new_contact)

    def test_contacts_last_name_values_changed(self):
        old_contact = Contact("Test", "User1", "111111")
        new_contact = Contact("Test", "User2", "111111")
        check_values_changes(old_contact, new_contact)

    def test_contacts_number_values_changed(self):
        old_contact = Contact("Test", "User", "111111")
        new_contact = Contact("Test", "User", "222222")
        check_values_changes(old_contact, new_contact)

    def test_method_str(self):
        exception = ContactHasNoChanged()
        result = 'The contact has not been changed!'
        self.assertEqual(exception.__str__(), result)
