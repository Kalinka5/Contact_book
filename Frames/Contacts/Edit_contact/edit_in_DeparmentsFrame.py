from tkinter import ttk

from Contact_book.contact_book import ContactBook
from Frames.Contacts.Add_contact.add_to_DepartmentsFrame import add_to_departments_frame


def edit_in_departments_frame(contact_book: ContactBook, departments_tree: ttk.Treeview, new_first_name: str) -> None:
    """Change contact's firstname, lastname and phone number in treeview of DepartmentsFrame"""

    # find contact's departments value
    dep_user = None
    for n, user in enumerate(contact_book.contacts):
        if new_first_name == user.first_name:
            dep_user = user.department
            break

    add_to_departments_frame(departments_tree, contact_book, dep_user)
