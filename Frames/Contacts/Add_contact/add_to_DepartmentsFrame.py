import tkinter as tk
from tkinter import ttk

from contact_book import Contact, ContactBook
from Frames.Departments.departments import DepartmentsFrame as Depart


def add_to_departments_frame(departments_tree: ttk.Treeview, contact_book: ContactBook, department: str) -> None:
    """
    Add contact to treeview of DepartmentsFrame
    :param departments_tree: treeview of DepartmentsFrame
    :param contact_book: object of ContactBook
    :param department: contact's department (Work, Classmates, Friends, Relatives, Stars)
    :return: None
    """

    # delete all contacts in current departments(dep_user)
    children = departments_tree.get_children(Depart.dict_departments[department])
    departments_tree.delete(*children)

    # Add all contacts, also with new firstname and lastname in current departments(dep_user)
    amount_all_contacts = len(contact_book)
    for human in contact_book:
        if human.department == department:
            departments_tree.insert('',
                                    tk.END,
                                    text=f'{human.first_name} {human.last_name}',
                                    iid=str(Contact.iid),
                                    open=False)
            departments_tree.move(str(Contact.iid),
                                  Depart.dict_departments[department],
                                  amount_all_contacts)
            Contact.iid += 1
