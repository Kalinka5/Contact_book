from Frames.Departments.departments import DepartmentsFrame as Depart


def delete_in_departments_frame(tree, contact_dep, first_name, last_name):
    found_id = None
    # Search for the row with contact name in the contact's department column
    for item in tree.get_children(Depart.dict_departments[contact_dep]):
        if tree.item(item, 'text') == f"{first_name} {last_name}":
            found_id = item
            break

    tree.delete(found_id)
