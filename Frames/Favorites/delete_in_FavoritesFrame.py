from tkinter import ttk


def delete_in_favorites_frame(favorites_tree: ttk.Treeview) -> None:
    """
    Delete contact from the treeview of FavoritesFrame
    :param favorites_tree: treeview of FavoritesFrame
    :return: None
    """

    selected_item = favorites_tree.selection()[0]
    favorites_tree.delete(selected_item)
