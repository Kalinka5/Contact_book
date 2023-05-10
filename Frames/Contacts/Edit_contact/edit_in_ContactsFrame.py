from tkinter import ttk

from contact_book import Contact
from Frames.Contacts.Delete_contact.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Contacts.Add_contact.add_to_ContactsFrame import add_to_contacts_frame


def edit_in_contacts_frame(contacts_tree: ttk.Treeview, new_contact: Contact, heart: str) -> None:
    """Change contact's firstname, lastname and phone number in treeview of ContactsFrame"""

    delete_in_contacts_frame(contacts_tree)
    add_to_contacts_frame(contacts_tree, new_contact.first_name, new_contact.last_name, new_contact.phone_number, heart)
