class InvalidNameException(Exception):
    """
    User can't add(edit) contact if:
        firstname length less than 0 or more than 12;
        lastname length more than 12.
    """
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid value of contact name: \"{self.name}\".\n" \
               "Name length should be from 1 to 12.\n"


class InvalidNameQuotesException(Exception):
    """User can't add(edit) contact if firstname or lastname contains quotes('', "")"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Invalid value of contact name: \"{self.name}\".\n" \
               "Name should be without quotes.\n"


class InvalidNumberException(Exception):
    """User can't add(edit) contact if phone number contains letters, punctuations"""
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Invalid value of phone number: \"{self.number}\".\n" \
               "Number should contain only integers and dashes.\n" \
               "Number example: \"0-(00)-000-0000\" or \"0000000000\".\n"


class InvalidLengthNumberException(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Invalid value of phone number: \"{self.number}\".\n" \
               "Number length should be from 6 to 12.\n" \
               "Number example: \"0-(00)-000-0000\" or \"0000000000\".\n"
