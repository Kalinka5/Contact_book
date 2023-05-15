class ContactExistInFavoritesException(Exception):
    """User can't add contact to a Favorites frame if contact is already exist there"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        if self.last_name:
            return f"A contact \"{self.first_name} {self.last_name}\" is already in the Favorites!"
        else:
            return f"A contact \"{self.first_name}\" is already in the Favorites!"


class NameExistException(Exception):
    """User can't add(edit) contact with already existed contact's full name"""
    def __str__(self):
        return "A contact with this name is already in the Contact Book!"


class NumberExistException(Exception):
    """User can't add(edit) contact with already existed contact's phone number"""
    def __str__(self):
        return "A contact with this number is already in the Contact book!"
