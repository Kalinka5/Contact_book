import tkinter as tk
from tkinter import ttk
from Frames.First_frame.first_frame import ImageFrame
from Frames.Contacts.contacts import ContactsFrame
from Frames.Departments.departments import DepartmentsFrame
from Frames.Favorites.favorites import FavoritesFrame
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

        self.data = []
        self.contact_book = ContactBook()
        self.tab_control = ttk.Notebook(self)
        self.tab_control.pack(expand=1, fill='both')

        self.__create_widgets()

    def __create_widgets(self):

        ImageFrame(self, self.tab_control)

        departments_frame = DepartmentsFrame(self, self.tab_control)

        favorites_frame = FavoritesFrame(self,
                                         self.tab_control,
                                         self.contact_book)

        contacts_frame = ContactsFrame(self,
                                       self.tab_control,
                                       self.contact_book,
                                       departments_frame.tree,
                                       departments_frame.dict_departments,
                                       favorites_frame.txt)

        # Read data from csv file
        df = pd.read_csv("Contact_book.csv")
        favorites = []
        contacts = []
        if os.path.exists("Contact_book.csv"):
            contact_book_r = open("Contact_book.csv")
            reader = csv.DictReader(contact_book_r)
            if not df.empty:
                for row in reader:
                    self.contact_book.contacts.append(Contact(row['first_name'],
                                                              row['last_name'],
                                                              row['numbers'],
                                                              row['department'],
                                                              row['favorites']))

                amount_all_contacts = len(self.contact_book)
                contact_book_r.seek(0)
                reader = csv.DictReader(contact_book_r)

                for row in reader:
                    departments_frame.tree.insert('',
                                                  tk.END,
                                                  text=f'{row["first_name"]} {row["last_name"]}',
                                                  iid=str(Contact.iid),
                                                  open=False)
                    departments_frame.tree.move(str(Contact.iid),
                                                departments_frame.dict_departments[row["department"]],
                                                amount_all_contacts)
                    Contact.iid += 1

                    if row["favorites"] == "True":
                        favorites.append((f"♥  {row['first_name']}", row['last_name'], row['numbers']))

                    contacts.append((row['first_name'], row['last_name'], row['numbers']))

                # add data to the Favorites Treeview
                for contact in favorites:
                    favorites_frame.txt.insert('', tk.END, values=contact)

                # add data to the Contacts Treeview
                for contact in contacts:
                    contacts_frame.txt.insert('', tk.END, values=contact)

            contact_book_r.close()

    def save_csv_file(self):
        contact_book_w = open("Contact_book.csv", "w")
        writer = csv.DictWriter(contact_book_w, fieldnames=["first_name",
                                                            "last_name",
                                                            "numbers",
                                                            "department",
                                                            "favorites"])
        writer.writeheader()

        peoples = []
        for contact in sorted(self.contact_book.contacts, key=lambda c: c.first_name):
            peoples.append({"first_name": contact.first_name,
                            "last_name": contact.last_name,
                            "numbers": contact.phone_number,
                            "department": contact.department,
                            "favorites": contact.favorites})

        writer.writerows(peoples)

        contact_book_w.close()
