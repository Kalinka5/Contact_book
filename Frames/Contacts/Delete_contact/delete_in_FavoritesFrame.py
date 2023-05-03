from tkinter import ttk


def delete_in_favorites_frame(favorites_tree: ttk.Treeview, first_name: str) -> None:
    """Delete contact from the treeview of FavoritesFrame"""

    # find contact's id in treeview of FavoritesFrame
    item_id = None
    for child in favorites_tree.get_children():
        if favorites_tree.set(child, "first_name")[3:] == first_name:
            item_id = child
            break

    if item_id is not None:
        favorites_tree.delete(item_id)
