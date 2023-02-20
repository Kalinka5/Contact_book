class OutputContact:
    def __str__(self):
        result = "Your Contact Book:\n\n"
        contact_book = sorted(getattr(self, "contacts"))
        for contact in contact_book:
            result += f"{contact.first_name} {contact.last_name} {contact.phone_number}\n"

        return result
