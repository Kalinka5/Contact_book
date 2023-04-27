import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno

from Exceptions.exist_in_favorites import ContactExistFavoritesException
from Frames.Contacts.add_frame import AddFrame
from Frames.Contacts.rename_frame import RenameFrame
from Frames.Departments.departments import DepartmentsFrame as Depart


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

        if last_name == "":
            answer = askyesno(title='Confirmation',
                              message=f'Are you sure that you want to delete \"{first_name}\"?')
        else:
            answer = askyesno(title='Confirmation',
                              message=f'Are you sure that you want to delete \"{first_name} {last_name}\"?')
        if answer:
            index_txt = None
            dep_user = None
            for n, user in enumerate(self.contact_book.contacts):
                if number == user.phone_number:
                    index_txt = n
                if first_name == user.first_name:
                    dep_user = user.department

            # Delete contact in ContactsFrame
            selected_item = self.txt.selection()[0]
            self.txt.delete(selected_item)

            # Delete contact in DepartmentsFrame
            found_id = None
            # Search for the row with contact name in the contact's department column
            for item in self.tree.get_children(Depart.dict_departments[dep_user]):
                if self.tree.item(item, 'text') == f"{first_name} {last_name}":
                    found_id = item
                    break

            self.tree.delete(found_id)

            # Delete contact in FavoritesFrame
            item_id = None
            # Search for the row with contact name in the contact's department column
            for child in self.favorites.get_children():
                if self.favorites.set(child, "first_name") == first_name:
                    item_id = child
                    break

            if item_id is not None:
                self.favorites.delete(item_id)

            # Delete contact in the class Contact book
            contact = self.contact_book.contacts[index_txt]
            self.contact_book.delete_contact(contact)

            if last_name == "":
                tk.messagebox.showinfo(title='Update Contact Book',
                                       message=f"\"{first_name}\" was successfully deleted.")
                print(f"Deleting \"{first_name}\" from your Contact Book was successfully.\n")
            else:
                tk.messagebox.showinfo(title='Update Contact Book',
                                       message=f"\"{first_name} {last_name}\" was successfully deleted.")
                print(f"Deleting \"{first_name} {last_name}\" from your Contact Book was successfully.\n")

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
                if number == self.favorites.item(self.favorites.get_children()[index])['values'][3].lower():
                    raise ContactExistFavoritesException(first_name, last_name)
                index += 1

            if last_name == "":
                answer = askyesno(
                    title='Confirmation',
                    message=f'Are you sure that you want to add \"{first_name}\" to the Favorites?')
            else:
                answer = askyesno(
                    title='Confirmation',
                    message=f'Are you sure that you want to add \"{first_name} {last_name}\" to the Favorites?')

            if answer:
                index = 0
                while index < len(self.favorites.get_children()):
                    favorites_name = self.favorites.item(self.favorites.get_children()[index])['values'][1].lower()
                    if first_name.lower() < favorites_name:
                        break
                    index += 1

                self.favorites.insert('',
                                      index,
                                      values=("🖤", first_name, last_name, number))

                index_txt = None
                for n, user in enumerate(self.contact_book.contacts):
                    if number == user.phone_number:
                        index_txt = n

                contact = self.contact_book.contacts[index_txt]
                contact.favorites = "True"

                if last_name == "":
                    tk.messagebox.showinfo(title='Update Contact Book',
                                           message=f"\"{first_name}\" was added to the Favorites successfully!")
                    print(f"\"{first_name}\" was added to the Favorites successfully!\n")
                else:
                    print(f"\"{first_name} {last_name}\" was added to the Favorites successfully!\n")
                    tk.messagebox.showinfo(
                        title='Update Contact Book',
                        message=f'"{first_name} {last_name}" was added to the Favorites successfully!')

        except ContactExistFavoritesException as fe:
            print(fe)
            if last_name:
                tk.messagebox.showwarning(
                    title='Update Contact Book',
                    message=f"A contact \"{first_name} {last_name}\" is already in the Favorites!")
            else:
                tk.messagebox.showwarning(title='Update Contact Book',
                                          message=f"A contact \"{first_name}\" is already in the Favorites!")
