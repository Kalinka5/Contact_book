from tkinter import ttk

from contact_book import Contact


def add_to_contacts_frame(contacts_tree: ttk.Treeview, new_contact: Contact, heart="") -> None:
    """
    Add new contact into treeview of ContactsFrame
    :param contacts_tree: the treeview of ContactsFrame
    :param new_contact: object of class Contact
    :param heart: is contact in favorites or not
    :return: None
    """

    # find contact's index to insert it in alphabetical order
    index = 0
    while index < len(contacts_tree.get_children()):
        first_name = contacts_tree.item(contacts_tree.get_children()[index])['values'][1]
        if new_contact.first_name.lower() < first_name.lower():
            break
        index += 1

    contacts_tree.insert('',
                         index,
                         values=(heart, new_contact.first_name, new_contact.last_name, new_contact.phone_number))
