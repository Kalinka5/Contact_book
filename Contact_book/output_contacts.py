class OutputContactBook:
    def __str__(self):
        result = "Your Contact Book:\n\n"
        contact_book = sorted(getattr(self, "get_contacts"))
        for contact in contact_book:
            if contact.last_name:
                result += f"{contact.first_name.ljust(13)} {contact.last_name.ljust(13)} {contact.phone_number}\n"
            else:
                result += f"{contact.first_name.ljust(27)} {contact.phone_number}\n"

        return result
