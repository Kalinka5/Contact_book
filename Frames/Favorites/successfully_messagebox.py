from tkinter import messagebox


def successfully_messagebox(first_name, last_name):

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