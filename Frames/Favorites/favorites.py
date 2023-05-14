import tkinter as tk
from tkinter import ttk

from Contact_book.contact_book import ContactBook
from data_base import DataBase
from Frames.Favorites.delete_in_ContactsFrame import delete_in_contacts_frame
from Frames.Favorites.confirmation_messagebox import confirmation_messagebox
from Frames.Favorites.successfully_messagebox import successfully_messagebox
from Frames.Favorites.delete_in_FavoritesFrame import delete_in_favorites_frame
from Frames.Favorites.update_contact_in_ContactBook import update_contact_in_contact_book


class FavoritesFrame(ttk.Frame):
    emoji = "♥  "

    def __init__(self, parent_container, tab_control: ttk.Notebook, contact_book: ContactBook, data_base: DataBase):
        super().__init__(parent_container)

        self.parent = parent_container
        self.tab_control = tab_control
        self.contact_book = contact_book
        self.data_base = data_base

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Favorites')

        columns = ('heart', 'first_name', 'last_name', 'number')
        self.favorites_tree = ttk.Treeview(self, columns=columns, show='headings')
        self.favorites_tree.heading('heart', text='♥')
        self.favorites_tree.heading('first_name', text='First Name')
        self.favorites_tree.heading('last_name', text='Second Name')
        self.favorites_tree.heading('number', text='Number')
        self.favorites_tree.column('heart', width=20, anchor=tk.CENTER)
        self.favorites_tree.column('first_name', width=100, anchor=tk.W)
        self.favorites_tree.column('last_name', width=100, anchor=tk.W)
        self.favorites_tree.column('number', width=200, anchor=tk.CENTER)

        self.favorites_tree.bind('<<TreeviewSelect>>', self.get_button_enable)

        self.favorites_tree.grid(row=0, column=0, sticky='nsew', pady=25)

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.favorites_tree.yview)
        self.favorites_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns', pady=25)

        # Fill the Favorites tree
        for contact in self.contact_book:
            if contact.favorites:
                insert_contact = ("♥", contact.first_name, contact.last_name, contact.phone_number)

                self.favorites_tree.insert('', tk.END, values=insert_contact)

        # Create Label Frame with button "Delete from Favorites"
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns')

        self.b1 = ttk.Button(master=self.lf,
                             text='Delete from Favorites',
                             command=self.delete_from_favorites,
                             cursor='hand2')

        self.b1.grid(row=1, column=0, sticky='ns')
        self.b1.state(['disabled'])

    def get_button_enable(self, contact):
        # remove the disabled flag
        self.b1.state(['!disabled'])

    def get_contact_id_by_phone_number(self, phone_number: str):
        """Find contact's id in treeview of FavoritesFrame"""

        item_id = None
        for child in self.favorites_tree.get_children():
            if self.favorites_tree.set(child, "number") == phone_number:
                item_id = child
                break

        return item_id

    def delete_from_favorites(self):
        human = self.favorites_tree.item(self.favorites_tree.focus())['values']

        first_name = human[1]
        last_name = human[2]
        phone_number = human[3]

        # print confirmation messagebox "Are you sure that you want to delete contact from the Favorites?"
        answer = confirmation_messagebox(first_name, last_name)

        if answer:
            # delete in the FavoritesFrame
            delete_in_favorites_frame(self.favorites_tree)

            # update in the ContactBook
            update_contact_in_contact_book(self.contact_book, phone_number)

            # update in ContactsFrame
            delete_in_contacts_frame(self.parent.contacts_frame.contacts_tree, phone_number)

            # update favorites in a database
            self.data_base.delete_from_favorites(phone_number)

            # notify user that the contact has been deleted successfully
            successfully_messagebox(first_name, last_name)

            self.b1.state(['disabled'])
