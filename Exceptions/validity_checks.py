from contact_book import ContactBook
from Exceptions.invalid_contact import InvalidNameException, InvalidNumberException, InvalidLengthNumberException
from Exceptions.exist_contact import NumberExistException, NameExistException


def check_on_invalid_length_number(digits: str, number: str) -> None:
    """Check amount of digits, if digits less than 6 or more than 12 - raises exception"""

    if len(digits) < 6 or len(digits) > 12:
        raise InvalidLengthNumberException(number)


def check_on_invalid_name(first_name: str, last_name: str) -> None:
    """Check amount of firstname and lastname.
    If firstname length equal 0 or more than 15 - raises exception.
    And if lastname length more than 12 - raises exception
    """

    if len(first_name) < 1 or len(first_name) > 12:
        raise InvalidNameException(first_name)

    if len(last_name) > 12:
        raise InvalidNameException(last_name)


def check_on_invalid_number(digits: str, new_phone_number: str) -> None:
    """Check if number contain not only digits, it raises exception"""

    # Check phone number is it has only digits
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


def validity_checks(digits: str, number: str, first_name: str, last_name: str,
                    contact_book: ContactBook, normal_number: str) -> None:
    """
    All validity checks of contact's number, name, number's length, already existing in Contact Book name and number
    :param digits: phone number digits (without dashes, pluses, spaces, brackets)
    :param number: phone number that user insert to Contact Book
    :param first_name: contact's firstname
    :param last_name: contact's lastname
    :param contact_book: object of the class ContactBook
    :param normal_number: formatted phone number by different countries format number
    :return: None
    """

    # check 6 < digits < 13
    check_on_invalid_length_number(digits, number)

    # check 1 < firstname < 16 and lastname < 13
    check_on_invalid_name(first_name, last_name)

    # check is number exist in the Contact Book
    check_on_existing_number(contact_book, normal_number)

    # check is name exist in the Contact Book
    check_on_existing_name(contact_book, first_name, last_name)
