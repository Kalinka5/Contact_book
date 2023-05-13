from tkinter import messagebox

from Contact_book.contact import Contact


def successfully_favorites(contact: Contact) -> None:
    """messagebox to notify user that the contact has been added to Favorites successfully"""

    if contact.last_name:
        full_name = f"{contact.first_name} {contact.last_name}"
    else:
        full_name = contact.first_name

    messagebox.showinfo(title='Update Contact Book',
                        message=f"\"{full_name}\" was added to the Favorites successfully!")
    print(f"\"{full_name}\" was added to the Favorites successfully!\n")
