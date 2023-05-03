from contact_book import ContactBook


def rename_in_contact_book(contact_book: ContactBook, new_first_name: str, new_last_name: str, number: str) -> None:
    """
    Change contact's firstname and lastname in the class ContactBook
    :param contact_book: object of the class ContactBook
    :param new_first_name: contact's new firstname
    :param new_last_name: contact's new lastname
    :param number: contact's new phone number
    :return: None
    """

    # search index of contact to delete him by his index
    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact_book.rename_contact(contact, new_first_name, new_last_name)
