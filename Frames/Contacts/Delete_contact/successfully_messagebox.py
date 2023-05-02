import tkinter as tk
from tkinter.messagebox import askyesno


def successfully_messagebox(first_name: str, last_name: str) -> None:
    """messagebox to notify user that the contact has been deleted successfully"""

    if last_name == "":
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name}\" was successfully deleted.")
        print(f"Deleting \"{first_name}\" from your Contact Book was successfully.\n")
    else:
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name} {last_name}\" was successfully deleted.")
        print(f"Deleting \"{first_name} {last_name}\" from your Contact Book was successfully.\n")