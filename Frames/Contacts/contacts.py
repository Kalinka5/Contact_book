import tkinter as tk
from tkinter import ttk

from Decorators.try_exceptions import try_exceptions
from Exceptions.exist_contact import ContactExistInFavoritesException
from Frames.Contacts.Add_contact.add_frame import AddFrame
from Frames.Contacts.Edit_contact.edit_frame import EditFrame
from Frames.Contacts.Delete_contact.delete_in_ContactBook import delete_in_contact_book
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
        self.departments_tree = tree
        self.favorites_tree = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        columns = ('first_name', 'last_name', 'number')
        self.contacts_tree = ttk.Treeview(self, columns=columns, show='headings')
        self.contacts_tree.heading('first_name', text='First Name')
        self.contacts_tree.heading('last_name', text='Second Name')
        self.contacts_tree.heading('number', text='Number')
        self.contacts_tree.column('first_name', width=100, anchor=tk.W)
        self.contacts_tree.column('last_name', width=100, anchor=tk.W)
        self.contacts_tree.column('number', width=200, anchor=tk.CENTER)

        self.contacts_tree.bind('<<TreeviewSelect>>', self.get_buttons_enable)

        # Create contacts to store data for Contacts Treeview
        self.contacts = []

        self.contacts_tree.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.contacts_tree.yview)
        self.contacts_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Create Label Frame with 3 buttons
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns', pady=10)

        # Button Add contact
        self.b1 = ttk.Button(master=self.lf, text='Add contact', command=self.add_contact, cursor='hand2')

        # Button Delete contact
        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact, cursor='hand2')

        # Button Rename contact
        self.b3 = ttk.Button(master=self.lf, text='Edit contact', command=self.rename_contact, cursor='hand2')

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
        AddFrame(self, self.contacts_tree, self.lf, self.scrollbar,
                 self.contact_book, self.departments_tree, self.favorites_tree)

    def delete_contact(self):
        human = self.contacts_tree.item(self.contacts_tree.focus())['values']

        first_name = human[0]
        last_name = human[1]
        number = human[2]

        # print confirmation messagebox "Are you sure that you want to delete contact?"
        answer = confirmation_messagebox(first_name, last_name)

        if answer:
            contact_index, contact_dep = contact_values(self.contact_book, first_name, last_name, number)

            # Delete contact in ContactsFrame
            delete_in_contacts_frame(self.contacts_tree)

            # Delete contact in DepartmentsFrame
            delete_in_departments_frame(self.departments_tree, contact_dep, first_name, last_name)

            # Delete contact in FavoritesFrame
            delete_in_favorites_frame(self.favorites_tree, first_name)

            # Delete contact in the class Contact book
            delete_in_contact_book(self.contact_book, contact_index)

            # notify user that the contact has been deleted successfully
            successfully_messagebox(first_name, last_name)

            # make buttons "Add contact", "Delete contact", "Rename contact" disabled
            self.b2.state(['disabled'])
            self.b3.state(['disabled'])
            self.b4.state(['disabled'])

    def rename_contact(self):
        EditFrame(self, self.contacts_tree, self.lf, self.scrollbar, self.contact_book, self.departments_tree,
                  self.favorites_tree, self.b2, self.b3, self.b4)

    @try_exceptions
    def add_to_favorites(self):
        item = self.contacts_tree.item(self.contacts_tree.focus())['values']
        first_name = item[0]
        last_name = item[1]
        number = item[2]

        index = 0
        while index < len(self.favorites_tree.get_children()):
            if number == self.favorites_tree.item(self.favorites_tree.get_children()[index])['values'][2].lower():
                raise ContactExistInFavoritesException(first_name, last_name)
            index += 1

        # print confirmation messagebox "Are you sure that you want to add contact to Favorites?"
        answer = confirmation_favorites(first_name, last_name)

        if answer:
            # Add contact to FavoritesFrame
            add_to_favorites_frame(self.favorites_tree, first_name, last_name, number)

            # Update contact's favorites to True value
            update_contact_favorites(self.contact_book, number)

            # notify user that the contact has been deleted from Favorites successfully
            successfully_favorites(first_name, last_name)
