from tkinter import ttk


def add_to_contacts_frame(contacts_txt: ttk.Treeview, first_name: str, last_name: str, normal_number: str) -> None:
    """
    Add new contact into treeview of ContactsFrame
    :param contacts_txt: the treeview of ContactsFrame
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param normal_number: contact's phone number
    :return: None
    """

    # Get index of contact where he is in contact book by alphabet
    index = 0
    while index < len(contacts_txt.get_children()):
        if first_name.lower() < contacts_txt.item(contacts_txt.get_children()[index])['values'][0].lower():
            break
        index += 1

    contacts_txt.insert('',
                        index,
                        values=(first_name, last_name, normal_number))
