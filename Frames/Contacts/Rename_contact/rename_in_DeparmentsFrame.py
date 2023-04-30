import tkinter as tk

from Frames.Departments.departments import DepartmentsFrame as Depart
from contact_book import Contact


def rename_in_departments_frame(contact_book, tree, old_first_name, old_last_name, new_first_name, new_last_name):
    dep_user = None
    for n, user in enumerate(contact_book.contacts):
        if old_first_name == user.first_name:
            dep_user = user.department

    found_id = None
    for item in tree.get_children(Depart.dict_departments[dep_user]):
        if tree.item(item, 'text') == f"{old_first_name} {old_last_name}":
            found_id = item
            break

    tree.delete(found_id)

    tree.insert('', tk.END, text=f'{new_first_name} {new_last_name}', iid=str(Contact.iid), open=False)
    tree.move(str(Contact.iid), Depart.dict_departments[dep_user], 0)
    Contact.iid += 1
