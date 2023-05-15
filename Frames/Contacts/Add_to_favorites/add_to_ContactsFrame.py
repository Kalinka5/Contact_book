from tkinter import ttk


def update_contacts_tree(contacts_tree: ttk.Treeview):
    """Add ♥ in the first column of Contacts tree"""

    selected_item = contacts_tree.selection()[0]
    contacts_tree.set(selected_item, 0, "♥")
