import tkinter as tk
from tkinter import ttk
from Frames.first_frame import ImageFrame
from Frames.contacts import ContactsFrame
from Frames.departments import DepartmentsFrame
from Frames.add_contact import AddContactFrame
from contact_book import Contact, ContactBook
import csv
import os
import pandas as pd


class ContactBookGUI(tk.Tk):
    def __init__(self):
        print("Open Contact book.")
        super().__init__()

        self.title('Contact book')
        self.window_width = 430
        self.window_height = 320

        # get the screen dimension
        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        # find the center point
        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)

        # set the position of the window to the center of the screen
        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')
        self.resizable(False, False)

        self.iconbitmap('images/receiver.ico')

        df = pd.read_csv("Contact_book.csv")
        self.data = []
        self.contact_book = ContactBook()
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill='both')

        if os.path.exists("Contact_book.csv"):
            contact_book_r = open("Contact_book.csv")
            reader = csv.DictReader(contact_book_r)

            if not df.empty:
                for row in reader:
                    self.contact_book.contacts.append(Contact(row['first_name'],
                                                              row['last_name'],
                                                              row['numbers'],
                                                              row['department']))

            contact_book_r.close()

        self.__create_widgets()

    def __create_widgets(self):
        # create the input frame
        ImageFrame(self, self.tab_control)

        departments_frame = DepartmentsFrame(self, self.tab_control)

        contacts_frame = ContactsFrame(self,
                                       self.tab_control,
                                       self.contact_book,
                                       departments_frame.tree,
                                       departments_frame.dict_departments)

        AddContactFrame(self,
                        self.tab_control,
                        contacts_frame.txt,
                        departments_frame.tree,
                        departments_frame.i,
                        departments_frame.dict_departments,
                        self.contact_book)

    def save_csv_file(self):
        contact_book_w = open("Contact_book.csv", "w")
        writer = csv.DictWriter(contact_book_w, fieldnames=["first_name", "last_name", "numbers", "department"])
        writer.writeheader()

        peoples = []
        for contact in sorted(self.contact_book.contacts, key=lambda c: c.first_name):
            peoples.append({"first_name": contact.first_name,
                            "last_name": contact.last_name,
                            "numbers": contact.phone_number,
                            "department": contact.department})

        writer.writerows(peoples)

        contact_book_w.close()
