import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import pandas as pd


class FavoritesFrame(ttk.Frame):
    def __init__(self, container, tab_control):
        super().__init__(container)

        self.tab_control = tab_control

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Favorites')

        columns = ('', 'first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(self, columns=columns, show='headings')
        self.txt.heading('', text='')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('', width=20, anchor=tk.CENTER)
        self.txt.column('first_name', width=100, anchor=tk.W)
        self.txt.column('last_name', width=100, anchor=tk.W)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Read file to check is it empty
        df = pd.read_csv("Contact_book.csv")
        contacts = []

        # Append to Contacts Treeview all data from CSV file
        if os.path.exists("Contact_book.csv"):
            contact_book_r = open("Contact_book.csv")
            reader = csv.DictReader(contact_book_r)

            if not df.empty:
                for row in reader:
                    if row["favorites"] == "True":
                        contacts.append(('🖤', row['first_name'], row['last_name'], row['numbers']))

            # add data to the Favorites Treeview
            for contact in contacts:
                self.txt.insert('', tk.END, values=contact)

            contact_book_r.close()

        # Create Label Frame with 3 buttons
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns', pady=10)

        self.b1 = ttk.Button(master=self.lf,
                             text='Delete from Favorites',
                             command=self.delete_from_favorites,
                             cursor='hand2')

        self.b1.grid(row=1, column=0, sticky='ns')

    def delete_from_favorites(self):
        human = self.txt.item(self.txt.focus())['values']

        first_name = human[1]
        last_name = human[2]

        # Delete in ContactsFrame
        selected_item = self.txt.selection()[0]
        self.txt.delete(selected_item)

        messagebox.showinfo(title='Update Contact Book',
                            message=f"\"{first_name} {last_name}\" was successfully deleted from Favorites.")

        print(f"Deleting \"{first_name} {last_name}\" from your Contact Book was successfully from Favorites.\n")
