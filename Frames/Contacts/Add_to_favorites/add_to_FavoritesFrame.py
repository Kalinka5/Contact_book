from tkinter import ttk

from Frames.Favorites.favorites import FavoritesFrame


def add_to_favorites_frame(favorites_tree: ttk.Treeview, first_name: str, last_name: str, number: str) -> None:
    """
    Add contact into treeview of FavoritesFrame
    :param favorites_tree: the treeview of FavoritesFrame
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param number: contact's phone number
    :return: None
    """

    emoji = FavoritesFrame.emoji  # emoji in firstname in Favorites contacts

    # find contact's index to insert it in alphabetical order
    index = 0
    while index < len(favorites_tree.get_children()):
        favorites_name = favorites_tree.item(favorites_tree.get_children()[index])['values'][0]
        if f"{emoji}{first_name.lower()}" < favorites_name.lower():
            break
        index += 1

    favorites_tree.insert('',
                          index,
                          values=(f"{emoji}{first_name}", last_name, number))
