from contact_book import Contact, ContactBook


def add_to_contacts(contact_book: ContactBook, department: str,
                    first_name: str, last_name: str, normal_number: str) -> None:
    """
    Add new contact to class ContactBook
    :param contact_book: object of class ContactBook
    :param department: contact's department (Work, Classmates, Friends, Relatives, Stars)
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param normal_number: contact's phone number
    :return: None
    """

    contact = Contact(first_name, last_name, normal_number, department)
    contact_book.add_contact(contact)
