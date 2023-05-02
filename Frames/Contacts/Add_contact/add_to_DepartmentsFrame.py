import tkinter as tk
from tkinter import ttk

from contact_book import Contact, ContactBook
from Frames.Departments.departments import DepartmentsFrame as Depart


def add_to_departments_frame(tree: ttk.Treeview, contact_book: ContactBook, department: str) -> None:
    """
    Add contact to treeview of DepartmentsFrame
    :param tree: treeview of DepartmentsFrame
    :param contact_book: object of ContactBook
    :param department: contact's department (Work, Classmates, Friends, Relatives, Stars)
    :return: None
    """

    children = tree.get_children(Depart.dict_departments[department])
    tree.delete(*children)

    amount_all_contacts = len(contact_book)
    for human in contact_book:
        if human.department == department:
            tree.insert('',
                        tk.END,
                        text=f'{human.first_name} {human.last_name}',
                        iid=str(Contact.iid),
                        open=False)
            tree.move(str(Contact.iid),
                      Depart.dict_departments[department],
                      amount_all_contacts)
            Contact.iid += 1
