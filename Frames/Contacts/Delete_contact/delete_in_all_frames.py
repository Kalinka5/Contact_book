from Frames.Contacts.Delete_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Delete_contact.delete_in_ContactBook import delete_in_contact_book
from Frames.Contacts.Delete_contact.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Contacts.Delete_contact.delete_in_DepartmentsFrame import delete_in_departments_frame
from Frames.Contacts.Delete_contact.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Contacts.Delete_contact.search_index_departments import contact_values
from Frames.Contacts.Delete_contact.successfully_messagebox import successfully_messagebox


def delete_contact_in_all_frames(contact_book, contacts_tree, departments_tree, favorites_tree):
    human = contacts_tree.item(contacts_tree.focus())['values']

    first_name = human[1]
    last_name = human[2]
    number = human[3]

    # print confirmation messagebox "Are you sure that you want to delete contact?"
    answer = confirmation_messagebox(first_name, last_name)

    if answer:
        contact_index, contact_dep = contact_values(contact_book, first_name, last_name, number)

        # Delete contact in ContactsFrame
        delete_in_contacts_frame(contacts_tree)

        # Delete contact in DepartmentsFrame
        delete_in_departments_frame(departments_tree, contact_dep, first_name, last_name)

        # Delete contact in FavoritesFrame
        delete_in_favorites_frame(favorites_tree, number)

        # Delete contact in the class Contact book
        delete_in_contact_book(contact_book, contact_index)

        # notify user that the contact has been deleted successfully
        successfully_messagebox(first_name, last_name)
