from tkinter import ttk


def delete_in_contacts_frame(contacts_tree: ttk.Treeview) -> None:
    """Delete contact from the treeview of ContactsFrame"""

    selected_item = contacts_tree.selection()[0]
    contacts_tree.delete(selected_item)
