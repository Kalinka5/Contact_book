import tkinter as tk
from tkinter import messagebox


def successfully_messagebox(first_name, last_name):
    if last_name == "":
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name}\" was successfully added.")
        print(f"\"{first_name}\" was successfully added to your Contact Book.\n")
    else:
        # Show message box when add contact
        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{first_name} {last_name}\" was successfully added.")
        print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")