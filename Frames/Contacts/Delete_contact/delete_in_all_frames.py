from tkinter import ttk

from Contact_book.contact_book import ContactBook
from data_base import DataBase
from Frames.Contacts.Delete_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Delete_contact.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Contacts.Delete_contact.delete_in_DepartmentsFrame import delete_in_departments_frame
from Frames.Contacts.Delete_contact.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Contacts.Delete_contact.successfully_messagebox import successfully_messagebox


def delete_contact_in_all_frames(favorites_frame, contact_book: ContactBook, data_base: DataBase,
                                 contacts_tree: ttk.Treeview, departments_tree: ttk.Treeview,
                                 favorites_tree: ttk.Treeview):

    human = contacts_tree.item(contacts_tree.focus())['values']
    phone_number = human[3]

    contact = contact_book.get_contact_by_phone_number(phone_number)

    # print confirmation messagebox "Are you sure that you want to delete contact?"
    answer = confirmation_messagebox(contact)

    if answer:
        # Delete contact in ContactsFrame
        delete_in_contacts_frame(contacts_tree)

        # Delete contact in DepartmentsFrame
        delete_in_departments_frame(departments_tree, contact)

        # Delete contact in FavoritesFrame
        delete_in_favorites_frame(favorites_frame, favorites_tree, contact.phone_number)

        # Delete contact in the class Contact book
        contact_book.delete_contact(contact)

        # Delete contact from database
        data_base.delete_contact(phone_number)

        # notify user that the contact has been deleted successfully
        successfully_messagebox(contact)
