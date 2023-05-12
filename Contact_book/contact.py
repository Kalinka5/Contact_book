from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone_number: str
    department: str = ""
    favorites: bool = False
    iid: int = 0

    def __post_init__(self):
        if self.last_name is None:
            self.last_name = ''

    def __lt__(self, other):
        return self.first_name < other.first_name

    def __eq__(self, other):
        if not isinstance(other, Contact):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.first_name == other.first_name and self.last_name == other.last_name and \
            self.phone_number == other.phone_number
