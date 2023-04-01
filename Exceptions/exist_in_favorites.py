class ContactExistFavoritesException(Exception):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"A contact {self.first_name} {self.last_name} is already in the Favorites!"
