import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.messagebox import askyesno


class FavoritesFrame(ttk.Frame):
    def __init__(self, container, tab_control, contact_book):
        super().__init__(container)

        self.tab_control = tab_control
        self.contact_book = contact_book

        self.__create_widgets()

    def __create_widgets(self):
        self.tab_control.add(self, text='Favorites')

        columns = ('first_name', 'last_name', 'number')
        self.txt = ttk.Treeview(self, columns=columns, show='headings')
        self.txt.heading('first_name', text='First Name')
        self.txt.heading('last_name', text='Second Name')
        self.txt.heading('number', text='Number')
        self.txt.column('first_name', width=100, anchor=tk.W)
        self.txt.column('last_name', width=100, anchor=tk.W)
        self.txt.column('number', width=200, anchor=tk.CENTER)

        self.txt.bind('<<TreeviewSelect>>', self.get_button_enable)

        self.txt.grid(row=0, column=0, sticky='nsew')

        # add a scrollbar to Contacts Treeview
        self.scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.txt.yview)
        self.txt.configure(yscroll=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky='ns')

        # Create Label Frame with 3 buttons
        self.lf = ttk.LabelFrame(self, text='Interaction')
        self.lf.grid(row=1, column=0, sticky='ns', pady=10)

        self.b1 = ttk.Button(master=self.lf,
                             text='Delete from Favorites',
                             command=self.delete_from_favorites,
                             cursor='hand2')

        self.b1.grid(row=1, column=0, sticky='ns')
        self.b1.state(['disabled'])

    def get_button_enable(self, contact):
        # remove the disabled flag
        self.b1.state(['!disabled'])

    def delete_from_favorites(self):
        human = self.txt.item(self.txt.focus())['values']

        first_name = human[0][3:]
        last_name = human[1]

        if last_name == "":
            answer = askyesno(
                title='Confirmation',
                message=f'Are you sure that you want to delete \"{first_name}\" from the Favorites?')
        else:
            answer = askyesno(
                title='Confirmation',
                message=f'Are you sure that you want to delete \"{first_name} {last_name}\" from the Favorites?')

        if answer:
            # Delete in the FavoritesFrame
            selected_item = self.txt.selection()[0]
            self.txt.delete(selected_item)

            index_txt = None
            for n, user in enumerate(self.contact_book.contacts):
                if first_name == user.first_name:
                    index_txt = n

            contact = self.contact_book.contacts[index_txt]
            contact.favorites = "False"

            # If contact doesn't have lastname
            if last_name == "":
                messagebox.showinfo(
                    title='Update Contact Book',
                    message=f"\"{first_name}\" was deleted from the Favorites successfully!")
                print(f"Deleting \"{first_name}\" from the Favorites was successfully!\n")
            # If contact has firstname and lastname
            else:
                messagebox.showinfo(
                    title='Update Contact Book',
                    message=f"\"{first_name} {last_name}\" was deleted from the Favorites successfully!")
                print(f"Deleting \"{first_name} {last_name}\" from the Favorites was successfully!\n")

            self.b1.state(['disabled'])
