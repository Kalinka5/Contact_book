class InvalidLengthNumberException(Exception):
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Invalid value of phone number: \"{self.number}\".\n" \
               "Number length should be from 6 to 12.\n" \
               "Number example: \"0-(00)-000-0000\" or \"0000000000\".\n"
