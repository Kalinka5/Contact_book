import re

from Exceptions.not_ukrainian_code import NotUkrainianCode


def length_10(ukrainian_numbers, digits):
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

    return result, normal_number


def length_11(digits):
    pattern = r"(\d{2})(\d{3})(\d{3})(\d{3})"
    result = re.search(pattern, digits)
    # convert phone number to +00-000-000-000
    normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"
    if digits[:1] == "1":
        pattern = r"(\d{1})(\d{3})(\d{3})(\d{4})"
        result = re.search(pattern, digits)
        # convert phone number to +0-000-000-0000
        normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"

    return result, normal_number


def length_12(ukrainian_numbers, digits):
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

    return result, normal_number
