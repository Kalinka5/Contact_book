from tkinter import ttk


def rename_in_favorites_frame(favorites: ttk.Treeview, old_first_name: str,
                              new_first_name: str, new_last_name: str, number: str) -> None:
    """Change contact's firstname and lastname in treeview of FavoritesFrame"""

    # find contact's id in treeview of FavoritesFrame
    item_id = None
    for child in favorites.get_children():
        if favorites.set(child, "first_name")[3:] == old_first_name:
            item_id = child
            break

    if item_id is not None:
        favorites.delete(item_id)

        # find contact's index to insert it in alphabetical order
        index = 0
        while index < len(favorites.get_children()):
            contact = favorites.item(favorites.get_children()[index])
            if new_first_name.lower() < contact['values'][0].lower()[3:]:
                break
            index += 1

        favorites.insert('',
                         index,
                         values=(f"♥  {new_first_name}", new_last_name, number))
