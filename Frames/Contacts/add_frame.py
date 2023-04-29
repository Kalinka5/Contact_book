import tkinter as tk
from tkinter import ttk, messagebox
import re

from Exceptions.invalid_name import InvalidNameException
from Exceptions.invalid_number import InvalidNumberException
from Exceptions.number_exist import NumberExistException
from Exceptions.name_exist import NameExistException
from Exceptions.not_ukrainian_code import NotUkrainianCode
from Exceptions.length_number import InvalidLengthNumberException
from Frames.Departments.departments import DepartmentsFrame as Depart
from contact_book import Contact


class AddFrame(ttk.Frame):

    def __init__(self, container, contacts_txt, contacts_lf, contacts_scrollbar,
                 contact_book, tree, favorites):
        super().__init__(container)

        self.ukrainian_numbers = ["039", "050", "063", "066", "067", "068",
                                  "091", "092", "093", "094", "095", "096", "097", "098", "099"]

        self.contacts_txt = contacts_txt
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.tree = tree
        self.favorites = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=self, text='Add Contact Window')
        lf.place(x=30, y=30)

        lbl1 = ttk.Label(master=lf, text='First Name', font=("BOLD", 10))
        lbl1.grid(row=1, column=0, padx=5)

        self.text3 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text3)
        t1.focus()
        t1.grid(row=1, column=1, padx=5)

        lbl2 = ttk.Label(master=lf, text='Last Name', font=("BOLD", 10))
        lbl2.grid(row=2, column=0, padx=5)

        self.text4 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text4)
        t2.grid(row=2, column=1, padx=5)

        lbl3 = ttk.Label(master=lf, text='Number', font=("BOLD", 10))
        lbl3.grid(row=3, column=0, padx=5, pady=10)

        self.text5 = tk.StringVar()
        t3 = ttk.Entry(master=lf, textvariable=self.text5)
        t3.grid(row=3, column=1, padx=5, pady=5)

        lbl4 = ttk.Label(master=lf, text="Departments")
        lbl4.grid(row=1, column=2, padx=5)
        departments_str = tk.StringVar()
        self.departments = ttk.Combobox(master=lf, textvariable=departments_str)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')
        self.departments['values'] = headers
        self.departments['state'] = 'readonly'
        self.departments.grid(row=2, column=2, padx=5)
        self.departments.bind('<<ComboboxSelected>>', self.get_button_enable)

        self.btn = ttk.Button(master=lf,
                              text='Add contact',
                              command=self.add,
                              cursor='hand2')
        self.btn.grid(row=4, column=2, padx=5, pady=15)
        self.btn.state(['disabled'])

        close_icon = tk.PhotoImage(file='images/close.png')
        download_button = ttk.Button(
            master=lf,
            image=close_icon,
            command=self.close_clicked
        )
        download_button.image = close_icon
        download_button.grid(row=0, column=2, sticky='e')

        self.tkraise()
        self.contacts_scrollbar.grid_forget()
        self.contacts_lf.grid_forget()

    def get_button_enable(self, department):
        # remove the disabled flag
        self.btn.state(['!disabled'])

    def close_clicked(self):
        self.contacts_txt.tkraise()
        self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
        self.contacts_lf.grid(row=1, column=0, sticky='ns')

    def add(self):
        try:
            first_name = self.text3.get().title()
            # if user don't enter first name, contact creates with "Mr/Mrs" first name
            if first_name == "":
                first_name = "Mr/Mrs"
            last_name = self.text4.get().title()
            number = self.text5.get()

            digits = number.replace("-", "").replace("+", "").replace(" ", "")

            if len(digits) < 6 or len(digits) > 12:
                raise InvalidLengthNumberException(number)

            # Check first name is it has less than 10 letters and more than 0
            if len(first_name) < 1 or len(first_name) > 15:
                raise InvalidNameException(first_name)
            # Check last name is it has less than 10 letters and more than 0
            if len(last_name) > 12:
                raise InvalidNameException(last_name)

            result = None
            normal_number = ""
            if len(digits) == 10:
                pattern = r"(\d{1})(\d{2})(\d{3})(\d{4})"
                result = re.search(pattern, digits)
                code = f"{result[1]}{result[2]}"

                if digits[:2] == "49":
                    pattern = r"(\d{2})(\d{2})(\d{6})"
                    result = re.search(pattern, digits)
                    # convert phone number to +00-00-000000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}"

                elif code in self.ukrainian_numbers:
                    # convert phone number to 0-(00)-000-0000
                    normal_number = f"{result[1]}-({result[2]})-{result[3]}-{result[4]}"
                else:
                    raise NotUkrainianCode(code)

            elif len(digits) == 11:
                pattern = r"(\d{2})(\d{3})(\d{3})(\d{3})"
                result = re.search(pattern, digits)
                # convert phone number to +00-000-000-000
                normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"
                if digits[:1] == "1":
                    pattern = r"(\d{1})(\d{3})(\d{3})(\d{4})"
                    result = re.search(pattern, digits)
                    # convert phone number to +0-000-000-0000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"

            elif len(digits) == 12:
                pattern = r"(\d{3})(\d{2})(\d{3})(\d{4})"
                result = re.search(pattern, digits)

                code = f"{result[1][-1]}{result[2]}"
                if result[1] == "380":
                    if code in self.ukrainian_numbers:
                        # convert phone number to 0-(00)-000-0000
                        normal_number = f"{result[1][-1]}-({result[2]})-{result[3]}-{result[4]}"
                elif result[1] == "351":
                    pattern = r"(\d{3})(\d{3})(\d{3})(\d{3})"
                    result = re.search(pattern, digits)
                    # convert phone number to +000-000-000-000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}-{result[4]}"
                elif result[1] == "393":
                    pattern = r"(\d{2})(\d{3})(\d{7})"
                    result = re.search(pattern, digits)
                    # convert phone number to +00-000-0000000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}"
                elif digits[:2] == "44":
                    pattern = r"(\d{2})(\d{4})(\d{6})"
                    result = re.search(pattern, digits)
                    # convert phone number to +00-0000-000000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}"
                else:
                    pattern = r"(\d{2})(\d{3})(\d{7})"
                    result = re.search(pattern, digits)
                    # convert phone number to +00-0000-000000
                    normal_number = f"+{result[1]}-{result[2]}-{result[3]}"

            # If number contain not only digits, it raises exception
            if not result:
                raise InvalidNumberException(number)

            # check is number exist in the Contact Book
            all_numbers = self.contact_book.get_all_numbers
            if normal_number in all_numbers:
                raise NumberExistException()

            # check is name exist in the Contact Book
            all_names = self.contact_book.get_all_names
            for name in all_names:
                if f"{first_name} {last_name}" in name:
                    raise NameExistException()

            # Get index of contact where he is in contact book by alphabet
            index = 0
            while index < len(self.contacts_txt.get_children()):
                if first_name.lower() < self.contacts_txt.item(self.contacts_txt.get_children()[index])['values'][0].lower():
                    break
                index += 1

            # Check phone number is it has only digits
            if digits.isdigit():
                # Add contact to class Contacts
                department = self.departments.get()
                contact = Contact(first_name, last_name, normal_number, department)
                self.contact_book.add_contact(contact)

                # Add new contact to ContactsFrame
                self.contacts_txt.insert('',
                                         index,
                                         values=(first_name, last_name, normal_number))

                # Add contact to DepartmentsFrame
                children = self.tree.get_children(Depart.dict_departments[department])
                self.tree.delete(*children)

                amount_all_contacts = len(self.contact_book)
                for human in self.contact_book:
                    if human.department == department:
                        self.tree.insert('',
                                         tk.END,
                                         text=f'{human.first_name} {human.last_name}',
                                         iid=str(Contact.iid),
                                         open=False)
                        self.tree.move(str(Contact.iid),
                                       Depart.dict_departments[department],
                                       amount_all_contacts)
                        Contact.iid += 1

                # Clear all fields with data
                self.text3.set("")
                self.text4.set("")
                self.text5.set("")

                if last_name == "":
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name}\" was successfully added.")
                    print(f"\"{first_name}\" was successfully added to your Contact Book.\n")
                else:
                    # Show message box when add contact
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name} {last_name}\" was successfully added.")
                    print(f"\"{first_name} {last_name}\" was successfully added to your Contact Book.\n")

                # Open ContactsFrame again
                self.contacts_txt.tkraise()
                self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
                self.contacts_lf.grid(row=1, column=0, sticky='ns')
            else:
                raise InvalidNumberException(number)

        except InvalidNameException as ine:
            # When raise Name error, it shows message box with error text
            print(ine)
            messagebox.showerror(title='Name error',
                                 message=ine)
        except InvalidNumberException as inue:
            # When raise Number error, it shows message box with error text
            print(inue)
            messagebox.showerror(title='Number error',
                                 message=inue)
        except NumberExistException as cee:
            print(cee)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message="A contact with this number is already in the Contact book!")
        except NameExistException as nee:
            print(nee)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message="A contact with this name is already in the Contact Book!")
        except NotUkrainianCode as nuc:
            print(nuc)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message=nuc)
        except InvalidLengthNumberException as ilne:
            print(ilne)
            tk.messagebox.showerror(title='Update Contact Book',
                                      message=ilne)