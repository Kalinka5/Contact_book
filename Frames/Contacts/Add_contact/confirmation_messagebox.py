from tkinter.messagebox import askyesno

from contact_book import Contact


def confirmation_messagebox(new_contact: Contact) -> askyesno:
    """Print confirmation messagebox to rename contact"""

    if new_contact.last_name:
        full_name = f"{new_contact.first_name} {new_contact.last_name}"
    else:
        full_name = new_contact.first_name

    answer = askyesno(title='Confirmation',
                      message=f'Are you sure that you want to add contact \"{full_name}\"?')

    return answer
