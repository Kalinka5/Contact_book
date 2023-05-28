from tkinter import messagebox

from Contact_book.contact import Contact


def successfully_messagebox(contact: Contact) -> None:
    """messagebox to notify user that the contact has been deleted successfully"""

    if contact.last_name:
        full_name = f"{contact.first_name} {contact.last_name}"
    else:
        full_name = contact.first_name

    messagebox.showinfo(title='Update Contact Book',
                        message=f"\"{full_name}\" was successfully deleted.")
    print(f"Deleting \"{full_name}\" from your Contact Book was successfully.\n")
