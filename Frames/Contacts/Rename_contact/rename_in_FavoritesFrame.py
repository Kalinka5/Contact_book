def rename_in_favorites_frame(favorites, old_first_name, new_first_name, new_last_name, number):
    item_id = None
    # Search for the row with contact name in the contact's department column
    for child in favorites.get_children():
        if favorites.set(child, "first_name") == old_first_name:
            item_id = child
            break

    if item_id is not None:
        favorites.delete(item_id)
        index = 0
        while index < len(favorites.get_children()):
            contact = favorites.item(favorites.get_children()[index])
            if new_first_name.lower() < contact['values'][0].lower()[3:]:
                break
            index += 1

        favorites.insert('',
                         index,
                         values=(f"♥  {new_first_name}", new_last_name, number))
