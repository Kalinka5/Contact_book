from tkinter import ttk
import tkinter as tk

from contact_book import Contact
from Exceptions.validity_checks import check_on_invalid_number
from Exceptions.validity_checks import validity_checks
from Frames.Contacts.convert_number import convert_phone_number
from Frames.Contacts.Edit_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Edit_contact.successfully_messagebox import successfully_messagebox
from Frames.Contacts.Edit_contact.edit_in_ContactsFrame import edit_in_contacts_frame
from Frames.Contacts.Edit_contact.edit_in_DeparmentsFrame import edit_in_departments_frame
from Frames.Contacts.Edit_contact.edit_in_FavoritesFrame import edit_in_favorites_frame
from Frames.Contacts.Edit_contact.edit_in_ContactBook import edit_in_contact_book
from Decorators.try_exceptions import try_exceptions


class EditFrame(ttk.Frame):
    def __init__(self, container, contacts_txt, contacts_lf, contacts_scrollbar,
                 contact_book, tree, favorites, contacts_b2, contacts_b3, contacts_b4):
        super().__init__(container)

        self.contacts_txt = contacts_txt
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.tree = tree
        self.favorites = favorites
        self.contacts_b2 = contacts_b2
        self.contacts_b3 = contacts_b3
        self.contacts_b4 = contacts_b4

        self.__create_widgets()

    def __create_widgets(self):
        item = self.contacts_txt.item(self.contacts_txt.focus())['values']
        self.heart = item[0]
        self.old_first_name = item[1]
        self.old_last_name = item[2]
        self.old_phone_number = item[3]

        self.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=self, text='Edit Contact Window')
        lf.pack(anchor=tk.S, expand=True)

        close_icon = tk.PhotoImage(file='Images/close.png')
        close_button = ttk.Button(
            lf,
            image=close_icon,
            command=self.close_clicked
        )
        close_button.image = close_icon
        close_button.grid(row=0, column=1, sticky='e')

        lbl1 = ttk.Label(master=lf, text='New first name:', font=("BOLD", 10))
        lbl1.grid(row=1, column=0, sticky='w', padx=5)

        self.text1 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text1)
        t1.insert(0, self.old_first_name)
        t1.focus()
        t1.grid(row=2, column=0, padx=5)

        lbl2 = ttk.Label(master=lf, text='New last name:', font=("BOLD", 10))
        lbl2.grid(row=1, column=1, sticky='w', padx=5)

        self.text2 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text2)
        t2.insert(0, self.old_last_name)
        t2.grid(row=2, column=1, padx=5)

        lbl3 = ttk.Label(master=lf, text='New phone number:', font=("BOLD", 10))
        lbl3.grid(row=3, column=0, sticky='e', padx=5, pady=10)

        self.text3 = tk.StringVar()
        t3 = ttk.Entry(master=lf, textvariable=self.text3)
        t3.insert(0, self.old_phone_number)
        t3.grid(row=3, column=1, sticky='w', padx=5, pady=15)

        btn = ttk.Button(master=lf, text='Edit contact', command=self.edit, cursor='hand2')
        btn.grid(row=5, column=1)

        self.tkraise()
        self.contacts_scrollbar.grid_forget()
        self.contacts_lf.grid_forget()

    def close_clicked(self):
        self.contacts_txt.tkraise()
        self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
        self.contacts_lf.grid(row=1, column=0, sticky='ns')

    @try_exceptions
    def edit(self):
        new_first_name = self.text1.get().capitalize()
        if new_first_name == "":
            new_first_name = "Mr/Mrs"
        new_last_name = self.text2.get().capitalize()
        new_phone_number = self.text3.get()

        digits = new_phone_number.replace("-", "").replace("+", "").replace(" ", "").replace("(", "").replace(")", "")
        check_on_invalid_number(digits, new_phone_number)

        # convert number in different formats
        normal_number = convert_phone_number(digits)

        old_contact = Contact(self.old_first_name, self.old_last_name, self.old_phone_number)
        new_contact = Contact(new_first_name, new_last_name, normal_number)

        validity_checks(digits, new_phone_number, self.contact_book, new_contact, old_contact)

        # print confirmation messagebox "Are you sure that you want to edit contact?"
        answer = confirmation_messagebox(new_first_name, new_last_name)

        if answer:
            # edit contact in the class ContactBook
            edit_in_contact_book(self.contact_book, new_first_name, new_last_name,
                                 new_phone_number, self.old_phone_number)

            # edit contact in the class ContactsFrame
            edit_in_contacts_frame(self.contacts_txt, new_first_name, new_last_name, new_phone_number, self.heart)

            # edit contact in the class DepartmentsFrame
            edit_in_departments_frame(self.contact_book, self.tree, new_first_name)

            # edit contact in the class FavoritesFrame
            edit_in_favorites_frame(self.favorites, self.old_phone_number, new_first_name,
                                    new_last_name, new_phone_number)

            # notify user that the contact has been edited successfully
            successfully_messagebox(new_first_name, new_last_name)

            # Open ContactsFrame again
            self.contacts_txt.tkraise()
            self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
            self.contacts_lf.grid(row=1, column=0, sticky='ns')

            # make buttons "Add contact", "Delete contact", "Edit contact" disabled
            self.contacts_b2.state(['disabled'])
            self.contacts_b3.state(['disabled'])
            self.contacts_b4.state(['disabled'])
