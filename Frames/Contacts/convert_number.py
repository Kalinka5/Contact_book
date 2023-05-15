import re

from Exceptions.not_ukrainian_code import NotUkrainianCode


def length_10(ukrainian_numbers: list, digits: str) -> str:
    """
    Convert contact's phone number with 10 digits into different number formats
    :param ukrainian_numbers: list of ukrainian subscriber's numbers
    :param digits: digits of contact's number
    :return: tuple of regular expression and phone number in normal format
    """

    pattern = r"(\d{1})(\d{2})(\d{3})(\d{4})"
    result = re.search(pattern, digits)
    code = f"{result[1]}{result[2]}"

    if digits[:2] == "49":
        pattern = r"(\d{2})(\d{2})(\d{6})"
        result = re.search(pattern, digits)
        # convert phone number to +00-00-000000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}"

    elif code in ukrainian_numbers:
        # convert phone number to 0-(00)-000-0000
        normal_number = f"{result[1]}-({result[2]})-{result[3]}-{result[4]}"
    else:
        raise NotUkrainianCode(code)

    return normal_number


def length_11(digits: str) -> str:
    """
    Convert contact's phone number with 11 digits into different number formats
    :param digits: digits of contact's number
    :return: tuple of regular expression and phone number in normal format
    """

    pattern = r"(\d{2})(\d{3})(\d{3})(\d{3})"
    result = re.search(pattern, digits)
    # convert phone number to +00-000-000-000
    normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"

    if digits[:1] == "1":
        pattern = r"(\d{1})(\d{3})(\d{3})(\d{4})"
        result = re.search(pattern, digits)
        # convert phone number to +0-000-000-0000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"

    return normal_number


def length_12(ukrainian_numbers: list, digits: str) -> str:
    """
    Convert contact's phone number with 12 digits into different number formats
    :param ukrainian_numbers: list of ukrainian subscriber's numbers
    :param digits: digits of contact's number
    :return: tuple of regular expression and phone number in normal format
    """
    pattern = r"(\d{3})(\d{2})(\d{3})(\d{4})"
    result = re.search(pattern, digits)
    code = f"{result[1][-1]}{result[2]}"

    if result[1] == "380":
        if code in ukrainian_numbers:
            # convert phone number to 0-(00)-000-0000
            normal_number = f"{result[1][-1]}-({result[2]})-{result[3]}-{result[4]}"
        else:
            raise NotUkrainianCode(code)
    elif result[1] == "351":
        pattern = r"(\d{3})(\d{3})(\d{3})(\d{3})"
        result = re.search(pattern, digits)
        # convert phone number to +000-000-000-000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"
    elif result[1] == "393":
        pattern = r"(\d{2})(\d{3})(\d{7})"
        result = re.search(pattern, digits)
        # convert phone number to +00-000-0000000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}"
    elif digits[:2] == "44":
        pattern = r"(\d{2})(\d{4})(\d{6})"
        result = re.search(pattern, digits)
        # convert phone number to +00-0000-000000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}"
    else:
        pattern = r"(\d{2})(\d{3})(\d{7})"
        result = re.search(pattern, digits)
        # convert phone number to +00-0000-000000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}"

    return normal_number


def convert_phone_number(digits: str) -> str:
    """Convert digits to phone number's formats of different countries"""

    ukrainian_numbers = ["039", "050", "063", "066", "067", "068",
                         "091", "092", "093", "094", "095", "096", "097", "098", "099"]

    normal_number = ""
    if len(digits) == 10:
        normal_number = length_10(ukrainian_numbers, digits)

    elif len(digits) == 11:
        normal_number = length_11(digits)

    elif len(digits) == 12:
        normal_number = length_12(ukrainian_numbers, digits)

    return normal_number
