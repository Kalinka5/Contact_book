from tkinter import ttk

from Contact_book.contact import Contact


def add_to_favorites_tree(favorites_tree: ttk.Treeview, contact: Contact) -> None:
    """
    Add contact into treeview of FavoritesFrame
    :param favorites_tree: the treeview of FavoritesFrame
    :param contact: object of class Contact
    :return: None
    """

    # find contact's index to insert it in alphabetical order
    index = 0
    while index < len(favorites_tree.get_children()):
        favorites_name = favorites_tree.item(favorites_tree.get_children()[index])['values'][1]
        if contact.first_name.lower() < favorites_name.lower():
            break
        index += 1

    favorites_tree.insert('',
                          index,
                          values=("♥", contact.first_name, contact.last_name, contact.phone_number))
