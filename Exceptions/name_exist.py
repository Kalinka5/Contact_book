class NameExistException(Exception):

    def __str__(self):
        return "A contact with this name is already in the Contact Book!"
