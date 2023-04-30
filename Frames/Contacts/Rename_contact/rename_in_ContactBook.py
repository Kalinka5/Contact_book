def rename_in_contact_book(contact_book, new_first_name, new_last_name, number):
    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if number == user.phone_number:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact_book.rename_contact(contact, new_first_name, new_last_name)
