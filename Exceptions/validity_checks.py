from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook

from Exceptions.exist_contact import ContactExistInFavoritesException, NameExistException, NumberExistException
from Exceptions.invalid_contact import InvalidLengthNumberException, InvalidNameException, InvalidNameQuotesException, \
    InvalidNumberException
from Exceptions.no_changes import ContactHasNoChanged


def check_on_invalid_length_number(digits: str, number: str) -> None:
    """Check amount of digits, if digits less than 6 or more than 12 - raises exception"""

    if len(digits) < 6 or len(digits) > 12:
        raise InvalidLengthNumberException(number)


def check_on_invalid_name(first_name: str, last_name: str) -> None:
    """Check amount of firstname and lastname.
    If firstname length equal 0 or more than 12 - raises exception.
    And if lastname length more than 12 - raises exception
    """

    if len(first_name) < 1 or len(first_name) > 12:
        raise InvalidNameException(first_name)

    if len(last_name) > 12:
        raise InvalidNameException(last_name)


def check_on_quotes_in_name(first_name: str, last_name: str) -> None:
    """Check existing quotes in firstname and lastname"""

    if "'" in first_name or '"' in first_name:
        raise InvalidNameQuotesException(first_name)

    if "'" in last_name or '"' in last_name:
        raise InvalidNameQuotesException(last_name)


def check_on_invalid_number(digits: str, new_phone_number: str) -> None:
    """Check if number contain not only digits, it raises exception"""

    if not digits.isdigit():
        raise InvalidNumberException(new_phone_number)


def check_on_existing_number(contact_book: ContactBook, normal_number: str) -> None:
    """Check contact's number, if it exists in object of ContactBook - raise exception"""

    for contact in contact_book:
        if normal_number == contact.phone_number:
            raise NumberExistException()


def check_on_existing_name(contact_book: ContactBook, first_name: str, last_name: str) -> None:
    """Check contact's name, if it exists in object of ContactBook - raise exception"""

    for contact in contact_book:
        if f"{first_name} {last_name}" == f"{contact.first_name} {contact.last_name}":
            raise NameExistException()


def check_on_existing_in_favorites(contact_book: ContactBook, contact: Contact) -> None:
    """Check if contact is already exist in Favorites - raise exception"""

    search_contact = contact_book.get_contact_by_phone_number(contact.phone_number)
    if search_contact.favorites is True:
        raise ContactExistInFavoritesException(contact.first_name, contact.last_name)


def check_values_changes(old_contact: Contact, new_contact: Contact) -> None:
    """If user didn't change contact's values in the Edit frame - raise exceptions"""
    if old_contact == new_contact:
        raise ContactHasNoChanged()


def validity_checks(digits: str, number: str, contact_book: ContactBook,
                    new_contact: Contact, old_contact=None) -> None:
    """
    All validity checks of contact's number, name, number's length, already existing in Contact Book name and number
    :param digits: phone number digits (without dashes, pluses, spaces, brackets)
    :param number: phone number that user insert to Contact Book
    :param contact_book: object of the class ContactBook
    :param new_contact: object of contact with edited values
    :param old_contact: object of contact with old values (parameter fo Edit frame)
    :return: None
    """

    # Condition to Edit frame
    if old_contact is not None:
        check_values_changes(old_contact, new_contact)

        if old_contact.phone_number != new_contact.phone_number:
            # check is number exist in the Contact Book
            check_on_existing_number(contact_book, new_contact.phone_number)

        if f"{old_contact.first_name} {old_contact.last_name}" != f"{new_contact.first_name} {new_contact.last_name}":
            # check is name exist in the Contact Book
            check_on_existing_name(contact_book, new_contact.first_name, new_contact.last_name)

    # check 6 < digits < 13
    check_on_invalid_length_number(digits, number)

    # check 1 < firstname < 16 and lastname < 13
    check_on_invalid_name(new_contact.first_name, new_contact.last_name)

    # check firstname or lastname contains quotes
    check_on_quotes_in_name(new_contact.first_name, new_contact.last_name)
