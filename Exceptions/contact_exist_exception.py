class ContactExistException(Exception):
    def __str__(self):
        return "A contact with this number is already in the phone book!"
