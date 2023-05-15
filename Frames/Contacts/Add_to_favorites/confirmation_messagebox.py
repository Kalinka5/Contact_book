from tkinter.messagebox import askyesno

from Contact_book.contact import Contact


def confirmation_favorites(contact: Contact) -> askyesno:
    """Print confirmation messagebox of adding contact to a Favorites"""

    if contact.last_name:
        full_name = f"{contact.first_name} {contact.last_name}"
    else:
        full_name = contact.first_name

    answer = askyesno(
        title='Confirmation',
        message=f'Are you sure that you want to add \"{full_name}\" to the Favorites?')

    return answer
