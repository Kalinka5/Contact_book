from tkinter import messagebox


def successfully_messagebox(old_first_name: str, old_last_name: str, new_first_name: str, new_last_name: str) -> None:
    """Notify user that the editing of a contact has been successfully"""

    if old_last_name == "" and new_last_name == "":
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!")
        print(f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!\n")
    elif old_last_name == "":
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!")
        print(f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!\n")
    elif new_last_name == "":
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!")
        print(f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!\n")
    else:
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name} {old_last_name}\" was renamed to "
                    f"\"{new_first_name} {new_last_name}\" successfully!")
        print(f"\"{old_first_name} {old_last_name}\" was renamed to "
              f"\"{new_first_name} {new_last_name}\" successfully!\n")
