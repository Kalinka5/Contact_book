from tkinter import ttk

from Frames.Contacts.Delete_contact.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Contacts.Add_contact.add_to_ContactsFrame import add_to_contacts_frame


def rename_in_contacts_frame(contacts_tree: ttk.Treeview, new_first_name: str, new_last_name: str, number: str) -> None:
    """Change contact's firstname and lastname in treeview of ContactsFrame"""

    delete_in_contacts_frame(contacts_tree)
    add_to_contacts_frame(contacts_tree, new_first_name, new_last_name, number)
