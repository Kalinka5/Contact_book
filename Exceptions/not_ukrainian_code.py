class NotUkrainianCode(Exception):
    """If user enter phone number, which doesn't start with ukrainian code - raise exception"""
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return f"The phone code \"{self.code}\" is not to belong Ukrainian operators.\n" \
               "Please enter international country code before your number.\n" \
               "For example: \"+380-00-000-0000\"."
