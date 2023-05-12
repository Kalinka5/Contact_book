from Contact_book.contact_book import ContactBook


def delete_in_contact_book(contact_book: ContactBook, contact_index: int) -> None:
    """Delete contact from object of class ContactBook"""

    contact = contact_book.contacts[contact_index]
    contact_book.delete_contact(contact)
