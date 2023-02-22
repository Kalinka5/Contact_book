from output_contacts import OutputContact
from dataclasses import dataclass


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone_number: str
    department: str

    def __lt__(self, other):
        return self.first_name < other.first_name


class ContactBook(OutputContact):
    def __init__(self):
        self.contacts = []

    @property
    def get_contacts(self):
        return self.contacts

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def rename_contact(self, contact, new_first_name, new_last_name):
        if new_first_name:
            contact.first_name = new_first_name
        if new_last_name:
            contact.last_name = new_last_name
