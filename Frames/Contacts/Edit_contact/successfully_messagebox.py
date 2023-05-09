from tkinter import messagebox


def successfully_messagebox(new_first_name: str, new_last_name: str) -> None:
    """Notify user that the editing of a contact has been successfully"""

    if new_last_name:
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"The contact \"{new_first_name} {new_last_name}\" was edited successfully!")
        print(f"The contact \"{new_first_name} {new_last_name}\" was edited successfully!\n")
    else:
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"The contact \"{new_first_name}\" was edited successfully!")
        print(f"The contact \"{new_first_name}\" was edited successfully!\n")
