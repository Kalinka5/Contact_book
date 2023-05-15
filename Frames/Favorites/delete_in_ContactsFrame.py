from tkinter import ttk


def delete_in_contacts_frame(contacts_tree: ttk.Treeview, phone_number: str) -> None:
    """
    Delete ♥ in the first column of Contacts tree
    :param contacts_tree: treeview of ContactsFrame
    :param phone_number: contact's phone number
    :return: None
    """

    # find contact's id in the treeview of ContactsFrame
    item_id = None
    for child in contacts_tree.get_children():
        if contacts_tree.set(child, "number") == phone_number:
            item_id = child
            break

    if item_id is not None:
        contacts_tree.set(item_id, 0, "")
