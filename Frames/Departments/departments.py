import tkinter as tk
from tkinter import ttk

from Contact_book.contact import Contact
from Contact_book.contact_book import ContactBook


class DepartmentsFrame(ttk.Frame):
    dict_departments = {'Work': "0", 'Classmates': "1", 'Friends': "2", 'Relatives': "3", 'Stars': "4"}

    def __init__(self, parent_container, tab_control: ttk.Notebook, contact_book: ContactBook):
        super().__init__(parent_container)
        self.tab_control = tab_control
        self.contact_book = contact_book
        self.__create_widgets()

    def __create_widgets(self):

        self.tab_control.add(self, text='Departments')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # create a Departments treeview
        self.departments_tree = ttk.Treeview(self)
        self.departments_tree.heading('#0', text='Departments', anchor=tk.W)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')

        for head in headers:
            self.departments_tree.insert('', tk.END, text=head, iid=str(Contact.iid), open=False)
            Contact.iid += 1

        self.departments_tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.departments_tree.yview)
        self.departments_tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')

        # Fill the departments tree
        amount_all_contacts = len(self.contact_book)

        for contact in self.contact_book:
            self.departments_tree.insert('',
                                         tk.END,
                                         text=f'{contact.first_name} {contact.last_name}',
                                         iid=str(Contact.iid),
                                         open=False)
            self.departments_tree.move(str(Contact.iid),
                                       self.dict_departments[contact.department],
                                       amount_all_contacts)
            Contact.iid += 1
