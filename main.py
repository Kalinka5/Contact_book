from contact_book_gui import ContactBookGUI
from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact
from data_base import DataBase


if __name__ == '__main__':
    data_base = DataBase()
    contacts = data_base.get_data()

    contact_book = ContactBook()
    for contact in contacts:
        contact_book.contacts.append(Contact(contact[0],
                                             contact[1],
                                             contact[2],
                                             contact[3],
                                             contact[4]))

    contact_book_gui = ContactBookGUI(contact_book, data_base)
    contact_book_gui.mainloop()

    print(contact_book_gui.contact_book)

    data_base.close_connection()
