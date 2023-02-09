class NameException(Exception):
    def __init__(self, name):
        self.name = name

    #  print exception
    def __str__(self):
        return f"Invalid value of contact name: \"{self.name}\".\n" \
               f"Name length should be from 1 to 10.\n"
