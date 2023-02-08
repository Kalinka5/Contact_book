from number_exception import NumberException
import csv


class ContactBook:
    def __init__(self, name: str, number: str):
        self.__favorites = {}
        self.all_contacts = {}
        self.changed_names = {}
        if number.replace("-", "").isdigit():
            self.all_contacts = {name.title(): number}
            peoples = [{"names": name, "numbers": number}]
            with open("Contact_book.csv", "w") as contact_book:
                writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
                writer.writeheader()
                writer.writerows(peoples)
            print(f"Creation Contact Book with contact \"{name.title()}\" was successfully.\n")
        else:
            raise NumberException(number)

    def add_phone_number(self, name, number):
        if number.replace("-", "").isdigit():
            self.all_contacts[name.title()] = number
            peoples = [{"names": name.title(), "numbers": number}]
            with open("Contact_book.csv", "a") as contact_book:
                writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
                writer.writerows(peoples)
            print(f"\"{name.title()}\" was successfully added to your Contact Book.\n")
        else:
            raise NumberException(number)

    def change_name(self, old_name, new_name):
        if old_name in self.all_contacts:
            peoples = []
            for name, phone in self.all_contacts.items():
                if name == old_name.title():
                    print(f"Contact \"{old_name.title()}\" was successfully changed to \"{new_name.title()}\".\n")
                    self.all_contacts[new_name.title()] = phone
                    peoples.append({"names": new_name.title(), "numbers": phone})
                    self.all_contacts.pop(old_name.title())
                    self.changed_names[old_name.title()] = new_name.title()
                    for key, value in self.changed_names.items():
                        if value == old_name.title():
                            self.changed_names.pop(key)
                            break
                    break
                else:
                    peoples.append({"names": name, "numbers": phone})

            with open("Contact_book.csv", "w") as contact_book:
                writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
                writer.writeheader()
                writer.writerows(peoples)

        elif old_name.title() in self.changed_names:
            print(f"You can't change {old_name} name.\n"
                  f"There is no contact with name \"{old_name}\" in your Contact Book.\n"
                  f"Maybe you mean \"{self.changed_names[old_name.title()]}\"?\n")
        else:
            print(f"There is no contact with name \"{old_name}\" in your Contact Book.\n")

    def delete_phone_number(self, name):
        if name in self.all_contacts:
            self.all_contacts.pop(name.title())
            peoples = []
            for key, value in self.all_contacts.items():
                peoples.append({"names": key, "numbers": value})
            with open("Contact_book.csv", "w") as contact_book:
                writer = csv.DictWriter(contact_book, fieldnames=["names", "numbers"])
                writer.writeheader()
                writer.writerows(peoples)
            print(f"Deleting \"{name.title()}\" from your Contact Book was successfully.\n")
        elif name.title() in self.changed_names:
            print(f"Can't delete \"{name}\".\nThere is no \"{name.title()}\" in the Contact book.\n"
                  f"Maybe you mean \"{self.changed_names[name.title()]}\"?\n")
        else:
            print(f"Can't delete \"{name}\".\nThere is no \"{name.title()}\" in the Contact book.\n")

    def add_to_favorites(self, name):
        if name in self.all_contacts:
            self.__favorites[name.title()] = self.all_contacts[name.title()]
            print(f"\"{name.title()}\" was successfully added to the favorites.\n")
        elif name.title() in self.changed_names:
            print(f"Can't add \"{name}\" to the favorites."
                  f"\nThere is no \"{name}\" in your Contact book.\n"
                  f"Maybe you mean \"{self.changed_names[name.title()]}\"?\n")
        else:
            print(f"Can't add \"{name}\" to the favorites.\n"
                  f"There is no \"{name}\" in your Contact book.\n")

    def favorites_numbers(self):
        result = "Your favorites:\n\n"
        for name, number in self.__favorites.items():
            if name not in self.all_contacts:
                result += f"{self.changed_names[name]}: {number}\n"
            else:
                result += f"{name}: {number}\n"
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
        result = "Your Contact Book:\n\n"
        for name, number in sorted(self.all_contacts.items()):
            result += f"{name}: {number}\n"
        return result
