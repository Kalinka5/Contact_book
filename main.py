from contact_book import ContactBook
from number_exception import NumberException


if __name__ == '__main__':
    try:
        book = ContactBook()

        book.add_phone_number("eldar", "098-342-8567")
        book.change_name("Eldar", "darik")
        book.change_name("Eldar", "loh")

        book.add_phone_number("nika", "056-339-6649")

        book.add_phone_number("Katya", "093-57-7731")

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
        print(book.favorites_numbers())

    except NumberException as ne:
        print(ne)
