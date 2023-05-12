import tkinter as tk
from tkinter import ttk

from Contact_book.contact_book import ContactBook
from Contact_book.contact import Contact
from data_base import DataBase
from Exceptions.validity_checks import check_on_invalid_number
from Exceptions.validity_checks import validity_checks
from Frames.Contacts.convert_number import convert_phone_number
from Frames.Contacts.Add_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Add_contact.add_to_ContactsFrame import add_to_contacts_frame
from Frames.Contacts.Add_contact.add_to_DepartmentsFrame import add_to_departments_frame
from Frames.Contacts.Add_contact.successfully_messagebox import successfully_messagebox
from Decorators.try_exceptions import try_exceptions


class AddFrame(ttk.Frame):

    def __init__(self, container: ttk.Frame, contacts_lf: ttk.LabelFrame, contacts_scrollbar: ttk.Scrollbar,
                 contact_book: ContactBook, data_base: DataBase, contacts_tree: ttk.Treeview,
                 departments_tree: ttk.Treeview, favorites: ttk.Treeview):
        super().__init__(container)

        self.contacts_txt = contacts_tree
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.data_base = data_base
        self.tree = departments_tree
        self.favorites = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=self, text='Add Contact Window')
        lf.pack(anchor=tk.S, expand=True)

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

        close_icon = tk.PhotoImage(file='Images/close.png')
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
        """Remove disabled flag from the button 'Add contact'
        :param department not used, but pass to this function
        """

        self.btn.state(['!disabled'])

    def close_clicked(self) -> None:
        """When click on red close button, returns list of contacts(ContactsFrame)"""

        self.contacts_txt.tkraise()
        self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
        self.contacts_lf.grid(row=1, column=0, sticky='ns')

    @try_exceptions
    def add(self) -> None:
        """Checks new contact's values for errors. Add new contact to class Contacts, ContactsFrame, DepartmentsFrame"""

        # convert firstname and lastname with big letter at the beginning
        first_name = self.text3.get().title()
        # if user don't enter first name, contact creates with "Mr/Mrs" first name
        if first_name == "":
            first_name = "Mr/Mrs"
        last_name = self.text4.get().title()
        number = self.text5.get()
        # need as parameter in add_to_contacts() and add_to_departments_frame()
        department = self.departments.get()

        digits = number.replace("-", "").replace("+", "").replace(" ", "").replace("(", "").replace(")", "")
        check_on_invalid_number(digits, number)

        # convert number in different formats
        normal_number = convert_phone_number(digits)

        new_contact = Contact(first_name, last_name, normal_number, department, favorites=False)

        validity_checks(digits, number, self.contact_book, new_contact)

        answer = confirmation_messagebox(new_contact)

        if answer:
            # Add contact to class ContactBook
            self.contact_book.add_contact(new_contact)

            # Add new contact to ContactsFrame
            add_to_contacts_frame(self.contacts_txt, new_contact)

            # Add contact to DepartmentsFrame
            add_to_departments_frame(self.tree, self.contact_book, department)

            # Add contact to database
            self.data_base.add_contact(new_contact)

            # Clear all fields with data
            self.text3.set("")
            self.text4.set("")
            self.text5.set("")

            # notify user that the contact has been added successfully
            successfully_messagebox(new_contact)

            # Open ContactsFrame again
            self.contacts_txt.tkraise()
            self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
            self.contacts_lf.grid(row=1, column=0, sticky='ns')
