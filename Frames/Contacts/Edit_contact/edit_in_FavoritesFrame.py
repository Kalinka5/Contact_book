from tkinter import ttk

from Frames.Contacts.Delete_contact.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Contacts.Add_to_favorites.add_to_FavoritesFrame import add_to_favorites_frame


def edit_in_favorites_frame(favorites_tree: ttk.Treeview, old_first_name: str,
                            new_first_name: str, new_last_name: str, number: str) -> None:
    """Change contact's firstname, lastname and phone number in treeview of FavoritesFrame"""

    delete_in_favorites_frame(favorites_tree, old_first_name)
    add_to_favorites_frame(favorites_tree, new_first_name, new_last_name, number)
