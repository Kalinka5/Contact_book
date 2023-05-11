import tkinter as tk
from tkinter import ttk

from Frames.Contacts.Add_contact.add_frame import AddFrame
from Frames.Contacts.Edit_contact.edit_frame import EditFrame
from Frames.Contacts.Delete_contact.delete_in_all_frames import delete_contact_in_all_frames
from Frames.Contacts.Add_to_favorites.add_contact_to_favorites import add_contact_to_favorites


class ContactsFrame(ttk.Frame):
    def __init__(self, container, tab_control, contact_book, data_base, tree, favorites):
        super().__init__(container)

        self.tab_control = tab_control
        self.contact_book = contact_book
        self.data_base = data_base
        self.departments_tree = tree
        self.favorites_tree = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        columns = ('heart', 'first_name', 'last_name', 'number')
        self.contacts_tree = ttk.Treeview(self, columns=columns, show='headings')
        self.contacts_tree.heading('heart', text='♥')
        self.contacts_tree.heading('first_name', text='First Name')
        self.contacts_tree.heading('last_name', text='Second Name')
        self.contacts_tree.heading('number', text='Number')
        self.contacts_tree.column('heart', width=20, anchor=tk.CENTER)
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
        self.b3 = ttk.Button(master=self.lf, text='Edit contact', command=self.edit_contact, cursor='hand2')

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
                 self.contact_book, self.data_base, self.departments_tree, self.favorites_tree)

    def delete_contact(self):
        delete_contact_in_all_frames(self.contact_book, self.contacts_tree, self.data_base,
                                     self.departments_tree, self.favorites_tree)

        # make buttons "Add contact", "Delete contact", "Rename contact" disabled
        self.b2.state(['disabled'])
        self.b3.state(['disabled'])
        self.b4.state(['disabled'])

    def edit_contact(self):
        EditFrame(self, self.contacts_tree, self.lf, self.scrollbar, self.contact_book, self.data_base,
                  self.departments_tree, self.favorites_tree, self.b2, self.b3, self.b4)

    def add_to_favorites(self):
        add_contact_to_favorites(self.contact_book, self.data_base, self.contacts_tree, self.favorites_tree)
