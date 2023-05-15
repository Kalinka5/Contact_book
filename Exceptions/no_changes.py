class ContactHasNoChanged(Exception):
    """If user didn't change values in Edit frame"""
    def __str__(self):
        return "The contact has not been changed!"
