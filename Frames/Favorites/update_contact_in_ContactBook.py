from contact_book import ContactBook


def update_contact_in_contact_book(contact_book: ContactBook, phone_number: str):
    """
    Update contact with favorites to False in the ContactBook
    :param contact_book: object of ContactBook
    :param phone_number: contact's phone number
    :return:
    """

    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if phone_number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact.favorites = "False"
