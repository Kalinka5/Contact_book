from tkinter import ttk


def add_to_favorites_frame(favorites: ttk.Treeview, first_name: str, last_name: str, number: str) -> None:
    """
    Add contact into treeview of FavoritesFrame
    :param favorites: the treeview of FavoritesFrame
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param number: contact's phone number
    :return: None
    """

    index = 0
    while index < len(favorites.get_children()):
        favorites_name = favorites.item(favorites.get_children()[index])['values'][0].lower()
        if first_name.lower() < favorites_name[3:]:
            break
        index += 1

    favorites.insert('',
                     index,
                     values=(f"♥  {first_name}", last_name, number))
