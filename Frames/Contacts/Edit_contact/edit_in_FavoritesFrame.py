from tkinter import ttk

from Contact_book.contact import Contact


def edit_in_favorites_frame(favorites_tree: ttk.Treeview, old_phone_number: str, new_contact: Contact) -> None:
    """Change contact's firstname, lastname and phone number in treeview of FavoritesFrame"""

    # find contact's id in treeview of FavoritesFrame
    item_id = None
    for child in favorites_tree.get_children():
        if favorites_tree.set(child, "number") == old_phone_number:
            item_id = child
            break

    if item_id is not None:
        favorites_tree.set(item_id, 1, new_contact.first_name)
        favorites_tree.set(item_id, 2, new_contact.last_name)
        favorites_tree.set(item_id, 3, new_contact.phone_number)
