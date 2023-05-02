from contact_book import ContactBook


def contact_values(contact_book: ContactBook, first_name: str, last_name: str, number: str) -> tuple[int, str]:
    """Search contact's index in ContactBook, and he's value of departments"""

    contact_index = None
    contact_dep = None

    for n, user in enumerate(contact_book.contacts):
        if number == user.phone_number:
            contact_index = n
        if first_name == user.first_name and last_name == user.last_name:
            contact_dep = user.department

    return contact_index, contact_dep
