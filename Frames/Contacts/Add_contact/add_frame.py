import tkinter as tk
from tkinter import ttk, messagebox

from Frames.Contacts.Add_contact.validity_check import *
from Frames.Contacts.Add_contact.convert_number import length_10, length_11, length_12
from Frames.Contacts.Add_contact.add_to_ContactsFrame import add_to_contacts_frame
from Frames.Contacts.Add_contact.add_to_class_Contacts import add_to_contacts
from Frames.Contacts.Add_contact.add_to_DepartmentsFrame import add_to_departments_frame
from Frames.Contacts.Add_contact.successfully_messagebox import successfully_messagebox


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

            # check 6 < digits < 13
            check_on_invalid_length_number(digits, number)

            # check 1 < firstname < 16 and lastname < 13
            check_on_invalid_name(first_name, last_name)

            # convert number in different formats
            result = None
            normal_number = ""
            if len(digits) == 10:
                result, normal_number = length_10(self.ukrainian_numbers, digits)

            elif len(digits) == 11:
                result, normal_number = length_11(digits)

            elif len(digits) == 12:
                result, normal_number = length_12(self.ukrainian_numbers, digits)

            # If number contain not only digits, it raises exception
            check_on_invalid_number(result, number)

            # check is number exist in the Contact Book
            check_on_existing_number(self.contact_book, normal_number)

            # check is name exist in the Contact Book
            check_on_existing_name(self.contact_book, first_name, last_name)

            # Check phone number is it has only digits
            if digits.isdigit():
                department = self.departments.get()

                # Add contact to class Contacts
                add_to_contacts(self.contact_book, department, first_name, last_name, normal_number)

                # Add new contact to ContactsFrame
                add_to_contacts_frame(self.contacts_txt, first_name, last_name, normal_number)

                # Add contact to DepartmentsFrame
                add_to_departments_frame(self.tree, self.contact_book, department)

                # Clear all fields with data
                self.text3.set("")
                self.text4.set("")
                self.text5.set("")

                # notify user that the contact has been added successfully
                successfully_messagebox(first_name, last_name)

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