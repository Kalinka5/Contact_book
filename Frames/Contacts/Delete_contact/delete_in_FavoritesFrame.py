def delete_in_favorites_frame(favorites, first_name):
    item_id = None
    # Search for the row with contact name in the contact's department column
    for child in favorites.get_children():
        if favorites.set(child, "first_name") == first_name:
            item_id = child
            break

    if item_id is not None:
        favorites.delete(item_id)
