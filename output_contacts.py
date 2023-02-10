import re


class OutputContact:
    def print_favorites(self):
        text = ""
        for name, number in sorted(getattr(self, "favorites").items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(r"(\w+): (\d{3})(\d{3})(\d{4})\n", text)

        result = "Your favorites:\n\n"
        for i in data:
            result += f"{i[0].ljust(10)} ({i[1]})-{i[2]}-{i[3]}\n"

        return result

    def __str__(self):
        text = ""
        for name, number in sorted(getattr(self, "all_contacts").items()):
            text += f"{name}: {number.replace('-', '')}\n"

        data = re.findall(r"(\w+): (\d{3})(\d{3})(\d{4})\n", text)

        result = "Your Contact Book:\n\n"
        for i in data:
            result += f"{i[0].ljust(10)} ({i[1]})-{i[2]}-{i[3]}\n"

        return result
