from number_exception import NumberException
import csv
import re


def write_csv(func):
    def _wrapper(*args, **kwargs):
        func(*args, **kwargs)
        peoples = []
        self = args[0]
        for name, phone in sorted(self.all_contacts.items()):
            peoples.append({"names": name.title(), "numbers": phone})
        with open("Contact_book.csv", "w") as contact_book:
            writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
            writer.writeheader()
            writer.writerows(peoples)
    return _wrapper


def check_name(func):
    def _wrapper(*args, **kwargs):
        self, name = args[:2]
        result = func(*args, **kwargs)
        if result == 1:
            if name.title() in self.changed_names:
                print(f"There is no \"{name}\" in your Contact book.\n"
                      f"Maybe you mean \"{self.changed_names[name.title()]}\"?\n")
            else:
                print(f"There is no \"{name}\" in your Contact book.\n")
    return _wrapper


class ContactBook:
    def __init__(self):
        self.__favorites = {}
        self.all_contacts = {}
        self.changed_names = {}
        with open("Contact_book.csv", "w") as contact_book:
            writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
            writer.writeheader()
        print(f"Contact Book was created successfully.\n")

    @write_csv
    def add_phone_number(self, name, number):
        if number.replace("-", "").isdigit():
            self.all_contacts[name.title()] = number
            print(f"\"{name.title()}\" was successfully added to your Contact Book.\n")
        else:
            raise NumberException(number)

    @write_csv
    @check_name
    def change_name(self, old_name, new_name) -> 0 or 1:
        if old_name in self.all_contacts:
            self.all_contacts[new_name.title()] = self.all_contacts[old_name]
            self.all_contacts.pop(old_name)
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

    @write_csv
    @check_name
    def delete_phone_number(self, name) -> 0 or 1:
        if name in self.all_contacts:
            self.all_contacts.pop(name.title())
            print(f"Deleting \"{name.title()}\" from your Contact Book was successfully.\n")
            return 0
        else:
            print("Can't remove the contact.")
            return 1

    @check_name
    def add_to_favorites(self, name) -> 0 or 1:
        if name in self.all_contacts:
            self.__favorites[name.title()] = self.all_contacts[name.title()]
            print(f"\"{name.title()}\" was successfully added to the favorites.\n")
            return 0
        else:
            print("Can't add contact to the favorites.")
            return 1

    def favorites_numbers(self):
        text = ""
        for name, number in sorted(self.__favorites.items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(r"(\w+): (\d{3})(\d{3})(\d{4})\n", text)

        result = "Your favorites:\n\n"
        for i in data:
            result += f"{i[0]}: ({i[1]})-{i[2]}-{i[3]}\n"

        return result

    def search_contact(self, letter):
        result = ""
        for name, number in self.all_contacts.items():
            if name.startswith(letter):
                result += f"{name}: {number}\n"
        if result == "":
            print(f"There are no names which starts with \"{letter}\" letter.\n")
        else:
            print(f"Contacts which starts with \"{letter}\" letter:\n")
            print(result)

    def __str__(self):
        text = ""
        for name, number in sorted(self.all_contacts.items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(r"(\w+): (\d{3})(\d{3})(\d{4})\n", text)

        result = "Your Contact Book:\n\n"
        for i in data:
            result += f"{i[0]}: ({i[1]})-{i[2]}-{i[3]}\n"
            
        return result
