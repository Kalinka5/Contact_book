from tkinter import ttk


def rename_in_contacts_frame(contacts_txt: ttk.Treeview, new_first_name: str, new_last_name: str, number: str) -> None:
    """Change contact's firstname and lastname in treeview of ContactsFrame"""

    # delete contact from treeview of ContactsFrame
    selected_item = contacts_txt.selection()[0]
    contacts_txt.delete(selected_item)

    # find contact's index to insert it in alphabetical order
    index = 0
    while index < len(contacts_txt.get_children()):
        if new_first_name.lower() < contacts_txt.item(contacts_txt.get_children()[index])['values'][0].lower():
            break
        index += 1

    contacts_txt.insert('',
                        index,
                        values=(new_first_name, new_last_name, number))
