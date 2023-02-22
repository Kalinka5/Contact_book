import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os
import pandas as pd


class ContactsFrame(ttk.Frame):
    def __init__(self, container, tab_control, contact_book, tree, department):
        super().__init__(container)
        self.tab_control = tab_control
        self.__create_widgets()
        self.contact_book = contact_book
        self.tree = tree
        self.department = department

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        columns = ('first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(self, columns=columns, show='headings')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('first_name', width=100, anchor=tk.CENTER)
        self.txt.column('last_name', width=100, anchor=tk.CENTER)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        df = pd.read_csv("Contact_book.csv")
        # generate sample data
        self.contacts = []
        if os.path.exists("Contact_book.csv"):
            contact_book_r = open("Contact_book.csv")
            reader = csv.DictReader(contact_book_r)

            if not df.empty:
                for row in reader:
                    self.contacts.append((row['first_name'], row['last_name'], row['numbers'], row['department']))

            # add data to the treeview
            for contact in self.contacts:
                self.txt.insert('', tk.END, values=contact)

            contact_book_r.close()

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # label frame
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns')

        self.b2 = ttk.Button(master=self.lf, text='Delete contact', command=self.delete_contact, cursor='hand2')
        self.b3 = ttk.Button(master=self.lf, text='Rename contact', command=self.rename_contact, cursor='hand2')
        self.b4 = ttk.Button(master=self.lf, text='Add to favorites', command=self.add_to_favorites, cursor='hand2')

        self.b2.grid(row=1, column=0, sticky='ns')
        self.b3.grid(row=1, column=1, sticky='ns')
        self.b4.grid(row=1, column=2, sticky='ns')

    def delete_contact(self):
        human = self.txt.item(self.txt.focus())['values']

        first_name = human[0]
        last_name = human[1]
        number = human[2]

        index_txt = None
        dep_user = None
        for n, user in enumerate(self.contact_book.contacts):
            if number == user.phone_number:
                index_txt = n
            if first_name == user.first_name:
                dep_user = user.department

        # Delete in class the Contact book
        contact = self.contact_book.contacts[index_txt]
        self.contact_book.delete_contact(contact)

        # Delete in ContactsFrame
        selected_item = self.txt.selection()[0]
        self.txt.delete(selected_item)

        found_id = None
        # Search for the row with 'Bob' in the first column
        for item in self.tree.get_children(self.department[dep_user]):
            if self.tree.item(item, 'text') == f"{first_name} {last_name}":
                found_id = item
                break

        # Delete in DepartmentsFrame
        self.tree.delete(found_id)

        tk.messagebox.showinfo(title='Update Contact Book',
                               message=f"\"{human[0]} {human[1]}\" was successfully deleted.")

        print(f"Deleting \"{human[0]} {human[1]}\" from your Contact Book was successfully.\n")

    def rename_contact(self):
        item = self.txt.item(self.txt.focus())['values']
        print(item)

        # selection = self.contact_listbox.curselection()
        # if selection:
        #     contact_index = selection[0]
        #     contact = self.contact_book.contacts[contact_index]
        #     new_name = self.name_entry.get()
        #     self.contact_book.rename_contact(contact, new_name)
        #     self.contact_listbox.delete(contact_index)
        #     self.contact_listbox.insert(contact_index, f"{new_name} - {contact.phone_number}")

    def add_to_favorites(self):
        item = self.txt.item(self.txt.focus())['values']
        print(item)
