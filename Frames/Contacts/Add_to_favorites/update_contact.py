from Contact_book.contact_book import ContactBook


def update_contact_favorites(contact_book: ContactBook, phone_number: str) -> None:
    """Change contact's favorites value in the class ContactBook"""

    contact = contact_book.get_contact_by_phone_number(phone_number)
    contact.favorites = "True"
