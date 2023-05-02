from tkinter import messagebox


def successfully_favorites(first_name: str, last_name: str) -> None:
    """messagebox to notify user that the contact has been deleted from Favorites successfully"""

    if last_name == "":
        messagebox.showinfo(title='Update Contact Book',
                            message=f"\"{first_name}\" was added to the Favorites successfully!")
        print(f"\"{first_name}\" was added to the Favorites successfully!\n")
    else:
        print(f"\"{first_name} {last_name}\" was added to the Favorites successfully!\n")
        messagebox.showinfo(title='Update Contact Book',
                            message=f'"{first_name} {last_name}" was added to the Favorites successfully!')
