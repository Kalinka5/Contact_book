def add_to_favorites_frame(favorites, first_name, last_name, number):
    index = 0
    while index < len(favorites.get_children()):
        favorites_name = favorites.item(favorites.get_children()[index])['values'][0].lower()
        if first_name.lower() < favorites_name[3:]:
            break
        index += 1

    favorites.insert('',
                     index,
                     values=(f"♥  {first_name}", last_name, number))
