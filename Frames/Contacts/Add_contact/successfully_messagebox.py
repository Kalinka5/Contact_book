import tkinter as tk
from tkinter import messagebox


def successfully_messagebox(first_name: str, last_name: str) -> None:
    """Notify user that the adding of a new contact has been successfully"""
    if last_name == "":
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name}\" was successfully added.")
        print(f"\"{first_name}\" was successfully added to your Contact Book.\n")

    else:
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name} {last_name}\" was successfully added.")
        print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")