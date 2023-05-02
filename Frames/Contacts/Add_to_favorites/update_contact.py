from contact_book import ContactBook


def update_contact_favorites(contact_book: ContactBook, number: str) -> None:
    """Change contact's favorites value in the class ContactBook"""

    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact.favorites = "True"
