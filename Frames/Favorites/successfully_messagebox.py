from tkinter import messagebox


def successfully_messagebox(first_name: str, last_name: str) -> None:
    """messagebox to notify user that the contact has been deleted from Favorites successfully"""

    if last_name == "":
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{first_name}\" was deleted from the Favorites successfully!")
        print(f"Deleting \"{first_name}\" from the Favorites was successfully!\n")
    else:
        messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{first_name} {last_name}\" was deleted from the Favorites successfully!")
        print(f"Deleting \"{first_name} {last_name}\" from the Favorites was successfully!\n")
