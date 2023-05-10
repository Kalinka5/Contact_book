from dataclasses import dataclass

from output_contacts import OutputContact


@dataclass
class Contact:
    first_name: str
    last_name: str
    phone_number: str
    department: str = ""
    favorites: str = "False"
    iid: int = 0

    def __lt__(self, other):
        return self.first_name < other.first_name

    def __eq__(self, other):
        if not isinstance(other, Contact):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.first_name == other.first_name and self.last_name == other.last_name and \
            self.phone_number == other.phone_number


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

    def get_contact_by_phone_number(self, phone_number):
        # search index of contact to edit him by his index
        index_txt = None
        for n, user in enumerate(self.contacts):
            if phone_number == user.phone_number:
                index_txt = n

        contact = self.contacts[index_txt]
        return contact

    def add_contact(self, contact):
        self.contacts.append(contact)

    def delete_contact(self, contact):
        self.contacts.remove(contact)

    def edit_contact(self, contact, new_first_name, new_last_name, new_phone_number):
        contact.first_name = new_first_name
        contact.last_name = new_last_name
        contact.phone_number = new_phone_number
