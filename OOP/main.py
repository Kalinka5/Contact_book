from contact_book import ContactBook


if __name__ == '__main__':
    book = ContactBook()

    book.add_phone_number("eldar", "0983428567")
    book.change_name("Eldar", "darik")
    book.change_name("Eldar", "loh")

    book.add_phone_number("", "056-339-6649")

    book.add_phone_number("Katya", "093-576-7bb731")

    book.add_phone_number("Nikahbsdhbsdvsd", "050-387-0087")

    book.add_to_favorites("eldAr")
    book.add_to_favorites("Darik")

    book.change_name("Darik", "Eldar_loh")

    book.delete_phone_number("Darik")
    book.delete_phone_number("Eldar")

    book.delete_phone_number("Nika")

    book.delete_phone_number("Andrew")

    book.add_to_favorites("Katya")

    book.add_phone_number("Roma", "066-299-5284")

    book.add_phone_number("Elena", "066-007-7329")

    book.search_contact("E")

    print(book)
    print(book.print_favorites())
