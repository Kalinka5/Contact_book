class InvalidNumberException(Exception):
    def __init__(self, number):
        self.number = number

    #  print exception
    def __str__(self):
        return f"Invalid value of phone number: \"{self.number}\".\n" \
               "Number should contain only integers and dashes.\n" \
               "Number example: \"000-000-0000\" or \"0000000000\".\n"
