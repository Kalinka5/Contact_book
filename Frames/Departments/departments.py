import tkinter as tk
from tkinter import ttk
from contact_book import Contact


class DepartmentsFrame(ttk.Frame):
    def __init__(self, container, tab_control):
        super().__init__(container)
        self.tab_control = tab_control
        self.dict_departments = {'Work': "0", 'Classmates': "1", 'Friends': "2", 'Relatives': "3", 'Stars': "4"}
        self.__create_widgets()

    def __create_widgets(self):

        self.tab_control.add(self, text='Departments')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # create a treeview
        self.tree = ttk.Treeview(self)
        self.tree.heading('#0', text='Departments', anchor=tk.W)
        headers = ('Work', 'Classmates', 'Friends', 'Relatives', 'Stars')

        for head in headers:
            self.tree.insert('', tk.END, text=head, iid=str(Contact.iid), open=False)
            Contact.iid += 1

        # place the Treeview widget on the root window
        self.tree.grid(row=0, column=0, sticky=tk.NSEW)

        # add a scrollbar
        scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')
