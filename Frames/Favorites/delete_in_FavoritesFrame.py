from tkinter import ttk

from contact_book import ContactBook


def delete_in_favorites_frame(favorites_tree: ttk.Treeview, contact_book: ContactBook, phone_number: str) -> None:
    """
    Delete contact from the treeview of FavoritesFrame
    :param favorites_tree: treeview of FavoritesFrame
    :param contact_book: object of ContactBook
    :param phone_number: contact's phone number
    :return: None
    """

    selected_item = favorites_tree.selection()[0]
    favorites_tree.delete(selected_item)

    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if phone_number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact.favorites = "False"
