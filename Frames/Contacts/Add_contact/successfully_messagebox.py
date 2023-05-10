import tkinter as tk
from tkinter import messagebox

from contact import Contact


def successfully_messagebox(new_contact: Contact) -> None:
    """Notify user that the adding of a new contact has been successfully"""

    if new_contact.last_name == "":
        full_name = f"{new_contact.first_name} {new_contact.last_name}"
    else:
        full_name = new_contact.first_name

    tk.messagebox.showinfo(title='Update Contact Book',
                           message=f"\"{full_name}\" was successfully added.")
    print(f"\"{full_name}\" was successfully added to your Contact Book.\n")
