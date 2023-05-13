import tkinter as tk
from tkinter import ttk

from Frames.First_frame.first_frame import ImageFrame
from Frames.Contacts.contacts import ContactsFrame
from Frames.Departments.departments import DepartmentsFrame
from Frames.Favorites.favorites import FavoritesFrame
from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook
from data_base import DataBase


class ContactBookGUI(tk.Tk):
    def __init__(self, contact_book: ContactBook, data_base: DataBase):
        print("Open Contact book.")
        super().__init__()

        self.title('Contact book')
        self.window_width = 430
        self.window_height = 340

        # get the screen dimension
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.resizable(False, False)

        self.iconbitmap('Images/receiver.ico')

        self.data = []
        self.contact_book = contact_book
        self.data_base = data_base
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill='both')

        self.__create_widgets()

    def __create_widgets(self):

        ImageFrame(self, self.tab_control)

        self.departments_frame = DepartmentsFrame(self, self.tab_control)

        self.favorites_frame = FavoritesFrame(self,
                                              self.tab_control,
                                              self.contact_book,
                                              self.data_base)

        self.contacts_frame = ContactsFrame(self,
                                            self.tab_control,
                                            self.contact_book,
                                            self.data_base,
                                            self.departments_frame.departments_tree,
                                            self.favorites_frame.favorites_tree)

        # Read data from ContactBook
        favorites = []
        contacts = []

        amount_all_contacts = len(self.contact_book)

        for contact in self.contact_book:
            self.departments_frame.departments_tree.insert('',
                                                           tk.END,
                                                           text=f'{contact.first_name} {contact.last_name}',
                                                           iid=str(Contact.iid),
                                                           open=False)
            self.departments_frame.departments_tree.move(str(Contact.iid),
                                                         self.departments_frame.dict_departments[contact.department],
                                                         amount_all_contacts)
            Contact.iid += 1

            if contact.favorites:
                favorites.append(("♥", contact.first_name, contact.last_name, contact.phone_number))
                contacts.append(("♥", contact.first_name, contact.last_name, contact.phone_number))
            else:
                contacts.append(("", contact.first_name, contact.last_name, contact.phone_number))

        # add data to the Favorites Treeview
        for contact in favorites:
            self.favorites_frame.favorites_tree.insert('', tk.END, values=contact)

        # add data to the Contacts Treeview
        for contact in contacts:
            self.contacts_frame.contacts_tree.insert('', tk.END, values=contact)
