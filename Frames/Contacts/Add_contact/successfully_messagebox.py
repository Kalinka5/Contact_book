import tkinter as tk
from tkinter import messagebox


def successfully_messagebox(first_name: str, last_name: str) -> None:
    """
    Notify user that the adding of a new contact has been successfully
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :return: None
    """
    if last_name == "":
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name}\" was successfully added.")
        print(f"\"{first_name}\" was successfully added to your Contact Book.\n")

    else:
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name} {last_name}\" was successfully added.")
        print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")