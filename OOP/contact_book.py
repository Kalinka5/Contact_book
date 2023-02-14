from Exceptions.name_exception import NameException
from Exceptions.number_exception import NumberException
from output_contacts import OutputContact
from decorators import check_name
import csv
import re


class ContactBook(OutputContact):
    def __init__(self):
        self.__favorites = {}
        self.__all_contacts = {}
        self.changed_names = {}
        self.pattern = r"(\w+): (\d{3})(\d{3})([\d.]+)\n"
        with open("Contact_book.csv", "w") as contact_book:
            writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
            writer.writeheader()
        print(f"Contact Book was created successfully.\n")

    @property
    def favorites(self):
        return self.__favorites

    @property
    def all_contacts(self):
        return self.__all_contacts

    def add_phone_number(self, name, number):
        try:
            if len(name) < 1 or len(name) > 10:
                raise NameException(name)
            if number.replace("-", "").isdigit():
                self.__all_contacts[name.title()] = number
                print(f"\"{name.title()}\" was successfully added to your Contact Book.\n")
            else:
                raise NumberException(number)

        except NameException as ne:
            print(ne)

        except NumberException as ne:
            print(ne)

    @check_name
    def change_name(self, old_name, new_name) -> 0 or 1:
        if old_name in self.__all_contacts:
            self.__all_contacts[new_name.title()] = self.__all_contacts[old_name]
            self.__all_contacts.pop(old_name)
            if old_name in self.__favorites:
                self.__favorites[new_name.title()] = self.__favorites[old_name]
                self.__favorites.pop(old_name)
            self.changed_names[old_name.title()] = new_name.title()
            for key, value in self.changed_names.items():
                if value == old_name.title():
                    self.changed_names.pop(key)
                    break
            print(f"Contact \"{old_name.title()}\" was successfully changed to \"{new_name.title()}\".\n")
            return 0
        else:
            print(f"Can't change the contact name.")
            return 1

    @check_name
    def delete_phone_number(self, name) -> 0 or 1:
        if name in self.__all_contacts:
            self.__all_contacts.pop(name.title())
            print(f"Deleting \"{name.title()}\" from your Contact Book was successfully.\n")
            return 0
        else:
            print("Can't remove the contact.")
            return 1

    @check_name
    def add_to_favorites(self, name) -> 0 or 1:
        if name in self.__all_contacts:
            self.__favorites[name.title()] = self.__all_contacts[name.title()]
            print(f"\"{name.title()}\" was successfully added to the favorites.\n")
            return 0
        else:
            print("Can't add contact to the favorites.")
            return 1

    def search_contact(self, letter):
        text = ""
        for name, number in self.__all_contacts.items():
            if name.startswith(letter):
                text += f"{name}: {number.replace('-', '')}\n"

        if text == "":
            print(f"There are no names which starts with \"{letter}\" letter.\n")

        else:
            data = re.findall(self.pattern, text)

            result = f"Contacts which starts with \"{letter}\" letter:\n\n"
            for i in data:
                result += f"{i[0].ljust(10)} ({i[1]})-{i[2]}-{i[3]}\n"

            print(result)

    def save_csv_file(self):
        text = ""
        for name, number in sorted(self.all_contacts.items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(self.pattern, text)
        peoples = []
        for i in data:
            peoples.append({"names": i[0], "numbers": f"({i[1]})-{i[2]}-{i[3]}"})
        with open("Contact_book.csv", "w") as contact_book:
            writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
            writer.writeheader()
            writer.writerows(peoples)
