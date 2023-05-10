from tkinter import ttk

from contact_book import Contact
from Frames.Contacts.Delete_contact.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Contacts.Add_to_favorites.add_to_FavoritesFrame import add_to_favorites_frame


def edit_in_favorites_frame(favorites_tree: ttk.Treeview, old_phone_number: str,
                            new_contact: Contact) -> None:
    """Change contact's firstname, lastname and phone number in treeview of FavoritesFrame"""

    delete_in_favorites_frame(favorites_tree, old_phone_number)
    add_to_favorites_frame(favorites_tree, new_contact.first_name, new_contact.last_name, new_contact.phone_number)
