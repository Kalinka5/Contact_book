from dataclasses import dataclass

from output_contacts import OutputContact


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone_number: str
    department: str
    favorites: str = "False"
    iid: int = 0

    def __lt__(self, other):
        return self.first_name < other.first_name


class ContactBook(OutputContact):
    def __init__(self):
        self.contacts = []

    @property
    def get_contacts(self):
        return self.contacts

    def __len__(self):
        return len(self.contacts)

    def __iter__(self):
        def generator():
            for item in sorted(self.contacts):
                yield item

        return generator()

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def edit_contact(self, contact, new_first_name, new_last_name, new_phone_number):
        contact.first_name = new_first_name
        contact.last_name = new_last_name
        contact.phone_number = new_phone_number
