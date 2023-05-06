from tkinter import ttk

from Frames.Favorites.favorites import FavoritesFrame


def delete_in_favorites_frame(favorites_tree: ttk.Treeview, phone_number: str) -> None:
    """
    Delete contact from the treeview of FavoritesFrame
    :param favorites_tree: treeview of FavoritesFrame
    :param phone_number: contact's phone number
    :return: None
    """

    emoji = FavoritesFrame.emoji  # emoji in firstname in Favorites contacts
    # find contact's id in treeview of FavoritesFrame
    item_id = None
    for child in favorites_tree.get_children():
        if favorites_tree.set(child, "number") == phone_number:
            item_id = child
            break

    if item_id is not None:
        favorites_tree.delete(item_id)
