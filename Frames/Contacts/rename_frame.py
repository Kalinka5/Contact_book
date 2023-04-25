from tkinter import ttk
import tkinter as tk
from tkinter.messagebox import askyesno
from contact_book import Contact
from Exceptions.fname_lname_exist import FirstnameLastnameExistException


class RenameFrame(ttk.Frame):
    def __init__(self, container, contacts_txt, contacts_lf, contacts_scrollbar,
                 contact_book, tree, department, favorites, contacts_b2, contacts_b3, contacts_b4):
        super().__init__(container)

        self.contacts_txt = contacts_txt
        self.contacts_lf = contacts_lf
        self.contacts_scrollbar = contacts_scrollbar
        self.contact_book = contact_book
        self.tree = tree
        self.dict_department = department
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
            new_last_name = self.text2.get().capitalize()

            all_names = self.contact_book.get_all_names
            for name in all_names:
                if f"{new_first_name} {new_last_name}" in name:
                    raise FirstnameLastnameExistException()

            if old_last_name == "" and new_last_name == "":
                answer = askyesno(title='Confirmation',
                                  message='Are you sure that you want to rename '
                                          f'\"{old_first_name}\" to \"{new_first_name}\"?')
            elif old_last_name == "":
                answer = askyesno(title='Confirmation',
                                  message='Are you sure that you want to rename '
                                          f'\"{old_first_name}\" to \"{new_first_name} {new_last_name}\"?')
            elif new_last_name == "":
                answer = askyesno(title='Confirmation',
                                  message='Are you sure that you want to rename '
                                          f'\"{old_first_name} {old_last_name}\" to \"{new_first_name}\"?')
            else:
                answer = askyesno(title='Confirmation',
                                  message='Are you sure that you want to rename '
                                          f'\"{old_first_name} {old_last_name}\" to \"{new_first_name} {new_last_name}\"?')
            if answer:
                # Rename contact in the class ContactsFrame
                selected_item = self.contacts_txt.selection()[0]
                self.contacts_txt.delete(selected_item)

                index = 0
                while index < len(self.contacts_txt.get_children()):
                    if new_first_name.lower() < self.contacts_txt.item(self.contacts_txt.get_children()[index])['values'][0].lower():
                        break
                    index += 1

                self.contacts_txt.insert('',
                                         index,
                                         values=(new_first_name, new_last_name, number))

                # Rename contact in the class DepartmentsFrame
                dep_user = None
                for n, user in enumerate(self.contact_book.contacts):
                    if old_first_name == user.first_name:
                        dep_user = user.department

                found_id = None
                for item in self.tree.get_children(self.dict_department[dep_user]):
                    if self.tree.item(item, 'text') == f"{old_first_name} {old_last_name}":
                        found_id = item
                        break

                self.tree.delete(found_id)

                self.tree.insert('', tk.END, text=f'{new_first_name} {new_last_name}', iid=str(Contact.iid), open=False)
                self.tree.move(str(Contact.iid), self.dict_department[dep_user], 0)
                Contact.iid += 1

                # Rename contact in the class FavoritesFrame
                item_id = None
                # Search for the row with contact name in the contact's department column
                for child in self.favorites.get_children():
                    if self.favorites.set(child, "first_name") == old_first_name:
                        item_id = child
                        break

                if item_id is not None:
                    self.favorites.delete(item_id)
                    index = 0
                    while index < len(self.favorites.get_children()):
                        contact = self.favorites.item(self.favorites.get_children()[index])
                        if new_first_name.lower() < contact['values'][1].lower():
                            break
                        index += 1

                    self.favorites.insert('',
                                          index,
                                          values=("🖤", new_first_name, new_last_name, number))

                # Rename contact in the class ContactBook
                index_txt = None
                for n, user in enumerate(self.contact_book.contacts):
                    if number == user.phone_number:
                        index_txt = n

                contact = self.contact_book.contacts[index_txt]
                self.contact_book.rename_contact(contact, new_first_name, new_last_name)

                if old_last_name == "" and new_last_name == "":
                    tk.messagebox.showinfo(
                        title='Update Contact Book',
                        message=f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!")
                    print(f"\"{old_first_name}\" was renamed to \"{new_first_name}\" successfully!\n")
                elif old_last_name == "":
                    tk.messagebox.showinfo(
                        title='Update Contact Book',
                        message=f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!")
                    print(f"\"{old_first_name}\" was renamed to \"{new_first_name} {new_last_name}\" successfully!\n")
                elif new_last_name == "":
                    tk.messagebox.showinfo(
                        title='Update Contact Book',
                        message=f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!")
                    print(f"\"{old_first_name} {old_last_name}\" was renamed to \"{new_first_name}\" successfully!\n")
                else:
                    tk.messagebox.showinfo(
                        title='Update Contact Book',
                        message=f"\"{old_first_name} {old_last_name}\" was renamed to "
                                f"\"{new_first_name} {new_last_name}\" successfully!")
                    print(f"\"{old_first_name} {old_last_name}\" was renamed to "
                          f"\"{new_first_name} {new_last_name}\" successfully!\n")

                self.contacts_b2.state(['disabled'])
                self.contacts_b3.state(['disabled'])
                self.contacts_b4.state(['disabled'])

                # Open ContactsFrame again
                self.contacts_txt.tkraise()
                self.contacts_scrollbar.grid(row=0, column=1, sticky='ns')
                self.contacts_lf.grid(row=1, column=0, sticky='ns')

        except FirstnameLastnameExistException as flee:
            print(flee)
            tk.messagebox.showwarning(title='Update Contact Book',
                                      message="A contact with this name is already in the Contact Book!")
