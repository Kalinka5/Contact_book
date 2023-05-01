def add_to_contacts_frame(contacts_txt, first_name, last_name, normal_number):
    # Get index of contact where he is in contact book by alphabet
    index = 0
    while index < len(contacts_txt.get_children()):
        if first_name.lower() < contacts_txt.item(contacts_txt.get_children()[index])['values'][0].lower():
            break
        index += 1

    contacts_txt.insert('',
                        index,
                        values=(first_name, last_name, normal_number))
