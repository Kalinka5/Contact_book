from tkinter import messagebox

from Contact_book.contact import Contact


def successfully_messagebox(new_contact: Contact) -> None:
    """Notify user that the editing of a contact has been successfully"""

    if new_contact.last_name:
        full_name = f"{new_contact.first_name} {new_contact.last_name}"
    else:
        full_name = new_contact.first_name

    messagebox.showinfo(title='Update Contact Book',
                        message=f"The contact \"{full_name}\" was edited successfully!")
    print(f"The contact \"{full_name}\" was edited successfully!\n")
