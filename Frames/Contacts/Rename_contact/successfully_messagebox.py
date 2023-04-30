import tkinter as tk
from tkinter.messagebox import askyesno


def successfully_messagebox(old_first_name, old_last_name, new_first_name, new_last_name):
    if old_last_name == "" and new_last_name == "":
        tk.messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!")
        print(f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!\n")
    elif old_last_name == "":
        tk.messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!")
        print(f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!\n")
    elif new_last_name == "":
        tk.messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!")
        print(f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!\n")
    else:
        tk.messagebox.showinfo(
            title='Update Contact Book',
            message=f"\"{old_first_name} {old_last_name}\" was renamed to "
                    f"\"{new_first_name} {new_last_name}\" successfully!")
        print(f"\"{old_first_name} {old_last_name}\" was renamed to "
              f"\"{new_first_name} {new_last_name}\" successfully!\n")
