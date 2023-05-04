import re

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


def check_on_invalid_number(result: re.search, number: str) -> None:
    """Check if number contain not only digits, it raises exception"""
    if not result:
        raise InvalidNumberException(number)


def check_on_existing_number(contact_book: ContactBook, normal_number: str) -> None:
    """Check contact's number, if it exists in object of ContactBook - raise exception"""
    all_numbers = contact_book.get_all_numbers
    if normal_number in all_numbers:
        raise NumberExistException()


def check_on_existing_name(contact_book: ContactBook, first_name: str, last_name: str) -> None:
    """Check contact's name, if it exists in object of ContactBook - raise exception"""
    all_names = contact_book.get_all_names
    if f"{first_name} {last_name}" in all_names:
        raise NameExistException()
