def rename_in_contacts_frame(contacts_txt, new_first_name, new_last_name, number):
    selected_item = contacts_txt.selection()[0]
    contacts_txt.delete(selected_item)

    index = 0
    while index < len(contacts_txt.get_children()):
        if new_first_name.lower() < \
                contacts_txt.item(contacts_txt.get_children()[index])['values'][0].lower():
            break
        index += 1

    contacts_txt.insert('',
                        index,
                        values=(new_first_name, new_last_name, number))
