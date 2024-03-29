from tkinter.messagebox import askyesno

from Contact_book.contact import Contact


def confirmation_messagebox(new_contact: Contact) -> askyesno:
    """Print confirmation messagebox of renaming contact"""

    if new_contact.last_name:
        full_name = f"{new_contact.first_name} {new_contact.last_name}"
    else:
        full_name = new_contact.first_name

    answer = askyesno(title='Confirmation',
                      message=f'Are you sure that you want to edit contact \"{full_name}\"?')

    return answer
