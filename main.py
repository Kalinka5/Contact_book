from contact_book_gui import ContactBookGUI


if __name__ == '__main__':
    contact_book = ContactBookGUI()
    contact_book.mainloop()
    contact_book.save_csv_file()
    print(contact_book.contact_book)
