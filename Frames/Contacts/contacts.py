import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from Frames.Contacts.Add_contact.add_frame import AddFrame
from Frames.Contacts.Edit_contact.edit_frame import EditFrame
from Frames.Contacts.Delete_contact.delete_in_all_frames import delete_contact_in_all_frames
from Frames.Contacts.Add_to_favorites.add_contact_to_favorites import add_contact_to_favorites
from Contact_book.contact_book import ContactBook
from data_base import DataBase


class ContactsFrame(ttk.Frame):
    def __init__(self, parent_container, tab_control: ttk.Notebook, contact_book: ContactBook,
                 data_base: DataBase, tree: ttk.Treeview, favorites: ttk.Treeview):
        super().__init__(parent_container)

        self.favorites_frame = parent_container.favorites_frame
        self.tab_control = tab_control
        self.contact_book = contact_book
        self.data_base = data_base
        self.departments_tree = tree
        self.favorites_tree = favorites

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Contacts')

        # Create Label Frame with Search contact
        self.fr1 = ttk.Frame(self)
        self.fr1.grid(row=0, column=0, columnspan=2, pady=10)

        lbl1 = ttk.Label(master=self.fr1, text='Search contact:', font=("BOLD", 10))
        lbl1.grid(row=0, column=0, sticky='nsew', padx=10)

        self.text1 = tk.StringVar()
        self.t1 = ttk.Entry(master=self.fr1, textvariable=self.text1)
        self.t1.bind("<KeyRelease>", lambda event: self.check_entry_content())
        self.t1.focus()
        self.t1.grid(row=0, column=1, sticky='nsew')

        search_icon = tk.PhotoImage(file='Images/search.png')
        close_button = ttk.Button(
            master=self.fr1,
            image=search_icon,
            command=self.search
        )
        close_button.image = search_icon
        close_button.grid(row=0, column=2, sticky='nsew')

        self.btn = ttk.Button(master=self.fr1, text='Cancel', command=self.cancel, cursor='hand2')
        self.btn.grid(row=0, column=3, sticky='nsew', padx=10)
        self.btn.state(['disabled'])

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

        self.contacts_tree.grid(row=1, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.contacts_tree.yview)
        self.contacts_tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=1, column=1, sticky='ns')

        # fill the Contacts tree
        for contact in self.contact_book:
            if contact.favorites:
                insert_contact = ("♥", contact.first_name, contact.last_name, contact.phone_number)
            else:
                insert_contact = ("", contact.first_name, contact.last_name, contact.phone_number)

            self.contacts_tree.insert('', tk.END, values=insert_contact)

        # Create Label Frame with 3 buttons
        self.lf1 = ttk.LabelFrame(self, text='Interaction')
        self.lf1.grid(row=2, column=0, columnspan=2, sticky='ns', pady=10)

        # Button Add contact
        self.b1 = ttk.Button(master=self.lf1, text='Add contact', command=self.add_contact, cursor='hand2')

        # Button Delete contact
        self.b2 = ttk.Button(master=self.lf1, text='Delete contact', command=self.delete_contact, cursor='hand2')

        # Button Rename contact
        self.b3 = ttk.Button(master=self.lf1, text='Edit contact', command=self.edit_contact, cursor='hand2')

        # Button Add to favorites
        self.b4 = ttk.Button(master=self.lf1, text='Add to favorites', command=self.add_to_favorites, cursor='hand2')

        # Location of button Add contact
        self.b1.grid(row=0, column=0, sticky='ns')

        # Location of button Delete contact
        self.b2.grid(row=0, column=1, sticky='ns')
        self.b2.state(['disabled'])

        # Location of button Rename contact
        self.b3.grid(row=0, column=2, sticky='ns')
        self.b3.state(['disabled'])

        # Location of button Add to favorites
        self.b4.grid(row=0, column=3, sticky='ns')
        self.b4.state(['disabled'])

    def check_entry_content(self):
        if self.t1.get():
            self.btn.state(['!disabled'])
        else:
            self.btn.state(['disabled'])

    def search(self):
        letters = self.text1.get().title()
        contact_exist = False

        self.contacts_tree.delete(*self.contacts_tree.get_children())

        for contact in self.contact_book:
            if letters in f"{contact.first_name} {contact.last_name}":
                if contact.favorites:
                    insert_contact = ("♥", contact.first_name, contact.last_name, contact.phone_number)
                else:
                    insert_contact = ("", contact.first_name, contact.last_name, contact.phone_number)

                self.contacts_tree.insert('', tk.END, values=insert_contact)
                contact_exist = True
        self.t1.unbind("<KeyRelease>")

        if contact_exist is False:
            print(f"No results for \"{letters}\"!\nCheck the spelling or try changing the query.")
            messagebox.showerror(title='No results error',
                                 message=f"No results for \"{letters}\"!\n"
                                         f"Check the spelling or try changing the query.")

            for contact in self.contact_book:
                if contact.favorites:
                    insert_contact = ("♥", contact.first_name, contact.last_name, contact.phone_number)
                else:
                    insert_contact = ("", contact.first_name, contact.last_name, contact.phone_number)

                self.contacts_tree.insert('', tk.END, values=insert_contact)

            self.text1.set("")
            self.t1.focus()
            self.btn.state(['disabled'])
            self.t1.bind("<KeyRelease>", lambda event: self.check_entry_content())

    def cancel(self):
        self.contacts_tree.delete(*self.contacts_tree.get_children())

        for contact in self.contact_book:
            if contact.favorites:
                insert_contact = ("♥", contact.first_name, contact.last_name, contact.phone_number)
            else:
                insert_contact = ("", contact.first_name, contact.last_name, contact.phone_number)

            self.contacts_tree.insert('', tk.END, values=insert_contact)

        self.text1.set("")
        self.btn.state(['disabled'])
        self.t1.bind("<KeyRelease>", lambda event: self.check_entry_content())

    def get_buttons_enable(self, contact):
        # remove the disabled flag
        self.b2.state(['!disabled'])
        self.b3.state(['!disabled'])
        self.b4.state(['!disabled'])

    def add_contact(self):
        AddFrame(self, self.fr1, self.lf1, self.scrollbar, self.contact_book, self.data_base,
                 self.contacts_tree, self.departments_tree, self.favorites_tree)

    def delete_contact(self):
        delete_contact_in_all_frames(self.favorites_frame, self.contact_book, self.data_base, self.contacts_tree,
                                     self.departments_tree, self.favorites_tree)

        # make buttons "Add contact", "Delete contact", "Rename contact" disabled
        self.b2.state(['disabled'])
        self.b3.state(['disabled'])
        self.b4.state(['disabled'])

    def edit_contact(self):
        EditFrame(self, self.fr1, self.lf1, self.scrollbar, self.contact_book, self.data_base, self.contacts_tree,
                  self.departments_tree, self.favorites_tree)

    def add_to_favorites(self):
        add_contact_to_favorites(self.contact_book, self.data_base, self.contacts_tree, self.favorites_tree)
