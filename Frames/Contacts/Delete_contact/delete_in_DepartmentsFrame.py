from tkinter import ttk

from Contact_book.contact import Contact
from Frames.Departments.departments import DepartmentsFrame as Depart


def delete_in_departments_frame(departments_tree: ttk.Treeview, contact: Contact) -> None:
    """Delete contact from the treeview of DepartmentsFrame"""

    found_id = None
    # Search the row of certain contact with his fullname in the contact's department column
    for item in departments_tree.get_children(Depart.dict_departments[contact.department]):
        if departments_tree.item(item, 'text') == f"{contact.first_name} {contact.last_name}":
            found_id = item
            break

    departments_tree.delete(found_id)
