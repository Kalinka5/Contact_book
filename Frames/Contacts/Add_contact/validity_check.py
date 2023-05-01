from Exceptions.invalid_contact import InvalidNameException, InvalidNumberException, InvalidLengthNumberException
from Exceptions.exist_contact import NumberExistException, NameExistException
from Exceptions.not_ukrainian_code import NotUkrainianCode


def check_on_invalid_length_number(digits, number):
    if len(digits) < 6 or len(digits) > 12:
        raise InvalidLengthNumberException(number)


def check_on_invalid_name(first_name, last_name):
    if len(first_name) < 1 or len(first_name) > 15:
        raise InvalidNameException(first_name)

    if len(last_name) > 12:
        raise InvalidNameException(last_name)


def check_on_invalid_number(result, number):
    if not result:
        raise InvalidNumberException(number)


def check_on_existing_number(contact_book, normal_number):
    all_numbers = contact_book.get_all_numbers
    if normal_number in all_numbers:
        raise NumberExistException()


def check_on_existing_name(contact_book, first_name, last_name):
    all_names = contact_book.get_all_names
    for name in all_names:
        if f"{first_name} {last_name}" in name:
            raise NameExistException()
