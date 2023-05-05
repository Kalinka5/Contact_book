from contact_book import ContactBook


def edit_in_contact_book(contact_book: ContactBook, new_first_name: str, new_last_name: str,
                         new_phone_number: str, old_phone_number: str) -> None:
    """
    Change contact's firstname,lastname and phone number in the class ContactBook
    :param contact_book: object of the class ContactBook
    :param new_first_name: contact's new firstname
    :param new_last_name: contact's new lastname
    :param new_phone_number: contact's new phone number
    :param old_phone_number: contact's old phone number
    :return: None
    """

    # search index of contact to delete him by his index
    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if old_phone_number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact_book.edit_contact(contact, new_first_name, new_last_name, new_phone_number)
