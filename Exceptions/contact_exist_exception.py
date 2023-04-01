class ContactExistException(Exception):
    def __init__(self, number):
        self.name = number

    #  print exception
    def __str__(self):
        return "A contact with this number is already in the phone book!"
