from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import askyesno

from Exceptions.exist_contact import NameExistException
from Exceptions.invalid_contact import InvalidNameException
from Frames.Contacts.Rename_contact.confirmation_messagebox import confirmation_messagebox
from Frames.Contacts.Rename_contact.successfully_messagebox import successfully_messagebox
from Frames.Contacts.Rename_contact.rename_in_ContactsFrame import rename_in_contacts_frame
from Frames.Contacts.Rename_contact.rename_in_DeparmentsFrame import rename_in_departments_frame
from Frames.Contacts.Rename_contact.rename_in_FavoritesFrame import rename_in_favorites_frame
from Frames.Contacts.Rename_contact.rename_in_ContactBook import rename_in_contact_book


class RenameFrame(ttk.Frame):
    def __init__(self, container, contacts_txt, contacts_lf, contacts_scrollbar,
                 contact_book, tree, favorites, contacts_b2, contacts_b3, contacts_b4):
        super().__init__(container)

        self.contacts_txt = contacts_txt
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.tree = tree
        self.favorites = favorites
        self.contacts_b2 = contacts_b2
        self.contacts_b3 = contacts_b3
        self.contacts_b4 = contacts_b4

        self.__create_widgets()

    def __create_widgets(self):
        item = self.contacts_txt.item(self.contacts_txt.focus())['values']

        self.grid(row=0, column=0, sticky='nsew')

        lf = ttk.LabelFrame(master=self, text='Rename Window')
        if item[1]:
            lf.place(x=85, y=25)
        else:
            lf.place(x=105, y=25)

        download_icon = tk.PhotoImage(file='images/close.png')
        download_button = ttk.Button(
            lf,
            image=download_icon,
            command=self.close_clicked
        )
        download_button.image = download_icon
        download_button.pack(anchor=tk.E)

        if item[1]:
            lbl1 = ttk.Label(master=lf, text=f'You choose the contact \"{item[0]} {item[1]}\".', font=("BOLD", 10))
        else:
            lbl1 = ttk.Label(master=lf, text=f'You choose the contact \"{item[0]}\".', font=("BOLD", 10))
        lbl1.pack(padx=10, pady=10)

        lbl1 = ttk.Label(master=lf, text='New first name:', font=("BOLD", 10))
        lbl1.pack(anchor=tk.W, padx=10, fill=tk.X)

        self.text1 = tk.StringVar()
        t1 = ttk.Entry(master=lf, textvariable=self.text1)
        t1.focus()
        t1.pack(anchor=tk.W, padx=10, fill=tk.X)

        lbl2 = ttk.Label(master=lf, text='New last name:', font=("BOLD", 10))
        lbl2.pack(anchor=tk.W, padx=10, fill=tk.X)

        self.text2 = tk.StringVar()
        t2 = ttk.Entry(master=lf, textvariable=self.text2)
        t2.pack(anchor=tk.W, padx=10, fill=tk.X)

        btn = ttk.Button(master=lf, text='Rename contact', command=self.rename, cursor='hand2')
        btn.pack(anchor=tk.E, padx=10, pady=5)

        self.tkraise()
        self.contacts_scrollbar.grid_forget()
        self.contacts_lf.grid_forget()

    def close_clicked(self):
        self.contacts_txt.tkraise()
        self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
        self.contacts_lf.grid(row=1, column=0, sticky='ns')

    def rename(self):
        try:
            item = self.contacts_txt.item(self.contacts_txt.focus())['values']

            old_first_name = item[0]
            old_last_name = item[1]
            number = item[2]
            new_first_name = self.text1.get().capitalize()
            if new_first_name == "":
                new_first_name = "Mr/Mrs"
            new_last_name = self.text2.get().capitalize()

            # check first name is it has less than 10 letters and more than 0
            if len(new_first_name) < 1 or len(new_first_name) > 12:
                raise InvalidNameException(new_first_name)
            # check last name is it has less than 10 letters and more than 0
            if len(new_last_name) > 12:
                raise InvalidNameException(new_last_name)

            all_names = self.contact_book.get_all_names
            for name in all_names:
                if f"{new_first_name} {new_last_name}" in name:
                    raise NameExistException()

            # print confirmation messagebox "Are you sure that you want to rename?"
            answer = confirmation_messagebox(old_first_name, old_last_name, new_first_name, new_last_name)

            if answer:
                # rename contact in the class ContactsFrame
                rename_in_contacts_frame(self.contacts_txt, new_first_name, new_last_name, number)

                # rename contact in the class DepartmentsFrame
                rename_in_departments_frame(self.contact_book, self.tree, old_first_name,
                                            old_last_name, new_first_name, new_last_name)

                # rename contact in the class FavoritesFrame
                rename_in_favorites_frame(self.favorites, old_first_name, new_first_name, new_last_name, number)

                # rename contact in the class ContactBook
                rename_in_contact_book(self.contact_book, new_first_name, new_last_name, number)

                # notify user that the contact has been renamed successfully
                successfully_messagebox(old_first_name, old_last_name, new_first_name, new_last_name)

                # make buttons "Add contact", "Delete contact", "Rename contact" disabled
                self.contacts_b2.state(['disabled'])
                self.contacts_b3.state(['disabled'])
                self.contacts_b4.state(['disabled'])

                # Open ContactsFrame again
                self.contacts_txt.tkraise()
                self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
                self.contacts_lf.grid(row=1, column=0, sticky='ns')

        except NameExistException as nee:
            print(nee)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message="A contact with this name is already in the Contact Book!")
        except InvalidNameException as ine:
            print(ine)
            tk.messagebox.showwarning(title='Name error',
                                      message=ine)
