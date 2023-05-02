def delete_in_favorites_frame(txt, contact_book, first_name):
    selected_item = txt.selection()[0]
    txt.delete(selected_item)

    index_txt = None
    for n, user in enumerate(contact_book.contacts):
        if first_name == user.first_name:
            index_txt = n

    contact = contact_book.contacts[index_txt]
    contact.favorites = "False"