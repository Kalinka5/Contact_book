import tkinter as tk
from tkinter import ttk

from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook

from Decorators.try_exceptions import try_exceptions

from Exceptions.validity_checks import check_on_invalid_number
from Exceptions.validity_checks import validity_checks

from Frames.Contacts.Edit_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Edit_contact.edit_in_ContactsFrame import edit_in_contacts_frame
from Frames.Contacts.Edit_contact.edit_in_DeparmentsFrame import edit_in_departments_frame
from Frames.Contacts.Edit_contact.edit_in_FavoritesFrame import edit_in_favorites_frame
from Frames.Contacts.Edit_contact.successfully_messagebox import successfully_messagebox
from Frames.Contacts.convert_number import convert_phone_number

from data_base import DataBase


class EditFrame(ttk.Frame):
    def __init__(self, parent_container, search_fr: ttk.Frame, buttons_lf: ttk.LabelFrame,
                 contacts_scrollbar: ttk.Scrollbar, contact_book: ContactBook, data_base: DataBase,
                 contacts_tree: ttk.Treeview, departments_tree: ttk.Treeview, favorites: ttk.Treeview):
        super().__init__(parent_container)

        self.parent = parent_container
        self.favorites_frame = self.parent.favorites_frame
        self.search_fr = search_fr
        self.buttons_lf = buttons_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.data_base = data_base
        self.contacts_tree = contacts_tree
        self.departments_tree = departments_tree
        self.favorites_tree = favorites
        self.contacts_b2 = self.parent.b2
        self.contacts_b3 = self.parent.b3
        self.contacts_b4 = self.parent.b4

        self.__create_widgets()

    def __create_widgets(self):
        item = self.contacts_tree.item(self.contacts_tree.focus())['values']
        self.old_first_name = item[1]
        self.old_last_name = item[2]
        self.old_phone_number = item[3]

        self.grid(row=1, column=0, sticky='nsew')

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
        self.search_fr.grid_forget()
        self.buttons_lf.grid_forget()

    def close_clicked(self) -> None:
        """When click on red close button, returns list of contacts(ContactsFrame)"""

        self.contacts_tree.tkraise()
        self.contacts_scrollbar.grid(row=1, column=1, sticky='ns')
        self.search_fr.grid(row=0, column=0, columnspan=2, pady=10)
        self.buttons_lf.grid(row=2, column=0, columnspan=2, sticky='ns', pady=10)

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

        old_contact = self.contact_book.get_contact_by_phone_number(self.old_phone_number)
        new_contact = Contact(new_first_name, new_last_name, normal_number)

        validity_checks(digits, new_phone_number, self.contact_book, new_contact, old_contact)

        # print confirmation messagebox "Are you sure that you want to edit contact?"
        answer = confirmation_messagebox(new_contact)

        if answer:
            # edit contact in the class ContactBook
            self.contact_book.edit_contact(old_contact, new_first_name, new_last_name, normal_number)

            # edit contact in the class ContactsFrame
            edit_in_contacts_frame(self.contacts_tree, new_contact)

            # edit contact in the class DepartmentsFrame
            edit_in_departments_frame(self.contact_book, self.departments_tree, new_contact.phone_number)

            # edit contact in the class FavoritesFrame
            edit_in_favorites_frame(self.favorites_frame, self.favorites_tree, self.old_phone_number, new_contact)

            # edit contact in a database
            self.data_base.edit_contact(new_contact, self.old_phone_number)

            # notify user that the contact has been edited successfully
            successfully_messagebox(new_contact)

            # Open ContactsFrame again
            self.contacts_tree.tkraise()
            self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
            self.search_fr.grid(row=0, column=0, columnspan=2, pady=10)
            self.buttons_lf.grid(row=2, column=0, columnspan=2, sticky='ns', pady=10)

            # make buttons "Add contact", "Delete contact", "Edit contact" disabled
            self.contacts_b2.state(['disabled'])
            self.contacts_b3.state(['disabled'])
            self.contacts_b4.state(['disabled'])
