from contact_book import Contact


def add_to_contacts(contact_book, department, first_name, last_name, normal_number):
    contact = Contact(first_name, last_name, normal_number, department)
    contact_book.add_contact(contact)
