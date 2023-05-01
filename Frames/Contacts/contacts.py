import tkinter as tk
from tkinter import ttk, messagebox

from Exceptions.exist_contact import ContactExistInFavoritesException
from Frames.Contacts.Add_contact.add_frame import AddFrame
from Frames.Contacts.Rename_contact.rename_frame import RenameFrame
from Frames.Contacts.Delete_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Delete_contact.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Contacts.Delete_contact.search_index_departments import contact_values
from Frames.Contacts.Delete_contact.delete_in_DepartmentsFrame import delete_in_departments_frame
from Frames.Contacts.Delete_contact.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Contacts.Delete_contact.successfully_messagebox import successfully_messagebox
from Frames.Contacts.Add_to_favorites.confirmation_messagebox import confirmation_favorites
from Frames.Contacts.Add_to_favorites.successfully_messagebox import successfully_favorites
from Frames.Contacts.Add_to_favorites.add_to_FavoritesFrame import add_to_favorites_frame
from Frames.Contacts.Add_to_favorites.update_contact import update_contact_favorites


class ContactsFrame(ttk.Frame):
    def __init__(self, container, tab_control, contact_book, tree, favorites):
        super().__init__(container)

        self.tab_control = tab_control
        self.contact_book = contact_book
        self.tree = tree
        self.favorites = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        columns = ('first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(self, columns=columns, show='headings')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('first_name', width=100, anchor=tk.W)
        self.txt.column('last_name', width=100, anchor=tk.W)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        self.txt.bind('<<TreeviewSelect>>', self.get_buttons_enable)

        # Create contacts to store data for Contacts Treeview
        self.contacts = []

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Create Label Frame with 3 buttons
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns', pady=10)

        # Button Add contact
        self.b1 = ttk.Button(master=self.lf, text='Add contact', command=self.add_contact, cursor='hand2')

        # Button Delete contact
        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact, cursor='hand2')

        # Button Rename contact
        self.b3 = ttk.Button(master=self.lf, text='Rename contact', command=self.rename_contact, cursor='hand2')

        # Button Add to favorites
        self.b4 = ttk.Button(master=self.lf, text='Add to favorites', command=self.add_to_favorites, cursor='hand2')

        # Location of button Add contact
        self.b1.grid(row=1, column=0, sticky='ns')

        # Location of button Delete contact
        self.b2.grid(row=1, column=1, sticky='ns')
        self.b2.state(['disabled'])

        # Location of button Rename contact
        self.b3.grid(row=1, column=2, sticky='ns')
        self.b3.state(['disabled'])

        # Location of button Add to favorites
        self.b4.grid(row=1, column=3, sticky='ns')
        self.b4.state(['disabled'])

    def get_buttons_enable(self, contact):
        # remove the disabled flag
        self.b2.state(['!disabled'])
        self.b3.state(['!disabled'])
        self.b4.state(['!disabled'])

    def add_contact(self):
        AddFrame(self, self.txt, self.lf, self.scrollbar,
                 self.contact_book, self.tree, self.favorites)

    def delete_contact(self):
        human = self.txt.item(self.txt.focus())['values']

        first_name = human[0]
        last_name = human[1]
        number = human[2]

        # print confirmation messagebox "Are you sure that you want to delete contact?"
        answer = confirmation_messagebox(first_name, last_name)

        if answer:
            contact_index, contact_dep = contact_values(self.contact_book, first_name, last_name, number)

            # Delete contact in ContactsFrame
            delete_in_contacts_frame(self.txt)

            # Delete contact in DepartmentsFrame
            delete_in_departments_frame(self.tree, contact_dep, first_name, last_name)

            # Delete contact in FavoritesFrame
            delete_in_favorites_frame(self.favorites, first_name)

            # Delete contact in the class Contact book
            contact = self.contact_book.contacts[contact_index]
            self.contact_book.delete_contact(contact)

            # notify user that the contact has been deleted successfully
            successfully_messagebox(first_name, last_name)

            # make buttons "Add contact", "Delete contact", "Rename contact" disabled
            self.b2.state(['disabled'])
            self.b3.state(['disabled'])
            self.b4.state(['disabled'])

    def rename_contact(self):
        RenameFrame(self, self.txt, self.lf, self.scrollbar, self.contact_book, self.tree,
                    self.favorites, self.b2, self.b3, self.b4)

    def add_to_favorites(self):
        item = self.txt.item(self.txt.focus())['values']
        first_name = item[0]
        last_name = item[1]
        number = item[2]

        try:
            index = 0
            while index < len(self.favorites.get_children()):
                if number == self.favorites.item(self.favorites.get_children()[index])['values'][2].lower():
                    raise ContactExistInFavoritesException(first_name, last_name)
                index += 1

            # print confirmation messagebox "Are you sure that you want to add contact to Favorites?"
            answer = confirmation_favorites(first_name, last_name)

            if answer:
                # Add contact to FavoritesFrame
                add_to_favorites_frame(self.favorites, first_name, last_name, number)

                # Update contact's favorites to True value
                update_contact_favorites(self.contact_book, number)

                # notify user that the contact has been deleted successfully
                successfully_favorites(first_name, last_name)

        except ContactExistInFavoritesException as ceife:
            print(ceife)
            tk.messagebox.showwarning(
                title='Update Contact Book',
                message=ceife)
