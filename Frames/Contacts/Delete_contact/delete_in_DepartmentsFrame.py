from tkinter import ttk

from Frames.Departments.departments import DepartmentsFrame as Depart


def delete_in_departments_frame(departments_tree: ttk.Treeview,
                                department: str, first_name: str, last_name: str) -> None:
    """Delete contact from the treeview of DepartmentsFrame"""

    found_id = None
    # Search for the row with contact name in the contact's department column
    for item in departments_tree.get_children(Depart.dict_departments[department]):
        if departments_tree.item(item, 'text') == f"{first_name} {last_name}":
            found_id = item
            break

    departments_tree.delete(found_id)
