import csv
import re


def write_csv(func):
    def _wrapper(*args, **kwargs):
        func(*args, **kwargs)
        self = args[0]
        text = ""
        for name, number in sorted(self.all_contacts.items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(r"(\w+): (\d{3})(\d{3})(\d{4})\n", text)
        peoples = []
        for i in data:
            peoples.append({"names": i[0], "numbers": f"({i[1]})-{i[2]}-{i[3]}"})
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
