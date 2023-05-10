from output_contacts import OutputContact


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
