import tkinter as tk
from tkinter.messagebox import askyesno


def successfully_favorites(first_name, last_name):
    if last_name == "":
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name}\" was added to the Favorites successfully!")
        print(f"\"{first_name}\" was added to the Favorites successfully!\n")
    else:
        print(f"\"{first_name} {last_name}\" was added to the Favorites successfully!\n")
        tk.messagebox.showinfo(
            title='Update Contact Book',
            message=f'"{first_name} {last_name}" was added to the Favorites successfully!')