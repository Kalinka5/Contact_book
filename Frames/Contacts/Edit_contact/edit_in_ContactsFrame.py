from tkinter import ttk

from Contact_book.contact import Contact


def edit_in_contacts_frame(contacts_tree: ttk.Treeview, new_contact: Contact) -> None:
    """Change contact's firstname, lastname and phone number in treeview of ContactsFrame"""

    selected_item = contacts_tree.selection()[0]
    contacts_tree.set(selected_item, 1, new_contact.first_name)
    contacts_tree.set(selected_item, 2, new_contact.last_name)
    contacts_tree.set(selected_item, 3, new_contact.phone_number)
