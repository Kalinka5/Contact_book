class ContactHasNoChanged(Exception):
    def __str__(self):
        return "The contact has not been changed!"
