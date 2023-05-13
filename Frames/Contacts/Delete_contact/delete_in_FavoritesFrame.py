from tkinter import ttk


def delete_in_favorites_frame(favorites_frame, favorites_tree: ttk.Treeview, phone_number: str) -> None:
    """
    Delete contact from the treeview of FavoritesFrame
    :param favorites_frame: object of the class FavoritesFrame
    :param favorites_tree: treeview of FavoritesFrame
    :param phone_number: contact's phone number
    :return: None
    """

    # find contact's id in treeview of FavoritesFrame
    item_id = favorites_frame.get_contact_id_by_phone_number(phone_number)

    if item_id is not None:
        favorites_tree.delete(item_id)
