from tkinter import ttk

from contact_book import ContactBook


def delete_in_favorites_frame(favorites_tree: ttk.Treeview, contact_book: ContactBook, first_name: str) -> None:
    """
    Delete contact from the treeview of FavoritesFrame
    :param favorites_tree: treeview of FavoritesFrame
    :param contact_book: object of ContactBook
    :param first_name: contact's firstname
    :return: None
    """

    selected_item = favorites_tree.selection()[0]
    favorites_tree.delete(selected_item)

    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if first_name == user.first_name:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact.favorites = "False"
