import tkinter as tk
from tkinter import ttk

from Frames.Departments.departments import DepartmentsFrame as Depart
from contact_book import Contact, ContactBook


def rename_in_departments_frame(contact_book: ContactBook, tree: ttk.Treeview, new_first_name: str) -> None:
    """Change contact's firstname and lastname in treeview of DepartmentsFrame"""

    # find contact's departments value
    dep_user = None
    for n, user in enumerate(contact_book.contacts):
        if new_first_name == user.first_name:
            dep_user = user.department
            break

    # delete all contacts in current departments(dep_user)
    children = tree.get_children(Depart.dict_departments[dep_user])
    tree.delete(*children)

    # Add all contacts, also with new firstname and lastname in current departments(dep_user)
    amount_all_contacts = len(contact_book)
    for human in contact_book:
        if human.department == dep_user:
            tree.insert('',
                        tk.END,
                        text=f'{human.first_name} {human.last_name}',
                        iid=str(Contact.iid),
                        open=False)
            tree.move(str(Contact.iid),
                      Depart.dict_departments[dep_user],
                      amount_all_contacts)
            Contact.iid += 1
