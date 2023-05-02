import tkinter as tk

from Frames.Departments.departments import DepartmentsFrame as Depart
from contact_book import Contact


def rename_in_departments_frame(contact_book, tree, new_first_name):
    dep_user = None
    for n, user in enumerate(contact_book.contacts):
        if new_first_name == user.first_name:
            dep_user = user.department
            break

    children = tree.get_children(Depart.dict_departments[dep_user])
    tree.delete(*children)

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
