from tkinter import ttk

from Decorators.try_exceptions import try_exceptions
from Frames.Contacts.Add_to_favorites.confirmation_messagebox import confirmation_favorites
from Frames.Contacts.Add_to_favorites.add_to_FavoritesFrame import add_to_favorites_tree
from Frames.Contacts.Add_to_favorites.update_contact import update_contact_favorites
from Frames.Contacts.Add_to_favorites.successfully_messagebox import successfully_favorites
from Frames.Contacts.Add_to_favorites.add_to_ContactsFrame import update_contacts_tree
from Exceptions.validity_checks import check_on_existing_in_favorites
from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact


@try_exceptions
def add_contact_to_favorites(contact_book: ContactBook, data_base, contacts_tree: ttk.Treeview,
                             favorites_tree: ttk.Treeview) -> None:

    item = contacts_tree.item(contacts_tree.focus())['values']
    first_name = item[1]
    last_name = item[2]
    phone_number = item[3]
    contact = Contact(first_name, last_name, phone_number)

    check_on_existing_in_favorites(favorites_tree, contact)

    # print confirmation messagebox "Are you sure that you want to add contact to Favorites?"
    answer = confirmation_favorites(contact)

    if answer:
        # Add ♥ in the first column of Contacts tree
        update_contacts_tree(contacts_tree)

        # Add contact to FavoritesFrame
        add_to_favorites_tree(favorites_tree, contact)

        # Update contact's favorites to True value
        update_contact_favorites(contact_book, phone_number)

        # Update in a database
        data_base.add_to_favorites(phone_number)

        # notify user that the contact has been deleted from Favorites successfully
        successfully_favorites(contact)
