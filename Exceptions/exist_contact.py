class ContactExistInFavoritesException(Exception):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        if self.last_name:
            return f"A contact \"{self.first_name} {self.last_name}\" is already in the Favorites!"
        else:
            return f"A contact \"{self.first_name}\" is already in the Favorites!"


class NameExistException(Exception):
    def __str__(self):
        return "A contact with this name is already in the Contact Book!"


class NumberExistException(Exception):
    def __str__(self):
        return "A contact with this number is already in the Contact book!"
