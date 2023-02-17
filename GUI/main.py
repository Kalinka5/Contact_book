from contact_book import ContactBook


if __name__ == '__main__':
    contact_book = ContactBook()
    contact_book.mainloop()
    contact_book.save_csv_file()
    print(contact_book)
    # # print(contact_book.print_favorites())
