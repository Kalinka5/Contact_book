from tkinter import ttk


def add_to_contacts_frame(contacts_tree: ttk.Treeview, first_name: str, last_name: str, normal_number: str) -> None:
    """
    Add new contact into treeview of ContactsFrame
    :param contacts_tree: the treeview of ContactsFrame
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param normal_number: contact's phone number
    :return: None
    """

    # find contact's index to insert it in alphabetical order
    index = 0
    while index < len(contacts_tree.get_children()):
        if first_name.lower() < contacts_tree.item(contacts_tree.get_children()[index])['values'][0].lower():
            break
        index += 1

    contacts_tree.insert('',
                         index,
                         values=(" ", first_name, last_name, normal_number))
